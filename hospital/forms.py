from django import forms
from django.contrib.auth.models import User
from  . import models




#for patient related form
# class PatientUserForm(forms.Form):
#     class Meta:
#         model=User
#         fields=['first_name','last_name','username','password']
#         widgets = {
#         'password': forms.PasswordInput()
#         }
# class PatientForm(forms.Form):
#     class Meta:
#         model=Patient
#         fields= '__all__'
        
class PatientUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }
class PatientForm(forms.ModelForm):
    #this is the extrafield for linking patient and their assigend doctor
    #this will show dropdown __str__ method doctor model is shown on html so override it
    #to_field_name this will fetch corresponding value  user_id present in Doctor model and return it
    
    class Meta:
        model=models.Patient
        fields= '__all__'

     
