from django.shortcuts import render

class Sticker:
    def __init__(self, name, shape, brand, description):
        self.name = name
        self.shape = shape
        self.brand = brand
        self.description = description

stickers = [
    Sticker('Donatello', 'outline', 'TMNT', 'Purple Ninja-turtle'),
    Sticker('Dolphins', 'outline', 'Lisa Frank', 'Dancing Dolphins'),
    Sticker('Star', 'star', 'generic', 'Multi-colored star set'),
    Sticker('Firestone', 'outline', 'Firestone Brewing', 'Firestone Brewing classic logo')
]

# Define the home view function
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def sticker_index(request):
    return render(request, 'stickers/index.html', {'stickers': stickers})