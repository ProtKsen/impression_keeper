import os

from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import redirect, render

from user_profile.forms import PlaceForm
from user_profile.models import Place


@login_required
def user_profile(request):
    user = request.user
    context = {"user": user}
    return render(request, "user_profile.html", context=context)


@login_required
def add_place(request):
    if request.method == "POST":
        form = PlaceForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data

            place_data = {}
            for key, val in form_data.items():
                if val:
                    place_data[key] = val

            place_data["user"] = request.user
            place = Place(**place_data)
            place.save()
            return redirect("user_profile")

    form = PlaceForm()
    context = {"ymap_api_key": os.environ["YANDEX_MAPS_API_KEY"], "form": form}
    return render(request, "add_place.html", context)
