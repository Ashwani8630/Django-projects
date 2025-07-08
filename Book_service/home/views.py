from django.shortcuts import render ,redirect
from django.contrib.auth.models import User
from home.models import Contact
from datetime import datetime
import requests
from django.contrib import messages
from django.contrib.auth import logout ,login
from django.contrib.auth import authenticate
from .models import Search  # Replace with your actual model
from django.db.models import Q
# Create your views here.

def index(request):
    context={
        'variable':"variable sent",
        'variable2':"Hey dude "
    }
    return render(request,"Index.html",context)
    # return render(request,"Index.html")
    # return HttpResponse("This is home page.")

def service(request):
    return render(request,"service.html")
    # return HttpResponse("This is a service page.")

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        mail = request.POST.get("email")
        phone = request.POST.get("phone")
        desc = request.POST.get("message")
        
        contact_instance = Contact(
            name=name,
            mail=mail,
            phone=phone,
            desc=desc,
            date=datetime.now()
        )
        contact_instance.save()
        messages.success(request, "Your request has been set!")
        return redirect("home") # redirect the home page.
    
    return render(request, "contact.html")
    # return HttpResponse("This is contact page.")
def __str__(self):
    return self.name

def about(request):
    return render(request,"about.html")
    # return HttpResponse("This about us.")

def chemistry(request):
    return render(request,"chemistry.html")
def math(request):
    return render(request,"math.html")
def literature(request):
    return render(request,"literature.html")
def physics(request):
    return render(request,"physics.html")

# Show the login page 
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)  # This was missing!
            messages.success(request,"Login succesfull")
            return redirect('/')
        else:
            messages.error(request,"Invalid user or password.")
            messages.error(request,"Please sign up ")
            return redirect('signup')
    return render(request, 'login.html')

def signup_view(request):
    if request.method=='POST':
        username=request.POST.get("username")
        email=request.POST.get("email")
        password1=request.POST.get("password1")
        password2=request.POST.get("password2")

        if password1 !=password2:
            messages.error(request,'Password do not match.')
            return redirect('signup')
        
        if User.objects.filter(username=username).exists():
            messages.error(request,"User already exists.")
            return redirect('signup')
        
        user=User.objects.create_user(username=username, email=email,password=password1)
        user.save() #save the user in the jango database
        messages.success(request,"Account created succesfully. Please login.")
        return redirect('login')
    
    return render(request,'signup.html')

def logout_view(request):
    logout(request)
    return render(request,'index.html')

# to search the content from the web


def search_view(request):
    query = request.GET.get('q')
    print("DEBUG: search_view called with q =", query)  # Add this line 
    results = []
    if query:
        results = Search.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        )
        print("DEBUG: results count =", results.count())

    return render(request, 'search_results.html', {'query': query, 'results': results})






