from typing import Any
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from litreview.models import Ticket, Review
from crispy_forms.helper import FormHelper


class LoginForm(forms.Form):
    """Collects the requested information to enable an user to log in."""
    username = forms.CharField(max_length=15,
                               label="",
                               widget=forms.TextInput(attrs={
                                   "class": "centered-placeholder",
                                   "placeholder": "Nom d'utilisateur", }))
    password = forms.CharField(max_length=15,
                               label="",
                               widget=forms.PasswordInput(attrs={
                                   "class": "centered-placeholder",
                                   "placeholder": "Mot de passe"}),)


class SignupForm(UserCreationForm):
    """Collects the requested information to enable an user to sign in."""
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

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """
        This is used to show personalised placeholder labels in the form
        instead of default ones.
        """
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({
            "placeholder": "Nom d'utilisateur",
        })
        self.fields["email"].widget.attrs.update({
            "placeholder": "Adresse mail",
        })
        self.fields["password1"].widget.attrs.update({
            "placeholder": "Mot de passe",
        })
        self.fields["password2"].widget.attrs.update({
            "placeholder": "Confirmation du mot de passe",
        })

        self.helper = FormHelper(self)
        self.helper.form_show_labels = False


class FindUserForm(forms.Form):
    """Collects the name of the user that is wanted to be followed."""
    username = forms.CharField(max_length=15,
                               label="",
                               widget=forms.TextInput(attrs={
                                   "placeholder": "Nom d'utilisateur"}))


class UnfollowUser(forms.Form):
    """Used to unfollow an user."""
    unfollow_user = forms.BooleanField(widget=forms.HiddenInput, initial=True)


class TicketForm(forms.ModelForm):
    """Collects the relevant information to create a Ticket object."""
    class Meta:
        model = Ticket
        fields = ["title", "description", "image"]


class DeleteTicketForm(forms.Form):
    """Used to delete a ticket."""
    delete_ticket = forms.BooleanField(widget=forms.HiddenInput, initial=True)


class ReviewForm(forms.ModelForm):
    """Collects the relevant information to create a Review object."""
    rating = forms.ChoiceField(choices=[(str(i), str(i)) for i in range(6)],
                               label="Note")

    class Meta:
        model = Review
        fields = ["headline", "rating", "body"]


class DeleteReviewForm(forms.Form):
    """Used to delete a review."""
    delete_review = forms.BooleanField(widget=forms.HiddenInput, initial=True)
