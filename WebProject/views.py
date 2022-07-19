from django.shortcuts import render
from .forms import InputForm, TitleProfileForm
from .models import TitleProfile 
# Create your views here.
def home(request):
     context = {'message':'Success'}
     return render(request, 'index.html', context)     
    
def profile(request):
      if request.method=='GET':
            context = { 'message': 'Success'}
            context['titleform']=TitleProfileForm()
            print(context)
            return render(request,'profile.html',context)

def updateProfile(request):
      if request.method=='GET':
            context = { 'message': 'Success'}
            formdata = TitleProfile.objects.get(pk=1)
            context['titleform']=TitleProfileForm(instance=formdata)
            print(context)
            return render(request,'profile-edit.html',context)
      elif request.method=='POST':
            print('request.POST',request.POST) 
            newForm= TitleProfileForm(request.POST)
            if newForm.is_valid():
                  context={ 'message':'Success'}
                  newForm.save()
            formdata = TitleProfile.objects.get(pk=1)
            context['titleform']=TitleProfileForm(instance=formdata)
            print(context)
            return render(request,'profile-edit.html',context)

def   contact(request):
      context = {'info':'hello bro'}
      return render(request,'contact.html',context)
      
def   hello(request):
      context = {'mess':'yooo'}
      return render(request,'hello.html',context)


 
# Create your views here.
def home_view(request):
    context ={}
    context['form']= InputForm()
    return render(request, "home.html", context)    

