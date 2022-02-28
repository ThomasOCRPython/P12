from django.contrib import admin
from django import forms
from accounts import models


class UserForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = (
            "username",
            "password",
            "first_name",
            "last_name",
            "user_type",
            "is_admin",
        )

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):

    form = UserForm

    def group(self, user):
        groups = []
        for group in user.groups.all():
            groups.append(group.name)
        return " ".join(groups)

    group.short_description = "Groups"

    list_display = (
        "first_name",
        "last_name",
        "username",
        "password",
        "is_admin",
        "group",
    )
    list_filter = ("user_type",)
