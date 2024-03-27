from django import forms
from .models import Project, Project2

from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django.contrib.auth.models import User



class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'industry_sector', 'target_market', 'unique_value_proposition', 'key_objectives']


class ProjectForm2(forms.ModelForm):
    class Meta:
        model = Project2
        fields = ['customer_segments', 'value_proposition', 'channels', 'customer_relationships', 'revenue_streams',
                  'key_resources', 'key_activities', 'key_partners', 'cost_structure' ]
