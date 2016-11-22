from __future__ import unicode_literals

from django.db import models
from django.conf import settings

from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


def image_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    #return 'user_{0}/{1}'.format(instance.user.id, filename)
    return '{publisher}/{filename}'.format(publisher=instance.publisher, filename=filename)


# This code is triggered whenever a new user has been created and saved to the database
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
    

class Photos(models.Model):
    publisher = models.ForeignKey('auth.User', related_name='photos', on_delete=models.CASCADE)
    published_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to=image_path)
    text = models.CharField(max_length=200, blank=True)
    latitude = models.DecimalField(max_digits= 8, decimal_places=6)
    longitude = models.DecimalField(max_digits = 9, decimal_places=6)


'''
class Votes(models.Model):
    image = models.ForeignKey(ImageModel, on_delete=models.CASCADE)
    votes = models.IntegerField(default=0)
'''


