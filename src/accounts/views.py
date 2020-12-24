from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, login, authenticate
from django.views.generic import ListView, DetailView
from .forms import CreateUserForm


def home_view(request):
    return render(request, "accounts/index.html")


def create_user_form(request):
    """
    Registration view
    """
    context = {}
    if request.POST:
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            raw_password = form.cleaned_data["password1"]
            account = authenticate(
                username=username,
                password=raw_password,
            )
            login(request, account)
            return redirect("home")
        else:
            context["registration_form"] = form
    else:
        form = CreateUserForm()
        context["registration_form"] = form
    return render(request, "accounts/register.html", context)


class UserListView(ListView):
    """
    Lists all the users with a link to their details page and number of their logins.
    """

    model = get_user_model()
    template_name = "accounts/user_list.html"


class UserDetailView(DetailView):
    """
    Slows all the details about selected user.
    """

    model = get_user_model()
    template_name = "accounts/user_details.html"
