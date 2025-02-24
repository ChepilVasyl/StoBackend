from rest_framework.views import APIView
from django.http import JsonResponse
from django.shortcuts import render
import json
from .models import Notification

class Main(APIView):
    def post(self,request):
        data = json.loads(request.body)
        dataMessage = data.get('text')
        print('dataMessage =',dataMessage)
        addElement = Notification(message=dataMessage)
        addElement.save()
        print('Відпрацював post notification, data =',data)
        return JsonResponse({'status':201, 'message': True})
    def get(self,request):
        print('Зайшло в метод get')
        data = Notification.objects.all().values()
        data = list(data)
        print('data =',data)
        return JsonResponse(data, safe=False)
    def delete(self,request):
        print('Зайшло в метод delete')
        try:
            getFromBody = json.loads(request.body)
            getId = getFromBody.get('id')
            print("getId = ",getId)
            deleted = Notification.objects.get(id=getId)
            deleted.delete()
            return JsonResponse({'success': 204, 'message': True})
        except Notification.DoesNotExist:
            return JsonResponse({'success': 404, 'message': False})

    def put(self,request):
        print('Зайшло в метод put')

        return JsonResponse({'success':204,'message':'Оновлено'})

