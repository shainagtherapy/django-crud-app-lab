import requests
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.http import require_GET

from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Stickerbook, Sticker
from .forms import StickerForm
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

class Home(LoginView):
    template_name = 'home.html'

class StickerbookCreate(LoginRequiredMixin, CreateView):
    model = Stickerbook
    fields = '__all__'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class StickerbookUpdate(LoginRequiredMixin, UpdateView):
    model = Stickerbook
    fields = '__all__'

class StickerbookDelete(LoginRequiredMixin, DeleteView):
    model = Stickerbook
    success_url = '/stickerbooks/'



# Define the home view function
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def stickerbook_index(request):
    stickerbooks = Stickerbook.objects.filter(user=request.user)
    return render(request, 'stickerbooks/index.html', {'stickerbooks': stickerbooks})

@login_required
def stickerbook_detail(request, stickerbook_id):
    stickerbook = Stickerbook.objects.get(id=stickerbook_id)
    sticker_form = StickerForm()
    return render(request, 'stickerbooks/detail.html', {'stickerbook': stickerbook, 'sticker_form' : sticker_form })

@login_required
def add_sticker(request, stickerbook_id):
    form = StickerForm(request.POST)

    if form.is_valid():
        new_sticker = form.save(commit=False)
        new_sticker.stickerbook_id = stickerbook_id
        new_sticker.save()
    return redirect('stickerbook-detail', stickerbook_id=stickerbook_id)

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('stickerbook-index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)



# Beginnings of GIPHY API integration:
# @require_GET
# def giphy_search(request):
#     q = request.GET.get("q", "").strip()
#     limit = int(request.GET.get("limit", 24))
#     if not q:
#         return JsonResponse({"results": []})

#     url = "https://api.giphy.com/v1/stickers/search"
#     params = {
#         "api_key": settings.GIPHY_API_KEY,
#         "q": q,
#         "limit": limit,
#         "rating": "pg",
#         "lang": "en",
#     }
#     r = requests.get(url, params=params, timeout=10)
#     r.raise_for_status()
#     raw = r.json().get("data", [])

#     #Suggestions for UI
#     results = []
#     for item in raw:
#         images = item.get("images", {})
#         # fallbacks for safety:
#         preview = (images.get("fixed_height_small") or
#                    images.get("fixed_height") or
#                    images.get("downsized")) or {}
#         original = images.get("original", {})
#         results.append({
#             "id": item.get("id"),
#             "title": item.get("title", ""),
#             "preview": preview.get("url"),
#             "original": original.get("url"),
#         })

#     return JsonResponse({"results": results})