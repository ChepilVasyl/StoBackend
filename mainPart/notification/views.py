from rest_framework.views import APIView
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
import json
from .models import Notification
from .utils import Pagination

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
        #Витягую номер сторінки яку треба видати
        numberOfPage = int(request.GET.get('page',1))
        print('___Який номер сторінки',numberOfPage)
        # Витягую кількість елементів які мають бути на сторінці
        sizeOnPage = int(request.GET.get('size', 10))
        print('___Розмір сторінки', sizeOnPage)
        #Обчислюємо скільки сторінок треба пропустити
        skipCount = (numberOfPage-1)*sizeOnPage
        print('___К-сть елементів які треба пропустити', skipCount)
        sortingDirection = request.GET.get('sortD', 'asc')
        print('Напрямок сортування', sortingDirection)
        sortingField = request.GET.get('sortF')
        if(sortingDirection=='desc'):
            sortingField = '-'+sortingField
        print('Поле сортування', sortingField)
        data = Notification.objects.all().order_by(sortingField).values()[skipCount:skipCount+sizeOnPage]

        #Треба передати кількість сторінок на клієнта
        countItem = Notification.objects.count()
        countPage = int((countItem+sizeOnPage-1)/sizeOnPage)

        item = Pagination(data,numberOfPage,sizeOnPage,countPage,countItem,sortingField)
        response = item.ReturnData()
        return JsonResponse(response, safe=False)
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
        try:
            rez = json.loads(request.body)
            id_loc = rez.get('id') #Витягнути id старого значення
            newValue = rez.get('newValue') #Витягнути нове значення
            print('___Нове значення =',newValue)
            objFromDb = get_object_or_404(Notification,id=id_loc)
            objFromDb.message = newValue
            objFromDb.save()
            return JsonResponse({'success': 204,'message':'Оновлено'})
        except Exception:
            return JsonResponse({'success':404,'message':'Не вдалося оновити'})


