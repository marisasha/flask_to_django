from django.shortcuts import render
import json

def home(request):
    return render(request,'home.html',context={})

def autarization(request):
    return render(request,'log_in.html',context={})


def product(request):
    with open("static/product.json") as file:
        product_objects_json : dict = json.load(file)
        product_objects = product_objects_json["data"]
    return render(
                request,
                'product.html',
                context={
                    "product_objects":product_objects
                    }
                    )

def product_info(request,product_id):
    with open("static/product.json") as file:
        product_objects_json : dict = json.load(file)
        product_objects = product_objects_json["data"]
        product_objects_need = product_objects[product_id]
    return render(
                            request,
                            'product_info.html',
                            context={"product_objects_need":product_objects_need},
                            )