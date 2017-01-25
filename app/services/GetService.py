from django.core import serializers
from django.shortcuts import HttpResponse
from app.services.conn import *



def GetOne():
    return user.find_one()
        

