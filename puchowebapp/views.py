from django.shortcuts import render

# Create your views here.

def index(request):
    context={}
    return render(request,'home.html',context)
def what_we_do(request):
    context={}
    return render(request,'what_we_do.html',context)
def about(request):
    context={}
    return render(request,'about.html',context)
def protfolio(request):
    context={}
    return render(request,'protfolio.html',context)
def gallery(request):
    context={}
    return render(request,'gallery.html',context)
def contact(request):
    context={}
    return render(request,'contact_us.html',context)