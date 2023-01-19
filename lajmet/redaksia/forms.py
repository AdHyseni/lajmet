from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import TextInput


from flash.models import Lajmi
 
 
 
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    phone_no = forms.CharField(max_length = 20)
    first_name = forms.CharField(max_length = 20)
    last_name = forms.CharField(max_length = 20)
    class Meta:
        model = User
        fields = ['username', 'email', 'phone_no', 'password1', 'password2']


class LajmiForm(forms.ModelForm):
    foto = forms.ImageField(required=False)
    
    class Meta:
        model =Lajmi
        fields = '__all__'
        exclude = ['slug','autori']
        
class LajmiUpdateForm(forms.ModelForm):
    foto = forms.ImageField(required=False)
    
    class Meta:
        model =Lajmi
        fields = '__all__'
        exclude = ['slug','autori']
      

