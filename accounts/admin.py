from django.contrib import admin
from django import forms
from accounts import models


# class LoginForm(forms.Form):
#     username = forms.CharField(max_length=63, label='Nom d\'utilisateur')
#     password = forms.CharField(max_length=63, widget=forms.PasswordInput, label='Mot de pass')

class UserForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = ("username", "password", "first_name", "last_name", "user_type", "is_admin")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
    

@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    
    form = UserForm

    list_display = ('first_name', 'last_name', 'username', 'password', "is_admin")
    list_filter = ("user_type",)



    # save du form