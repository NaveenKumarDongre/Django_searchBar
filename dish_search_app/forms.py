from django import forms

class query_form(forms.Form) :
    query = forms.CharField(max_length=20, label="Search Dishes")