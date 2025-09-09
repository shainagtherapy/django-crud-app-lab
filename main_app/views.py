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

def sticker_detail(request, sticker_id):
    sticker = Sticker.objects.get(id=sticker_id)
    return render(request, 'stickers/detail.html', {'sticker': sticker})
