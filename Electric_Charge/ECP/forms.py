

from django import forms
from .models import Signup

class SignupModelForm(forms.ModelForm):
   class Meta:
       db_table="Users"
       model=Signup
       fields=['user','first_name','second_name','email','password']
       widgets = {
            'first_name': forms.TextInput(
				attrs={
					'class': 'form-control',
                    'placeholder':"First Name",
                    'required':False
					}
				),
            'second_name':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':"Last Name"
                }
            ),
            'email':forms.EmailInput(
                attrs={
                    'class':'form-control',
                    'placeholder':"Email address"
                }
            ),
            'password':forms.PasswordInput(
                attrs={
                    'class':'form-control',
                    'placeholder':"Password"
                }
            ),
        }

# class SignupModelForm(forms.ModelForm):
#         class Meta:
#             model = signup
#             fields = ('user','first_name', 'second_name', 'email','password')
      
   