from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.utils.datastructures import MultiValueDictKeyError

from app.models import Address



def list(request):
    address=Address.objects.all()
    return HttpResponse(address)


def index(request):
    address = ''
    try:
        address = request.GET['address']


        add = Address(address=address)
        add.save()
        #save() 를 호출하면 기록을 저장해줌.


    except MultiValueDictKeyError:
        pass


    return HttpResponse('{"Hello":'+address+'"}')



