from django.conf import settings
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from litreview import forms, models

def login_page(request):
    form = forms.LoginForm()
    message = ""

    if request.method == "POST":
        form = forms.LoginForm(request.POST)
        
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            
            if user is not None:
                login(request, user)
                return redirect("home")
            
            else:
                message = "Identifiants incorrects."
    
    context = {
        "form": form,
        "message": message
    }

    return render(request, "litreview/login.html", context=context)


def home(request):
    return render(request, "litreview/home.html")


def signup_page(request):
    form = forms.SignupForm()
    if request.method == "POST":
        form = forms.SignupForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    
    return render(request, "litreview/signup.html", context={"form": form})


@login_required
def follow_users(request):
    form = forms.FindUserForm()
    followed_users = models.UserFollows.objects.filter(user=request.user)
    following_users = models.UserFollows.objects.filter(followed_user=request.user)

    if request.method == "POST":
        form = forms.FindUserForm(request.POST)

        if form.is_valid():
            followed_username = form.cleaned_data["username"]
            
            try:
                followed_user = models.User.objects.get(username=followed_username)

                if followed_user == request.user:
                    messages.error(request, "Vous ne pouvez pas vous suivre !")
                
                else:
                    if not models.UserFollows.objects.filter(
                    user=request.user,
                    followed_user=followed_user).exists():
                        userfollows_object = models.UserFollows(
                            user=request.user, 
                            followed_user=followed_user)
                        
                        userfollows_object.save()
                        
                        messages.success(request, f"Vous vous êtes abonnés à {followed_user} !")
                    
                    else:
                        messages.warning(request, f"Vous suivez déjà {followed_user}.")
            
            except models.User.DoesNotExist:
                messages.error(request, "Cet utilisateur n'existe pas.")

        return redirect("follow_users")
        
    return render(request, 
                  "litreview/follow_user_form.html", 
                  context={"form": form,
                           "followed_users": followed_users,
                           "following_users": following_users})


@login_required
def unfollow_user(request, id):
    if request.method == "POST":

        followed_user_id = request.POST.get("unfollow_user")
        
        try:
            followed_user = models.User.objects.get(id=followed_user_id)
            follow_object = models.UserFollows.objects.get(user=request.user, followed_user=followed_user)
            follow_object.delete()
            messages.success(request, f"Vous ne suivez plus {followed_user}.")
            return redirect("follow_users")


        except (models.User.DoesNotExist, models.UserFollows.DoesNotExist):
            messages.error(request, "Erreur lors de la suppression de l'abonnement.")

    return redirect("follow_users")


@login_required
def create_ticket(request):
    form = forms.TicketForm()

    if request.method == "POST":
        form = forms.TicketForm(request.POST)
        
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            return redirect("home")
    
    context = {
        "form": form,
    }

    return render(request, "litreview/create_ticket.html", context=context)


@login_required
def edit_ticket(request, id):
    ticket = get_object_or_404(models.Ticket, id=id)
    edit_form = forms.TicketForm(instance=ticket)

    if request.method == "POST":
        
        if "edit_ticket" in request.POST:
            edit_form = forms.TicketForm(request.POST, instance=ticket)
            
            if edit_form.is_valid():
                edit_form.save()
                return redirect("home")
                  
    context = {
        "edit_form": edit_form,
    }

    return render(request, "litreview/edit_ticket.html", context=context)


@login_required
def delete_ticket(request, id):
    ticket = get_object_or_404(models.Ticket, id=id)
    delete_form = forms.DeleteTicketForm()

    if request.method == "POST":
        
        if "delete_ticket" in request.POST:
            delete_form = forms.DeleteTicketForm(request.POST)
            
            if delete_form.is_valid():
                ticket.delete()
                return redirect("home")
                
    context = {
        "delete_form": delete_form,
    }

    return render(request, "litreview/delete_ticket.html", context=context)


@login_required
def create_review(request):
    ticket_form = forms.TicketForm()
    review_form = forms.ReviewForm()

    if request.method == "POST":
        ticket_form = forms.TicketForm(request.POST, request.FILES)
        review_form = forms.ReviewForm(request.POST)
        
        if any ([ticket_form.is_valid(), review_form.is_valid()]):
            ticket = ticket_form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            
            review = review_form.save(commit=False)
            review.user = request.user
            review.ticket = ticket
            review.save()
            
            return redirect("home")
    
    context = {
        "ticket_form": ticket_form,
        "review_form": review_form,
    }

    return render(request, "litreview/create_review.html", context=context)


@login_required
def edit_review(request, id):
    review = get_object_or_404(models.Review, id=id)
    edit_form = forms.ReviewForm(instance=review)

    if request.method == "POST":
        
        if "edit_review" in request.POST:
            edit_form = forms.ReviewForm(request.POST, instance=review)
            
            if edit_form.is_valid():
                edit_form.save()
                return redirect("home")
            
    context = {
        "edit_form": edit_form,
    }

    return render(request, "litreview/edit_review.html", context=context)


@login_required
def delete_review(request, id):
    review = get_object_or_404(models.Review, id=id)
    delete_form = forms.DeleteReviewForm()

    if request.method == "POST":
        
        if "delete_review" in request.POST:
            delete_form = forms.DeleteReviewForm(request.POST)
            
            if delete_form.is_valid():
                review.delete()
                return redirect("home")
                
    context = {
        "delete_form": delete_form,
    }

    return render(request, "litreview/delete_review.html", context=context)