from django.urls import path
from .views import Index, CustomLoginView, ResgisterPage, MyProfile, ChangePassword, PetitionDetails, PetitionCreate, PetitionUpdate, PetitionDelete, PetitionList, ContactUs, ThankYou
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', Index.as_view(), name='home'),
    path('petition/', PetitionList.as_view(),name='petition-list'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(template_name='api/logout.html'), name='logout'), # directly using the default LogoutView class instead of using custom view
    path('register/', ResgisterPage.as_view(), name='register'),
    path('myprofile/<int:pk>/', MyProfile.as_view(), name='myprofile'),
    path('change-password/', ChangePassword.as_view(success_message="Password changed successfully"), name='change-password'),
    path('create-petition/', PetitionCreate.as_view(success_message="Petition created successfully"), name='create-petition'),
    path('update-petition/<int:pk>/', PetitionUpdate.as_view(success_message="Petition updated successfully"), name='update-petition'),
    path('delete-petition/<int:pk>/', PetitionDelete.as_view(success_message="Petition deleted successfully"), name='delete-petition'),
    path('petition/<int:pk>/', PetitionDetails.as_view(), name='petition_detail'),
    path('petition/<int:pk>/sign/', PetitionDetails.as_view(), {'action': 'sign_petition'}, name='sign_petition'),
    path('petition/<int:pk>/unsign/', PetitionDetails.as_view(), {'action': 'unsign_petition'}, name='unsign_petition'),
    path('contact-us/', ContactUs.as_view(), name='contact-us'),
    path('thankyou/', ThankYou.as_view(), name='thank-you'),
]
