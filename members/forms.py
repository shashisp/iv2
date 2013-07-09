from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from members.models import Member

class RegistrationForm(ModelForm):
		username = forms.CharField(label=(u'User Name'))
		email = forms.EmailField(label=(u'Email Address'))
		password = forms.CharField(label=(u'Password')), #widget=forms.PasswordInput(render_value=False))
		password = forms.CharField(label=(u'Verify Password')) #widget=forms.PasswordInput(render_value=False))


class Meta:
        model = Member
        exclude = ('user',)


        def clean_username(self):
                                        username = self.cleaned_data['username']
                                        try:
                                                User.objects.get(username=username)
                                        except User.DoesNotExists:
                                                        return username
                                        raise forms.ValidationError("That Username already Taken")


        def clean_password(self):
                                password = self.cleaned_data['password']
                                password1 = self.cleaned_data['password1']
                                if password != password1:
                                                raise forms.ValidationError("Passwords are not same")
                                return password
                        

                        	