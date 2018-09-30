from django import forms
from django.contrib.auth.models import User
from basic_app.models import Order, Address


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'

class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ('quantity','delivery_date', 'billing_address')
        widgets = {
            'delivery_date': forms.DateInput(format=('%m/%d/%Y'),
                                             attrs={'class': 'form-control',
                                                    'type': 'date'}),
        }

    def __init__(self, user ,*args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields['quantity'].widget.attrs['class'] = 'form-control'
        self.fields['billing_address'].widget.attrs['class'] = 'form-control'
        self.fields['billing_address'].queryset = Address.objects.filter(user=user)


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ('city', 'line1', 'line2', 'phone_number')

    def __init__(self, *args, **kwargs):
        super(AddressForm, self).__init__(*args, **kwargs)
        self.fields['city'].widget.attrs['class'] = 'form-control'
        self.fields['line1'].widget.attrs['class'] = 'form-control'
        self.fields['line2'].widget.attrs['class'] = 'form-control'
        self.fields['phone_number'].widget.attrs['class'] = 'form-control'
