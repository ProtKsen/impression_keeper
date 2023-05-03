from django import forms

from user_profile.models import Place


class PlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ("name", "latitude", "longitude", "comment")
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Название"}),
            "comment": forms.Textarea(attrs={"placeholder": "Комментарий", "rows": 4}),
        }
