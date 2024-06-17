from django.db.models.query import QuerySet
from django.shortcuts import redirect, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth import login
from .models import Petition, ContactUS
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_POST
from django.views.generic import TemplateView


class Index(FormView):
    template_name = 'api/index.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('petition-list')

class CustomLoginView(LoginView):
    template_name = 'api/login.html'
    field = '__all__'
    redirect_authenticated_user = True #Redirects to the home page if the user is already authenticated
    
    def get_success_url(self):
        return reverse_lazy('petition-list')

#  creating our own view for registration
class ResgisterPage(FormView, SuccessMessageMixin):
    template_name = 'api/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('petition-list')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
            messages.success(self.request, "User registered and logged in successfully.")
        else:
            messages.error(self.request, "User registration failed.")
        return super(ResgisterPage, self).form_valid(form)
    
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated: #Redirects to the home page if the user is already authenticated
            messages.info(self.request, "You are already authenticated.")
            return redirect('petition-list')
        return super(ResgisterPage, self).get(*args, **kwargs)

class MyProfile(LoginRequiredMixin ,ListView):
    model = Petition
    template_name = 'api/myprofile.html'
    context_object_name = 'petitions'  # Default is object_list

    # only display petitions created by the logged in user
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['petitions'] = context['petitions'].filter(user=self.request.user).order_by('-updated_at')
        
        # search functionality, search by title only
        search_input = self.request.GET.get('search') or ''
        if search_input:
            context['petitions'] = context['petitions'].filter(
                title__icontains=search_input)

        context['search_input'] = search_input
        return context
    

class ChangePassword(LoginRequiredMixin, SuccessMessageMixin, FormView):
    template_name = 'api/change-password.html'
    success_message = "Password updated successfully"
    form_class = PasswordChangeForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('login')

class PetitionList(LoginRequiredMixin, ListView):
    model = Petition
    template_name = 'api/petitionlist.html'
    context_object_name = 'petitions'  # Default is object_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # search functionality, search by title or username
        search_input = self.request.GET.get('search') or ''
        if search_input:
            context['petitions'] = context['petitions'].filter(title__icontains=search_input) | context['petitions'].filter(user__username__icontains=search_input)
        context['search_input'] = search_input
        return context

    def get_queryset(self):
        return Petition.objects.all().order_by('-updated_at')
    
class PetitionDetails(LoginRequiredMixin, DetailView):
       model = Petition
       template_name = 'api/petitiondetails.html'
       context_object_name = 'petition'  # Default is object

    # sign and unsign petition logic
       def dispatch(self, request, *args, **kwargs):
           action = kwargs.get('action')
           if action == 'sign_petition':
               return self.sign_petition(request, *args, **kwargs)
           elif action == 'unsign_petition':
               return self.unsign_petition(request, *args, **kwargs)
           return super().dispatch(request, *args, **kwargs)

       @method_decorator(login_required)
       @method_decorator(require_POST)
       def sign_petition(self, request, *args, **kwargs):
           petition = self.get_object()
           if request.user not in petition.signed_users.all():
               petition.signed_users.add(request.user)
               petition.signature_count += 1
               petition.save()
           return redirect('petition_detail', pk=petition.id)

       @method_decorator(login_required)
       @method_decorator(require_POST)
       def unsign_petition(self, request, *args, **kwargs):
           petition = self.get_object()
           if request.user in petition.signed_users.all():
               petition.signed_users.remove(request.user)
               petition.signature_count -= 1
               petition.save()
           return redirect('petition_detail', pk=petition.id)
       
class PetitionCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Petition
    template_name = 'api/create-petition.html'
    fields = ['title', 'description']
    success_url = reverse_lazy('petition-list')
    success_message = "Petition submitted successfully"
    
     # petition can created by the logged in user only
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PetitionCreate, self).form_valid(form)


class PetitionUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Petition
    template_name = 'api/update-petition.html'
    fields = ['title', 'description']
    success_url = reverse_lazy('petition-list')
    success_message = "Petition updated successfully"

    # only owner of the petition can update the petition
    def dispatch(self, request, *args, **kwargs):
        petition = self.get_object()
        if petition.user != request.user:
                return HttpResponseForbidden(
                    "<h1>404 Forbidden</h1><p>You are not the creator of this petition.</p>"
                    "<p>Only the creator of the petition can update the petition.</p>"
                    "<button onclick='window.location.href=\"/\"'>Go Back to homepage</button>"
                )
        return super().dispatch(request, *args, **kwargs)



class PetitionDelete(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Petition
    template_name = 'api/petition_confirm_delete.html'
    success_url = reverse_lazy('petition-list')
    success_message = "Petition deleted successfully"

    # only owner of the petition can delete the petition
    def dispatch(self, request, *args, **kwargs):
        petition = self.get_object()
        if petition.user != request.user:
            return HttpResponseForbidden(
                "<h1>403 Forbidden</h1><p>You are not the creator of this petition.</p>"
                "<p>Only the creator of the petition can delete the petition.</p>"
                "<button onclick='window.location.href=\"/\"'>Go Back to homepage</button>"
            )
        return super().dispatch(request, *args, **kwargs)

class ContactUs(CreateView, SuccessMessageMixin):
    model = ContactUS
    template_name = 'api/index.html'
    fields = '__all__'
    success_url = reverse_lazy('thank-you')
    success_message = "Message sent successfully"

class ThankYou(TemplateView):
    template_name = 'api/thankyou.html'
