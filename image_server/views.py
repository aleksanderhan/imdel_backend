from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotAllowed, FileResponse
from django.views.decorators.csrf import csrf_exempt

from math import cos, sin, acos, radians
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
        id = request.POST['id']
        imageObject = ImageModel.objects.get(pk = id)

        # send image text and publication date too
 
        response = FileResponse(open(imageObject.image, 'rb'), content_type='image/jpeg')

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

        SQL = _create_sql(latitude, longitude, radius, amount, offset)

        '''
        for p in ImageModel.objects.raw(SQL):
            print p.id, p.image
        '''


        return HttpResponse()

    else:
        return HttpResponseNotAllowed(['POST'])



# Helper function to create sql to get all pictures within a given radius
# 'latitude' and 'longitude' in degrees
# 'radius' in km
# 'amount' is the amount of pictures retrived
# 'offset' is from which place in the list to start getting the images
def _create_sql(latitude, longitude, radius, amount, offset, sorting='distance'):
    SQL = """SELECT id, image
             FROM (SELECT id, image, (3959 * acos(cos(radians({lat})) * cos(radians(latitude)) * cos(radians(longitude) - radians({long})) + sin(radians({lat})) * sin(radians(latitude )))) AS distance 
                   FROM image_server_imagemodel) AS sub_query
                   WHERE distance < {radius}
                   ORDER BY {sorting} LIMIT {amount} OFFSET {offset};""".format(lat=latitude, long=longitude, radius=radius, amount=amount, offset=offset, sorting=sorting)
    return SQL


