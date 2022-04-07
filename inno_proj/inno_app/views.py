from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from inno_app.forms import UploadForm

def index(request):
    return render(request, 'inno_app/index.html')

def contact(request):
        return render(request,'inno_app/contact.html')
def display(request):
    return render(request, 'inno_app/display.html')
def article1(request):
    return render(request,'inno_app/article1.html')

def story(request):
    return render(request,'inno_app/story.html')

def info(request):
    return render(request,'inno_app/info.html')
def article2(request):
    return render(request,'inno_app/article2.html')
def article3(request):
    return render(request,'inno_app/article3.html')
def article4(request):
    return render(request,'inno_app/article4.html')
def article5(request):
    return render(request,'inno_app/article5.html')
def upload(request):
    form = UploadForm()
    if request.method=='POST':
        form = UploadForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return story(request)
        else:
            print('Invalid!')



    return render(request,'inno_app/upload.html',{'form':form})


def storypage(request):
    return render(request,'inno_app/storypage.html')
def videopage(request):
    return render(request,'inno_app/videopage.html')
