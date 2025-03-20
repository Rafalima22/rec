from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(resquest):
    context={'nome':'Rafael','idade':'27'}
    return render(resquest, 'recipes/pages/home.html',context)