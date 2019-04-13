from django import forms

class AddCommentForm(forms.Form):
    title = forms.CharField(label='Title', max_length=100)
    email = forms.EmailField(label='Email', max_length=100)
