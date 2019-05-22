from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import Catalog, Shop

class CatalogForm(forms.ModelForm):
    class Meta:
        model = Catalog
        fields = '__all__'


class ShopForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = '__all__'
        #exclude = ['catalog']



class SignupForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    last_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        # fields = ('username', 'password1', 'password2')
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def clean(self):
        data = super().clean()

        password1 = data.get('password1')
        password2 = data.get('password2')

        if password1 != password2:
            self.error = 'รหัสไม่ตรงกันนะจ้ะ'
            raise ValidationError('รหัสไม่ตรงกัน')
        # elif start < datetime.datetime.now().date():
        #     self.error = 'Please do not fill date in past'
        #     raise ValidationError('กรุณากรอกวันที่ให้ถูกต้อง')
