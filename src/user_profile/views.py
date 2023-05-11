import os

from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import redirect, render

from user_profile.forms import PlaceForm
from user_profile.models import Place


@login_required
def user_profile(request):
    user = request.user
    places = Place.objects.filter(user=request.user.id)
    context = {"user": user, "places": places}
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
    return render(request, "edit_place.html", context)


@login_required
def edit_place(request, id: int):
    place = Place.objects.get(id=id)
    initial_data = {
        "name": place.name,
        "comment": place.comment,
        "latitude": place.latitude,
        "longitude": place.longitude,
    }
    if request.method == "POST":
        form = PlaceForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data

            new_place_data = {}
            for key, val in form_data.items():
                if val:
                    new_place_data[key] = val
            new_place_data["user"] = request.user
            place = Place.objects.get(id=id)
            for key, value in new_place_data.items():
                setattr(place, key, value)
            place.save()
            return redirect("user_profile")
        form = PlaceForm(initial=initial_data)
        context = {"form": form}
        return render(request, "edit_place.html", context)
    else:
        form = PlaceForm(initial=initial_data)
        context = {"form": form}
        return render(request, "edit_place.html", context)


@login_required
def delete_place(request, id: int):
    place = Place.objects.get(id=id)
    place.delete()
    return redirect("user_profile")
