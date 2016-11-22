from django.http import HttpResponse, HttpResponseBadRequest
from django.contrib.auth.models import User
from django.db import IntegrityError

from rest_framework.views import APIView
from rest_framework.authtoken.models import Token

from rest_framework import permissions


class Register(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        if request.method == 'POST':
            try: 
                user = User.objects.create_user(
                    username = request.POST['username'],
                    password = request.POST['password'])
                return HttpResponse()
            except IntegrityError:
                return HttpResponseBadRequest()


class Login(APIView):
    def post(self, request):
        if request == 'POST':
            #token = Token.objects.create(user=...)
            #print token.key
            return HttpResponse()
