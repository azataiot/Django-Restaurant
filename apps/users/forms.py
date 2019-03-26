# users/forms.py
from django import forms

# form 是数据库之前的,所以可以在 forms 中检验,这样减轻数据库的负担

class LoginForm(forms.Form):
  username = forms.CharField(required=True)  # 必须与 HTML 中的字段一样
  password = forms.CharField(required=True, min_length=5)  # 必须与 HTML 中的字段一样