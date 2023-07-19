from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import query_form
import json
from .models import Dish_data
# Create your views here.


def home(request):
    # return HttpResponse("<h1> Home </h1>")
    return render(request,"dish_search_app\home.html")


def search(request):
    if request.method == 'POST':
        data = query_form(request.POST)
        print(f"data: {data}")
        obj = Dish_data.objects.all()
        print(f"obj:{obj}")
        final_data = {}
        if data.is_valid():
            que = data.cleaned_data['query']
            print(f"que:{que}")
            for i in obj:
                temp = {}
                dic_str = (i.items)
                dic_data = json.loads(dic_str)
                for j in dic_data.keys():
                    if que in j:
                        temp[j] = dic_data[j]
                if temp:
                    temp = sorted(temp.items(), key=lambda x: x[1])
                    final_data[i.name] = temp

            return render(request, "dish_search_app\\results.html", {'data': final_data})
        
        # return render(request, 'result.html', {'data': obj})

    else:
        data = query_form()
    return render(request, "dish_search_app/search.html", {'form': data})
