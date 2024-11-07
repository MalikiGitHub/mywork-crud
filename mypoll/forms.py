from django import forms
from .models import Poll

class PollForm(forms.ModelForm):
    author = forms.CharField(label='Author', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Author name'}), required=True)
    categories = forms.CharField(label='Categories', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'categories'}), required=True)
    tag = forms.CharField(label='Tag(s)', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'tag'}), required=True)
    post = forms.CharField(label='Post', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'post'}), required=False)
    
    
    class Meta:
        model = Poll
        fields = ['author', 'categories', 'tag', 'post']
   