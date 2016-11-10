from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotAllowed
import json

from .forms import UploadImageForm
from .models import ImageModel

from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def upload_image(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            instance = ImageModel(file=request.FILES['file'])
            instance.save()
            return HttpResponse(json.dumps({'success': True}), content_type='application/json')
        else:
            return HttpResponseBadRequest()
    else:
        return HttpResponseNotAllowed(['POST'])