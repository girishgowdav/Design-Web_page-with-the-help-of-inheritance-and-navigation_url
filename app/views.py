from django.shortcuts import render

# Create your views here.
def Home(request):
    return render(request,'Home.html')
def Registration(request):
    return render(request,'Registration.html')
def Login(request):
    return render(request,'Login.html')        
    
def dummy(request):
    return render(request,'dummy.html')        