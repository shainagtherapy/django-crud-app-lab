import requests


from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.http import require_GET
from django.shortcuts import render
from .models import Sticker, Stickerbook


# Define the home view function
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def stickerbook_index(request):
    stickerbook = Stickerbook.objects.all()
    return render(request, 'stickerbooks/index.html', {'stickerbook': stickerbook})

def stickerbook_detail(request, sticker_id):
    stickerbook = Stickerbook.objects.get(id=sticker_id)
    return render(request, 'stickerbooks/detail.html', {'stickerbook': stickerbook})



@require_GET
def giphy_search(request):
    q = request.GET.get("q", "").strip()
    limit = int(request.GET.get("limit", 24))
    if not q:
        return JsonResponse({"results": []})

    url = "https://api.giphy.com/v1/stickers/search"
    params = {
        "api_key": settings.GIPHY_API_KEY,
        "q": q,
        "limit": limit,
        "rating": "pg",
        "lang": "en",
    }
    r = requests.get(url, params=params, timeout=10)
    r.raise_for_status()
    raw = r.json().get("data", [])

    #Suggestions for UI
    results = []
    for item in raw:
        images = item.get("images", {})
        # fallbacks for safety:
        preview = (images.get("fixed_height_small") or
                   images.get("fixed_height") or
                   images.get("downsized")) or {}
        original = images.get("original", {})
        results.append({
            "id": item.get("id"),
            "title": item.get("title", ""),
            "preview": preview.get("url"),
            "original": original.get("url"),
        })

    return JsonResponse({"results": results})