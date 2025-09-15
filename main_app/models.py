from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class Stickerbook(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField('Start Date')
    description = models.TextField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('stickerbook-detail', kwargs={'stickerbook_id': self.id})
    
class Sticker(models.Model):
    title = models.CharField(max_length=255, blank=True)
    preview_url = models.URLField()
    original_url = models.URLField()
    stickerbook = models.ForeignKey(Stickerbook, on_delete=models.CASCADE)

    def __str__(self):
        return self.title or self.giphy_id
    
    # stickerbook = models.ForeignKey(
    #     Stickerbook,
    #     on_delete=models.CASCADE,
    #     related_name="stickers"
    # )
    # image = models.ImageField(upload_to="stickers/")
    # caption = models.CharField(max_length=100, blank=True)

    # def __str__(self):
    #     return f"Sticker in {self.stickerbook.name}"
    
