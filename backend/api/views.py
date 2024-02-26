from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
# def api_home(request):
#     print("from api home",request.body)
#     return JsonResponse({"message":"Hello mr swapno"})
# get random porduct
from products.models import Product
from django.forms.models import model_to_dict
def api_home(request):
    model_data = Product.objects.all().order_by("?").first()
    data= {}
    if model_data:
        # data['id'] = model_data.id
        # data['title'] = model_data.title
        # data['content'] = model_data.content
        # data['price'] = model_data.price
        
        #this can be dobe in one line
        data = model_to_dict(model_data, fields=['id','title'])

    return JsonResponse(data)