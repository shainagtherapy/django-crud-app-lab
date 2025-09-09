from django.shortcuts import render
from .models import Sticker

# Define the home view function
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def sticker_index(request):
    stickers = Sticker.objects.all()
    return render(request, 'stickers/index.html', {'stickers': stickers})