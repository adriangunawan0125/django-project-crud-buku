from django.http import HttpResponse
from django.shortcuts import render

def index(request):
   context = {
      'title' : 'daftar buku',
      'all_buku' : [
         [
            'belajar pemrograman python',
            2015
         ],
         [
            'HTML untuk pemula',
            2014
         ],
         [
            'Membuat aplikasi dengan framework Django',
            2020,
         ]
      ]
   }
   return render(request, 'index.html',context)