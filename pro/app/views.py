from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .task import * 
from .helper import *


    

def home(request):
    # add.delay(10)
    # sleep(10)
    send_mail_with_out_celery()
    return HttpResponse("heeolo from celery")



















