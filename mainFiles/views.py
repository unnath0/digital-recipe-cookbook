from django.shortcuts import render,redirect
from django.http import HttpResponse
from mainFiles.models import User

# Create your views here.

def home(request):
    return render(request,'index.html')

def signup(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        city = request.POST.get('city')
        state = request.POST.get('state')

        user = User(FirstName=fname, LastName=lname, Email=email, City=city, State=state)
        user.save()

        return redirect('home')
    
    return render(request, 'signup.html')