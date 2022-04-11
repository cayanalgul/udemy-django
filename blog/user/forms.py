from django import forms
from sklearn.model_selection import learning_curve


class LoginForm(forms.Form):
    username = forms.CharField(label="Kullanıcı Adı")
    password = forms.CharField(label="Şifre",widget=forms.PasswordInput)



class RegsiterForm(forms.Form):

    username = forms.CharField(max_length=50,label="Kullanıcı Adı")
    password = forms.CharField(max_length=20,label="Şifre",widget= forms.PasswordInput)
    confirm = forms.CharField(max_length=20,label="Şifre doğrula",widget= forms.PasswordInput)

    def clean(self):

        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")

        if password and confirm and password != confirm:
            raise forms.ValidationError("Şifreler Eşleşmiyor")

        
        values = {
            "username":username,
            "password":password,
            "confirm" :confirm,
        }

        return values

    