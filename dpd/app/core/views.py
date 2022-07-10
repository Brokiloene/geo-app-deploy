import json
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404, JsonResponse
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from .models import Session, TargetCords, ZoneCords, UserCords
from django.db import IntegrityError

def create(request): #создание сессии, клиенту будет прислан ses_id в json
    s = Session()
    s.save()
    val = getattr(s, 'ses_id')
    return JsonResponse(json.dumps({val}), safe=False)

def getuser(request, ses_id): #отправка всех координат пользователей с сервера к клиенту
    #field_value = getattr(s, 'ses_id')
    #SomeModel_json = serializers.serialize("json", UserCords.objects.filter(ses_id=1).values("lapt", "long"))
    #data = {"UserCords": json.dumps(list_to_json)}
    if (not(Session.objects.filter(ses_id=ses_id).exists())): #проверка ses_id
        return HttpResponse(status=404)

    list_to_json = list(UserCords.objects.values("lapt", "long").filter(ses_id=ses_id))
    return JsonResponse(list_to_json, safe=False)

def getzone(request, ses_id): #отправка всех координат зоны поиска от сервера к клиенту
    if (not(Session.objects.filter(ses_id=ses_id).exists())):
        return HttpResponse(status=404)

    list_to_json = list(ZoneCords.objects.values("lapt", "long").filter(ses_id=ses_id))
    return JsonResponse(list_to_json, safe=False)

def gettarg(request, ses_id): #отправка координат целей поиска от сервера к клиенту
    if (not(Session.objects.filter(ses_id=ses_id).exists())):
        return HttpResponse(status=404)

    list_to_json = list(TargetCords.objects.values("lapt", "long").filter(ses_id=ses_id))
    return JsonResponse(list_to_json, safe=False) 

def adduser(request, ses_id): #отправка координат пользователя от клиента к серверу 
    if (not(Session.objects.filter(ses_id=ses_id).exists())):
        return HttpResponse(status=404)
    lapt_list = request.GET.getlist('lapt')
    long_list = request.GET.getlist('long')
    if (len(lapt_list) != len(long_list) or len(lapt_list) == 0): #количество присланных
        return HttpResponse(status=400)                           #длинн/широт должно совпадать

    s = Session.objects.get(ses_id=ses_id)
    for lpt, lng in zip(lapt_list, long_list):
        if(UserCords.objects.filter(ses_id=ses_id, lapt=lpt, long=lng).exists()): #если уже есть координата такого типа с тем же значением -- 
            continue;                                                             #не добавлять в базу данных
        s.usercords_set.create(lapt=lpt, long=lng)
    return HttpResponse(status=204)

def addzone(request, ses_id):
    if (not(Session.objects.filter(ses_id=ses_id).exists())):
        return HttpResponse(status=404)
    lapt_list = request.GET.getlist('lapt')
    long_list = request.GET.getlist('long')
    if (len(lapt_list) != len(long_list) or len(lapt_list) == 0):
        return HttpResponse(status=400)

    s = Session.objects.get(ses_id=ses_id)
    for lpt, lng in zip(lapt_list, long_list):
        if(ZoneCords.objects.filter(ses_id=ses_id, lapt=lpt, long=lng).exists()):
            continue;
        s.zonecords_set.create(lapt=lpt, long=lng)
    return HttpResponse(status=204)

def addtarg(request, ses_id):
    if (not(Session.objects.filter(ses_id=ses_id).exists())):
        return HttpResponse(status=404)
    lapt_list = request.GET.getlist('lapt')
    long_list = request.GET.getlist('long')
    if (len(lapt_list) != len(long_list) or len(lapt_list) == 0):
        return HttpResponse(status=400)  

    s = Session.objects.get(ses_id=ses_id)
    for lpt, lng in zip(lapt_list, long_list):
        if(TargetCords.objects.filter(ses_id=ses_id, lapt=lpt, long=lng).exists()):
            continue;
        s.targetcords_set.create(lapt=lpt, long=lng)
    return HttpResponse(status=204)

def endsession(request, ses_id): #завершение сессии, также все полученные к это сессии координаты
    if (not(Session.objects.filter(ses_id=ses_id).exists())):
        return HttpResponse(status=400)
    if (not(Session.objects.filter(ses_id=ses_id).exists())):
        return HttpResponse(status=404)
    s = Session.objects.get(ses_id=ses_id)
    s.delete()
    return HttpResponse(status=204)
    
    
    
    
   
    
