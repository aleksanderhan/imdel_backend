from __future__ import unicode_literals

from django.db import models
from django.conf import settings


def image_path(instance, filename):
	# file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
	#return 'user_{0}/{1}'.format(instance.user.id, filename)
	return '{filename}'.format(filename=filename)
    

class ImageModel(models.Model):
    pub_date = models.DateTimeField(auto_now_add=True)
    #uploader_ip = models.CharField()
    image = models.FileField(upload_to=image_path)
    text = models.CharField(max_length=200, blank=True)
    latitude = models.DecimalField(max_digits= 8, decimal_places=6)
    longitude = models.DecimalField(max_digits = 9, decimal_places=6)


'''
class Votes(models.Model):
    image = models.ForeignKey(ImageModel, on_delete=models.CASCADE)
    votes = models.IntegerField(default=0)
'''


