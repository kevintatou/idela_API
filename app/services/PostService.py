from django.core import serializers
from django.shortcuts import HttpResponse



# Posts data into given entity's collection
def InsertData(*args):
    args[0].insert_one(args[1])


    