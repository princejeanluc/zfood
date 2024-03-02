import json
import os

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from .libs import auth
from .models import Client, Store, Product
from zfoodapi.forms import SaveFile
@csrf_exempt
@require_POST
def signup_view(request):
    print("------------1")
    if request.content_type == 'multipart/form-data':
        data = request.POST
        print("------------1")
        form = SaveFile(request.POST, request.FILES)
        if form.is_valid():
                client = Client(
                    first_name=data['first_name'],
                    last_name=data['last_name'],
                    email=data['email'],
                    phone=data['phone'],
                    country=data['country'],
                    city=data['city'],
                    delegation=data['delegation'],
                    password=data['password'],
                )
                photo = form.cleaned_data['file']
                path = os.path.join("./zfoodapi/static/", photo.name)
                with open(path, 'wb+') as f:
                    for chunk in photo.chunks():
                        f.write(chunk)
                client.photo = path
                client.save()
                return JsonResponse({"message": "inscription success"})
    return JsonResponse({"message": "inscription failed"})


@csrf_exempt
@require_POST
def auth_view(request):
    if request.content_type == 'application/x-www-form-urlencoded':
        data = request.POST.dict()
        print(data)
        if auth(data):
            return JsonResponse({"message": "auth success"})
    return JsonResponse({"message": "auth failed"})


@csrf_exempt
@require_POST
def getUserDetails(request):
    if request.content_type == 'application/x-www-form-urlencoded':
        if auth(request.POST.dict()):
            user = Client.objects.get(email=request.POST.dict()["email"])

            return JsonResponse(
                {
                    "first_name": user.first_name,
                    "last_name":user.last_name,
                    "email":user.email,
                    "phone":user.phone,
                    "file":user.photo.name,
                    "country":user.country,
                    "city":user.city,
                    "delegation":user.delegation,
                    "occupation":user.occupation
                }
            )
        return JsonResponse({"message": "failed to get User details"})



@csrf_exempt
@require_POST
def getAllStore(request):
    stores = Store.objects.all().values()
    stores = list(stores)
    return JsonResponse(stores, safe=False)


@csrf_exempt
@require_POST
def getAllProduct(request):
    try:
        products = Product.objects.all().values()
        products = list(products)
        return JsonResponse(products, safe=False)
    except Product.DoesNotExist:
        return JsonResponse([{"message": "Product"}])


@csrf_exempt
@require_POST
def getProductFromStore(request,store_id:int):
    try:
        store = Store.objects.all().get(id=store_id)
        store_products = Product.objects.filter(store=store).values()
        store_products = list(store_products)
        return JsonResponse(store_products, safe=False)
    except Store.DoesNotExist:
        return JsonResponse([{"message":"store not found"}], safe=False)




