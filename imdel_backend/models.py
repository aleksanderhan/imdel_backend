from __future__ import unicode_literals

from django.db import models


class ImageModel(models.Model):
    file = models.FileField(upload_to="user_images")
    pub_date = models.DateTimeField(auto_now_add=True)
