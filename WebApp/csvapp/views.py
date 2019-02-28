# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from collections import OrderedDict
import json
from django.shortcuts import HttpResponse
from .models import csvdata
def home(request,key):
    data = OrderedDict()
    data["key"] = key
    result = csvdata.objects.filter(key=key)
    if result:
        result = result.first()
        data["value"] = result.value
    else:
        data["value"] = "Data is not present in loaded CSV File"
    return HttpResponse(json.dumps(data))

def default(request):
    return HttpResponse("<h1>Please try http://127.0.0.1/one<h1>")