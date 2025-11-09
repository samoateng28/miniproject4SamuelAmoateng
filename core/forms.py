# INF601 - Advanced Programming in Python
# samuel Amoateng
# Mini Project 4

from django import forms

class ContactForm(forms.Form):
    """
    A simple contact form for user inquiries.
    """
    # Name field - required, max length 100
    name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Your Full Name'
        })
    )
    
    # Email field - uses EmailInput for browser validation
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'name@example.com'
        })
    )
    
    # Subject field - optional, but useful
    subject = forms.CharField(
        max_length=150,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Subject (e.g., Partnership Inquiry)'
        })
    )
    
    # Message field - large textarea
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 5, 
            'placeholder': 'Type your detailed message here...'
        }),
        required=True
    )
    
    


from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # Only allow users to edit these fields
        fields = ('title', 'content', 'status') 
        
        # Apply modern Bootstrap classes to form fields
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'A catchy title for your post'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 15, 'placeholder': 'Start writing your amazing content here...'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
        }