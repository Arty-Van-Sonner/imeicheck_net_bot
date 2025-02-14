from django.shortcuts import render

import json
from django.views import View
from django.http import JsonResponse
from telegram import Update
from imeicheck_net_bot.settings import TElEGRAM_BOT_TOKEN
from rest_framework import status
from rest_framework.response import Response 
from .models import *

# Create your views here.
def imei_api(request):
    if request.method != 'POST':
        response_status = status.HTTP_400_BAD_REQUEST
        return Response()