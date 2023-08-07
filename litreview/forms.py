from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from litreview.models import UserFollows


class LoginForm(forms.Form):
    username = forms.CharField(max_length=15, label="Nom d'utilisateur")
    password = forms.CharField(max_length=15, widget=forms.PasswordInput, label="Mot de passe")


class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ("username", "email")
        exclude = ("first_name",
                   "last_name",
                   "groups",
                   "user_permissions", 
                   "is_staff", 
                   "is_active", 
                   "is_superuser", 
                   "last_login", 
                   "date_joined",)


class UserFollowsForm(forms.ModelForm):
    username = forms.CharField(max_length=15, label="Nom d'utilisateur")

    class Meta:
        model = get_user_model()
        fields = ["follows"]


class FindUserForm(forms.Form):
    username = forms.CharField(max_length=15, label="", widget=forms.TextInput(attrs={"placeholder": "Nom d'utilisateur"}))


class UnfollowUser(forms.Form):
    unfollow_user = forms.BooleanField(widget=forms.HiddenInput, initial=True)