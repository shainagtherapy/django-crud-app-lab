from django.urls import path
from . import views # Import views to connect routes to view functions

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('stickerbooks/', views.stickerbook_index, name='stickerbook-index'),
    path('stickerbooks/<int:stickerbook_id>/', views.stickerbook_detail, name='stickerbook-detail'),
    path('stickerbooks/create/', views.StickerbookCreate.as_view(), name='stickerbook-create'),
    path('stickerbooks/<int:pk>/update/', views.StickerbookUpdate.as_view(), name='stickerbook-update'),
    path('stickerbooks/<int:pk>/delete/', views.StickerbookDelete.as_view(), name='stickerbook-delete'),
    path('stickerbooks/<int:stickerbook_id>/add-sticker/', views.add_sticker, name='add-sticker'),
    path('accounts/signup/', views.signup, name='signup'),    
]