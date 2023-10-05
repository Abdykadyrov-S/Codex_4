from django import forms


class MailForm(forms.Form):
    url = forms.CharField(
        label="URL", widget=forms.Textarea(attrs={"rows": 1})
    )
    email = forms.EmailField(label="Email Address")