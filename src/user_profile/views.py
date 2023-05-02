from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import redirect, render


@login_required
def user_profile(request):
    user = request.user
    context = {"user": user}
    return render(request, "user_profile.html", context=context)
