from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse

# Create your views here.


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponse("Login successful!")
        else:
            return HttpResponse("Invalid credentials. Please try again.")
    return render(request, "login.html")
