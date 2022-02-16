from django import forms

class CreatorProductForm(forms.Form):
    title = forms.CharField(max_length=200)
    subcategory = forms.IntegerField
