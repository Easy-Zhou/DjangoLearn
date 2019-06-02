from django import forms
from django.forms import widgets
from blog.models import UserInfo
from django.core.exceptions import ValidationError


# form 组件
class RegisterForm(forms.Form):
    username = forms.CharField(max_length=8, label="用户名",
                               widget=widgets.TextInput(attrs={"class": "form-control", "placeholder": "Username"}))
    password = forms.CharField(min_length=4, label="密码",
                               widget=widgets.PasswordInput(attrs={"class": "form-control", "placeholder": "Password"}))
    repeat_password = forms.CharField(min_length=4, label="确认密码",
                                      widget=widgets.PasswordInput(
                                          attrs={"class": "form-control", "placeholder": "Confirm"}))
    email = forms.EmailField(label="邮箱",
                             widget=widgets.EmailInput(attrs={"class": "form-control", "placeholder": "Email"}))

    # 局部钩子
    def clean_username(self):
        username = self.cleaned_data.get('username')
        user = UserInfo.objects.filter(username=username)
        if user:
            raise ValidationError("用户已存在")
        else:
            return username

    # 全局钩子
    def clean(self):
        if self.cleaned_data.get("password") == self.cleaned_data.get("repeat_password"):
            return self.cleaned_data
        else:
            raise ValidationError("两次密码不一致")
