from django.http import JsonResponse
from .models import user_entry
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
import pika
import random

@csrf_exempt
def create(request):
    if request.method != 'POST':
        return JsonResponse({'status': 'please send a post request'})
    user_id = request.POST.get('user_id')
    file_id = request.POST.get('file_id')
    print(user_id, file_id)
    ip = request.POST.get('ip')
    port = request.POST.get('port')
    if user_entry.objects.filter(file_id=file_id).exists():
        return JsonResponse({'status': 'file already opened'})

    user_entry(user_id=user_id, file_id=file_id, ip=ip, port=port).save()
    connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.exchange_declare(exchange=str(file_id), exchange_type='fanout')
    connection.close()
    return JsonResponse({'status': 'success'})

@csrf_exempt
def open(request):
    if request.method != 'GET':
        return JsonResponse({'status': 'please send a get request'})

    file_id = request.GET.get('file_id')
    print(file_id)
    try:
        max_id = user_entry.objects.filter(file_id=file_id).order_by('-id')[0].id
        random_id = random.randint(1, max_id + 1)
        obj = user_entry.objects.filter(file_id=file_id).filter(id__gte=random_id)[0]
        return JsonResponse({'user_id': obj.user_id, 'ip':obj.ip, 'port':obj.port, 'time':obj.time})

    except ObjectDoesNotExist:
        return JsonResponse({'status': 'file is not open'})

@csrf_exempt
def opened(request):
    if request.method != 'POST':
        return JsonResponse({'status': 'please send a post request'})
    user_id = request.POST.get('user_id')
    file_id = request.POST.get('file_id')
    ip = request.POST.get('ip')
    port = request.POST.get('port')
    user_entry(user_id=user_id, file_id=file_id, ip=ip, port=port).save()
    return JsonResponse({'status': 'success'})

@csrf_exempt
def close(request):
    if request.method != 'POST':
        return JsonResponse({'status': 'please send a post request'})
    user_id = request.POST.get('user_id')
    file_id = request.POST.get('file_id')
    ip = request.POST.get('ip')
    port = request.POST.get('port')
    
    user_entry.objects.filter(user_id=user_id, file_id=file_id,ip=ip,port=port).delete()
    return JsonResponse({'status': 'success'})

