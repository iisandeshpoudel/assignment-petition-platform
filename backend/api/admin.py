from django.contrib import admin
from .models import Petition, ContactUS
# Register your models here.

admin.site.register(Petition) 
admin.site.register(ContactUS)

# contact model 