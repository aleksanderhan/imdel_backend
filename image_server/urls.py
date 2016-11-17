from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^get_thumbnails', views.get_thumbnails, name='get_thumbnails'),
	url(r'^get_picture', views.get_picture, name='get_picture'),
    url(r'^upload_image', views.upload_image, name='upload_image'),
]