from django.core import serializers
from django.shortcuts import HttpResponse
import datetime



# Posts data into given entity's collection
def InsertData(*args):
    args[1]['date'] = datetime.datetime.utcnow()
    print(args[1])
    args[0].insert_one(args[1])
