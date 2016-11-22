from rest_framework import serializers
from .models import Photos
from django.contrib.auth.models import User


class PhotoSerializer(serializers.ModelSerializer):
	publisher = serializers.PrimaryKeyRelatedField(many=False, queryset=User.objects.all())

	class Meta:
		model = Photos
		fields =('publisher', 'image', 'text', 'latitude', 'longitude')