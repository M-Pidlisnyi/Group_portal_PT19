from django import forms
from .models import GalleryItem

class GalleryItemForm(forms.ModelForm):
    class Meta:
        model = GalleryItem
        fields = ['title', 'description', 'media_type', 'file']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }
