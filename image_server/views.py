from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotAllowed, FileResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

import json, base64

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
                text = request.POST['imageText'], 
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


@csrf_exempt
def get_picture(request):
    if request.method == 'POST':
        id = int(request.POST['id'])
        imageObject = ImageModel.objects.get(pk = id)

        response = FileResponse(open(settings.MEDIA_ROOT + imageObject.image.name, 'rb'), content_type='image/jpeg')
        return response

    else:
        return HttpResponseNotAllowed(['POST'])


@csrf_exempt
def get_thumbnails(request):
    if request.method == 'POST':
        latitude = request.POST['latitude']
        longitude = request.POST['longitude']
        radius = request.POST['radius']
        amount = request.POST['amount']
        offset = request.POST['offset']

        # Stopping SQL injections
        try:
            float(latitude)
            float(longitude)
            float(radius)
            int(amount)
            int(offset)
        except ValueError:
            return HttpResponseBadRequest("400")


        # Create sql query
        SQL = _create_sql(latitude, longitude, radius, amount, offset)
        # Query database
        query_result = ImageModel.objects.raw(SQL)
        
        # Create response
        response_dict = {}
        i = 1
        for imageObject in query_result:
            thumb_dict = {}
            thumb = open(get_thumb_path(imageObject.image.url)).read()
            thumb_dict['base64Thumb'] = base64.standard_b64encode(thumb)
            thumb_dict['filename'] = imageObject.image.name
            thumb_dict['id'] = imageObject.id
            thumb_dict['text'] = imageObject.text
            thumb_dict['pub_date'] = str(imageObject.pub_date)
            response_dict[i] = thumb_dict
            i += 1

        return HttpResponse(json.dumps(response_dict), content_type='application/json')


    else:
        return HttpResponseNotAllowed(['POST'])



# Helper function to create sql to get all pictures within a given radius
# 'latitude' and 'longitude' in degrees
# 'radius' in km
# 'amount' is the amount of pictures retrived
# 'offset' is from which place in the list to start getting the images
def _create_sql(latitude, longitude, radius, amount, offset, sorting='distance'):
    SQL = """SELECT id, image, pub_date, text 
             FROM (SELECT id, image, pub_date, text, (3959 * acos(cos(radians({lat})) * cos(radians(latitude)) * cos(radians(longitude) - radians({long})) + sin(radians({lat})) * sin(radians(latitude )))) AS distance 
                   FROM image_server_imagemodel) AS sub_query
                   WHERE distance < {radius}
                   ORDER BY {sorting} LIMIT {amount} OFFSET {offset};""".format(lat=latitude, long=longitude, radius=radius, amount=amount, offset=offset, sorting=sorting)
    return SQL


def _create_thumb_tar(query_result):
    out = tarfile.open('temp.tar', 'w')



def get_thumb_path(filename):
    return settings.MEDIA_ROOT + "thumb_" + filename
