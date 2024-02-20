from django import forms 

from .models import ViewUser,site_about







class commentt(forms.ModelForm):
    class Meta:
        model = ViewUser
        fields = ['rate','movie2','user']
 


class site_comment(forms.ModelForm):
    class Meta:
        model = site_about
        fields = ['comment']