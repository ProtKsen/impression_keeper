from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import redirect, render


@user_passes_test(lambda u: u.is_anonymous, login_url="home")
def auth_login(request):
    """Page for selecting an authentication method"""
    return render(request, "login.html")


@login_required
def auth_logout(request):
    """Logging out of the user profile page"""
    logout(request)
    return redirect("home")
