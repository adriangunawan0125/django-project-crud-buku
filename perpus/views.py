from django.shortcuts import render
from django.http import HttpResponse

def index(request):
   return HttpResponse("index Aplikasi Buku")

# Create your views here.
