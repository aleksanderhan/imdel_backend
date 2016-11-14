from django.forms import ModelForm

from .models import ImageModel


class UploadImageForm(ModelForm):
    class Meta:
        model = ImageModel
        fields = ['image', 'imageText', 'latitude', 'longitude']

