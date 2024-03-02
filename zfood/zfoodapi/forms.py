from django import forms

class ClientForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50)
    email = forms.EmailField()
    phone = forms.CharField(max_length=20)
    occupation = forms.CharField(max_length=50)
    country = forms.CharField(max_length=20)
    city = forms.CharField(max_length=20)
    delegation = forms.CharField(max_length=50)
    created_at = forms.DateTimeField()
    updated_at = forms.DateTimeField()


class SaveFile(forms.Form):
    file = forms.FileField()