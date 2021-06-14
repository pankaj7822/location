from django.shortcuts import render
from .models import Location
import json
from django.http import HttpResponse


def home(request):
    ip = request.META.get('REMOTE_ADDR', None)
    return render(request, 'index.html')

def getlocation(request):
    r=json.loads(request.body)
    ip=r['ip']
    x=r['lat']
    y=r['long']
    print(ip)
    if(x and y):
        url="https://maps.google.com/?q="+str(x)+","+str(y)
        print(url)
        loc_obj=Location(ip=ip,gps=url)
    else:
        loc_obj=Location(ip=ip)
    loc_obj.save()
    return HttpResponse(json.dumps({"data":x}))