from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from myuserapp.models import MyUser
from myuserapp.forms import LoginForm, AddUserForm
from myuser_proj.settings import AUTH_USER_MODEL

# Create your views here.


@login_required
def index_view(request):
    my_user = MyUser.objects.all()
    return render(request, "index.html", {"users": my_user, "auth": AUTH_USER_MODEL})


def create_user(request):
    if request.method == "POST":
        form = AddUserForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            MyUser.objects.create_user(username=data.get(
                "username"), password=data.get("password"), display_name=data.get("display_name"))

            return HttpResponseRedirect(reverse("homepage"))

    form = AddUserForm
    return render(request, "generic_form.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data.get(
                "username"), password=data.get("password"))
            if user:
                login(request, user)
                return HttpResponseRedirect(request.GET.get('next', reverse("homepage")))
            else:
                return HttpResponseRedirect(request.GET.get('next', reverse("adduser")))

    form = LoginForm
    return render(request, "generic_form.html", {"form": form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("homepage"))
