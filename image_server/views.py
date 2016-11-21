from django.http import HttpResponse, HttpResponseBadRequest, FileResponse
from django.conf import settings

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

import json, base64

from .serializers import PhotoSerializer
from .models import PhotoModel

from thumbnailer import makeThumbnail


class PublishPhoto(APIView):
    def post(self, request, format=None):
        if request.method == 'POST':
            serializer = PhotoSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()

                # Create thumbnail
                filename = request.FILES['image'].name
                makeThumbnail(filename)

                return Response(status=status.HTTP_201_CREATED)


class FetchPhoto(APIView):
    def post(request):
        if request.method == 'POST':
            id = int(request.POST['id'])
            print id
            photoObject = PhotoModel.objects.get(pk = id)
            print photoObject

            response = FileResponse(open(settings.MEDIA_ROOT + photoObject.image.name, 'rb'), content_type='image/jpeg')
            return response


class FetchThumbnails(APIView):
    def post(request):
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
                return HttpResponseBadRequest()

            # Create sql query
            SQL = _create_sql(latitude, longitude, radius, amount, offset)
            # Query database
            query_result = ImageModel.objects.raw(SQL)
            
            # Create response
            response_dict = {}
            i = 1
            for photoObject in query_result:
                thumb_dict = {}
                thumb = open(get_thumb_path(photoObject.image.url)).read()
                thumb_dict['base64Thumb'] = base64.standard_b64encode(thumb)
                thumb_dict['filename'] = photoObject.image.name
                thumb_dict['id'] = photoObject.id
                thumb_dict['text'] = photoObject.text
                thumb_dict['pub_date'] = str(photoObject.pub_date)
                thumb_dict['distance'] = photoObject.distance
                response_dict[i] = thumb_dict
                i += 1

            return HttpResponse(json.dumps(response_dict), content_type='application/json')


def _create_sql(latitude, longitude, radius, amount, offset, sorting='distance'):
    # Helper function to create sql query to get all pictures within a given radius
    # 'latitude' and 'longitude' in degrees
    # 'radius' in km
    # 'amount' is the amount of pictures retrived
    # 'offset' is from which place in the list to start getting the images
    SQL = """SELECT id, image, pub_date, text, distance  
             FROM (SELECT id, image, pub_date, text, (3959 * acos(cos(radians({lat})) * cos(radians(latitude)) * cos(radians(longitude) - radians({long})) + sin(radians({lat})) * sin(radians(latitude )))) AS distance 
                   FROM image_server_imagemodel) AS sub_query
                   WHERE distance < {radius}
                   ORDER BY {sorting} LIMIT {amount} OFFSET {offset};""".format(lat=latitude, long=longitude, radius=radius, amount=amount, offset=offset, sorting=sorting)
    return SQL


def get_thumb_path(filename):
    return settings.MEDIA_ROOT + "thumb_" + filename
