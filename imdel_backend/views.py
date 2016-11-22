from django.http import HttpResponse, HttpResponseBadRequest
from django.contrib.auth.models import User
from django.db import IntegrityError

from rest_framework.views import APIView
from rest_framework.authtoken.models import Token

from rest_framework import permissions

import json

class Register(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        if request.method == 'POST':
            try: 
                # TODO: user id increases even if exception is raised, rewrite try/catch to if/else
                user = User.objects.create_user(
                    username = request.data['username'],
                    password = request.data['password'])
                user.save()
                token = Token.objects.get(user=user)

                return HttpResponse(json.dumps({"user_id" : user.id, "token" : token.key}))
            except IntegrityError:
                return HttpResponseBadRequest(json.dumps({"status":"failed", "reason":"username taken"}))


class Login(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        if request.method == 'POST':
            try:
                user = User.objects.get(username=request.POST['username'])
                if user.check_password(request.POST['password']):
                    token = Token.objects.get(user=user)
                    return HttpResponse(json.dumps({"user_id" : user.id, "token" : token.key}))
                else:
                    return HttpResponseBadRequest(json.dumps({"status":"failed", "reason":"wrong password"}))
            except:
                return HttpResponseBadRequest(json.dumps({"status":"failed", "reason":"username not registered"}))

