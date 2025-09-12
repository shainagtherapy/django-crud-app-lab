from django.db import models

# Create your models here.
class Sticker(models.Model):
    giphy_id = models.CharField(max_length=64, unique=True)
    title = models.CharField(max_length=255, blank=True)
    preview_url = models.URLField()
    original_url = models.URLField()

    def __st__(self):
        return self.title or self.giphy_id
    
    
class Stickerbook(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField('Start Date')
    description = models.TextField(max_length=250)
    stickers = models.JSONField(default=list, blank=True) 

    def __str__(self):
        return self.name