from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request,'index.html')

def signup(request):
    # print(request.GET)
    print(request.GET['your_name'])
    print(request.GET['your_email'])
    return render(request, 'signup.html')