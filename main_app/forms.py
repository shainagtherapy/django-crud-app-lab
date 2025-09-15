from django import forms
from .models import Sticker

class StickerForm(forms.ModelForm):
    class Meta:
        model = Sticker
        fields = ['title', 'preview_url', 'original_url', 'stickerbook']