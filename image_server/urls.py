from django.conf.urls import url, include

from . import views

urlpatterns = [
	url(r'^fetch_thumbnails/', views.FetchThumbnails.as_view(), name='fetch_thumbnails'),
	url(r'^get_photo/(?P<id>[0-9]+)/', views.GetPhoto.as_view(), name='get_photo'),
    url(r'^publish_photo/', views.PublishPhoto.as_view(), name='publish_photo'),
]