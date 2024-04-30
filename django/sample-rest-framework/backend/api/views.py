# from django.shortcuts import render
from django.http import JsonResponse
import json
from products.models import Product
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.serializers import ProductSerializer

# def api_home(request, *args, **kwargs):
#     bdy = request.body
#     data = {}
#     try:
#         data = json.loads(bdy)
#     except:
#         pass
#     # print(request.headers)

#     # data['headers'] = dict(request.headers)
#     # data['content_type'] = request.content_type
#     # print(data.keys())
#     # return JsonResponse({"message":"Hello there, how are you"})
#     # print(request.GET)
#     # print(request.POST)
#     data['params'] = dict(request.GET)
#     print(data)

#     return JsonResponse(data)

@api_view(['GET'])
def api_home(request, *args, **kwargs):
    instance = Product.objects.all().order_by('?').first()
    info = {}
    # print(instance)
    if instance:
        info = ProductSerializer(instance).data
        # info = model_to_dict(instance, fields='id')
        # info['title'] = instance.title
        # info['content'] = instance.content
        # info['price'] = instance.price
    return Response(info)