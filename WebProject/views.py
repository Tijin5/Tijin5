from django.shortcuts import render

# Create your views here.
def home(request):
     context = {'message':'Success'}
     return render(request, 'index.html', context)     
    
def   contact(request):
      context = {'info':'hello bro'}
      return render(request,'contact.html',context)