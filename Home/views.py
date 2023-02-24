from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")
# # Create your views here.


class Index(View):
    def get(self,request,*args, **kwargs):
        return render(request, 'Home/index.html')