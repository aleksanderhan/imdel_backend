from django.conf.urls import url, include

from . import views

urlpatterns = [
	url(r'^fetch_thumbnails', views.FetchThumbnails.as_view(), name='fetch_thumbnails'),
	url(r'^fetch_photo', views.FetchPhoto.as_view(), name='fetch_photo'),
    url(r'^publish_photo', views.PublishPhoto.as_view(), name='publish_photo'),
]