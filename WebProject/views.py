from django.shortcuts import render

# Create your views here.
def home(request):
     context = {'message':'Success'}
     return render(request, 'index.html', context)     
    
def   contact(request):
      context = {'info':'hello bro'}
      return render(request,'contact.html',context)
      
def   hello(request):
      context = {'mess':'yooo'}
      return render(request,'hello.html',context)





from django.shortcuts import render
from .forms import InputForm
 
# Create your views here.
def home_view(request):
    context ={}
    context['form']= InputForm()
    return render(request, "home.html", context)    

