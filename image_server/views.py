from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt
import json

from .forms import UploadImageForm
from .models import ImageModel

from thumbnailer import makeThumbnail


@csrf_exempt
def upload_image(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            instance = ImageModel(
                image = request.FILES['image'],
                text = request.POST['text'], 
                latitude = request.POST['latitude'], 
                longitude = request.POST['longitude'])
            instance.save()

            filename = request.FILES['image'].name
            makeThumbnail(filename)

            return HttpResponse(json.dumps({'success': True}), content_type='application/json')
        else:
            return HttpResponseBadRequest("400 invalid form")
    else:
        return HttpResponseNotAllowed(['POST'])