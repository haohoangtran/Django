from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    return render(request,'index.html')
def table(request):
    return render(request,"basic-table.html")