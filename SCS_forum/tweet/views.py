from django.shortcuts import render
from .models import tweet
from .forms import UserRegistrationForm, tweetForm
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login


def index(request):
    """
    Renders the 'index.html' template as the homepage of the application.
    """
    return render(request, "index.html")


"""
Renders the 'tweet_list.html' template with a context containing tweets ordered by creation date.
"""


def tweet_list(request):
    tweets = tweet.objects.order_by("-created_at")
    return render(request, "tweet_list.html", {"tweets": tweets})


"""
Creates a new tweet based on the form data submitted by the user.
If the request method is POST, validates the form data, saves the tweet with the user information, 
and redirects to the tweet list page upon successful creation.
If the method is not POST, renders the tweet creation form page for the user to input data.
"""


@login_required
def tweet_create(request):
    if request.method == "POST":
        form = tweetForm(request.POST, request.FILES)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect("tweet_list")
    else:
        form = tweetForm
    return render(request, "tweet_form.html", {"form": form})


"""
Edits a specific tweet based on the provided tweet ID. 
If the request method is POST, updates the tweet with the new form data and saves the changes. 
Redirects to the tweet list page after successful editing. 
If the method is not POST, renders the 'tweet_form.html' template with the tweet form data.
"""


@login_required
def tweet_edit(request, tweet_id):
    tweet_instance = get_object_or_404(tweet, pk=tweet_id, user=request.user)
    if request.method == "POST":
        form = tweetForm(request.POST, request.FILES, instance=tweet_instance)
        if form.is_valid():
            tweet_instance = form.save(commit=False)
            tweet_instance.user = request.user
            tweet_instance.save()
            return redirect("tweet_list")
    else:
        form = tweetForm(instance=tweet_instance)
    return render(request, "tweet_form.html", {"form": form})


"""
Deletes a specific tweet based on the provided tweet ID. 
If the request method is POST, the tweet is deleted and the user is redirected to the tweet list page. 
Otherwise, renders the 'tweet_confirm_delete.html' template with the tweet information.
"""


def tweet_delete(request, tweet_id):
    tweet_instance = get_object_or_404(tweet, pk=tweet_id, user=request.user)
    if request.method == "POST":
        tweet_instance.delete()
        return redirect("tweet_list")
    return render(request, "tweet_confirm_delete.html", {"tweet": tweet_instance})


# def register(request):
#     if request.method == "POST":
#         form = UserRegisterForm(request.POST)
#         if form.is_valid():
#             user = form.save()(commit=False)
#             user.set_password(form.cleaned_data["password1"])
#             user.save()
#             login(request, user)
#             return redirect("tweet_list")
#     else:
#         form = UserRegisterForm()
#     return render(request, "registration/register.html", {"form": form})


"""
Registers a new user based on the provided request data. If the request method is POST, 
validates the user registration form and saves the user details. 
Then, logs in the user and redirects to the tweet list page. If the method is not POST, renders the user registration form page.
"""


def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password1"])
            user.save()
            login(request, user)
            return redirect("tweet_list")
    else:
        form = UserRegistrationForm()
    return render(request, "registration/register.html", {"form": form})


"""
Renders a list of tweets based on a search query if provided, otherwise renders all tweets.
"""


def search(request):
    if query := request.GET.get("q"):
        tweets = tweet.objects.filter(text__icontains=query)
    else:
        tweets = tweet.objects.all()
    return render(request, "tweet_list.html", {"tweets": tweets})
