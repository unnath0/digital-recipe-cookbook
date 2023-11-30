from django.shortcuts import render,redirect
from django.http import HttpResponse
# import the mysql connector library

# establish mysql connection

# Create your views here.

def home(request):
    return render(request,'index.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('fname')
        email = request.POST.get('email')
        print(username)
        print(email)

        # concatenate fname and lname into name

        # create a database if it doesn't exist already using a if block

        # mysql query execution using another function which will insert the values into the mysql database

        return redirect('home')
    
    return render(request, 'signup.html')