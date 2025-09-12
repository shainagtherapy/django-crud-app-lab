from django.urls import path
from . import views # Import views to connect routes to view functions

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('stickerbooks/', views.stickerbook_index, name='stickerbook-index'),
    path('stickerbooks/<int:stickerbook_id>/', views.stickerbook_detail, name='stickerbook-detail'),

]