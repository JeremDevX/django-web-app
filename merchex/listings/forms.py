from django import forms

from listings.models import Band, Listing

class ContactUsForm(forms.Form):
    name = forms.CharField(required=False)
    email = forms.EmailField()
    message = forms.CharField(max_length=1000, widget=forms.Textarea(attrs={"rows": 4}))

class BandForm(forms.ModelForm):
    class Meta:
        model = Band
        exclude = ("active", "official_homepage")


class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = "__all__"