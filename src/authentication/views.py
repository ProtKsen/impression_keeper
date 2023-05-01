from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import redirect, render


@user_passes_test(lambda u: u.is_anonymous, login_url="home")
def login(request):
    return render(request, "login.html")
