from __future__ import unicode_literals

from django.db import models


class ImageModel(models.Model):
    pub_date = models.DateTimeField(auto_now_add=True)
    image = models.FileField(upload_to="uploaded_images")
    imageText = models.CharField(max_length=200, blank=True)
    latitude = models.DecimalField(max_digits= 8, decimal_places=6)
    longitude = models.DecimalField(max_digits = 9, decimal_places=6)


'''
class Votes(models.Model):
    image = models.ForeignKey(ImageModel, on_delete=models.CASCADE)
    votes = models.IntegerField(default=0)
'''