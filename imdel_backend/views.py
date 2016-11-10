from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import UploadImageForm
from .models import ImageModel


def upload_image(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            instance = ImageModel(file_field=request.FILES['image'])
            instance.save()
            return HttpResponseRedirect('/success/url/')
    else:
        form = UploadImageForm()
    return render(request, 'upload.html', {'form': form})