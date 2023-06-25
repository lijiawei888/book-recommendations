from django import  forms
from captcha.fields import CaptchaField
from bookStore.models import BookUser
from django.core.exceptions import ValidationError

class Login_Form(forms.Form):
    user=forms.CharField(label='用户名',required=True,max_length=20,
                         widget=forms.TextInput(attrs={'class':'form-control','placeholder':'请输入用户名'}),
                         error_messages={
                             'required':'必要的',
                             'max_length':'最大20位'
                         })
    pwd=forms.CharField(label='密码',required=True,min_length=6,max_length=20,
                        widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'请输入密码'}),
                        error_messages={
                            'required': '必要的',
                            'max_length': '最大20位',
                            'min_length':'最小6位'
                        })
    captcha=CaptchaField(label='验证码',required=True,
                        error_messages={
                            'required': '必选项',
                            'invalid':'验证码错误'
                        })
    def clean_user(self):
        user=self.cleaned_data.get('user')
        user1=BookUser.objects.filter(username=user)
        if not user1:
            raise ValidationError('用户不存在')
        return user