from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from litreview.models import UserFollows, Ticket, Review


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


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ["title", "description", "image"]


class DeleteTicketForm(forms.Form):
    delete_ticket = forms.BooleanField(widget=forms.HiddenInput, initial=True)


class ReviewForm(forms.ModelForm):
    rating = forms.ChoiceField(choices=[(str(i), str(i)) for i in range(6)], widget=forms.RadioSelect)

    class Meta:
        model = Review
        fields = ["headline", "rating", "body"]


class DeleteReviewForm(forms.Form):
    delete_review = forms.BooleanField(widget=forms.HiddenInput, initial=True)   