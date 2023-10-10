from django import forms
from customer.models import Customer


class FormDangKy(forms.ModelForm):
    first_name = forms.CharField(max_length=264, label='First Name', widget=forms.TextInput(attrs={
        "class": "form-control", "placeholder": "Tên",
    }))
    last_name = forms.CharField(max_length=264, label='Last Name', widget=forms.TextInput(attrs={
        "class": "form-control", "placeholder": "Họ",
    }))
    email = forms.EmailField(label='Email', widget=forms.TextInput(attrs={
        "class": "form-control", "placeholder": "Email",
    }))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={
        "class": "form-control", "placeholder": "Mật khẩu",
    }))
    confirm_password = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={
        "class": "form-control", "placeholder": "Xác nhận Mật khẩu",
    }))
    phone = forms.CharField(max_length=20, label='Phone', widget=forms.TextInput(attrs={
        "class": "form-control", "placeholder": "Điện thoại",
    }))
    address = forms.CharField(label='Address', widget=forms.Textarea(attrs={
        "class": "form-control", "placeholder": "Địa chỉ", "rows": "3",
    }))
    class Meta:
        model = Customer
        fields = '__all__'