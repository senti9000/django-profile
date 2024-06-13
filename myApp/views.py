from django.shortcuts import render, redirect  
from .forms import RegisterForm

# Create your views here.
def helloWorld (request):
        return render(request,'helloWorld.html')

def testPath (request):
        return render(request,'testPath.html')

def Login_Page(request):
        return render(request, 'Login_Page.html')

def register(request):
        if request.method =='POST':
                form = RegisterForm(request.POST)
                if form.is_valid():
                        form.save()
                        return redirect('Login_Page')
        else:
                form = RegisterForm()
                return render(request, 'register.html'('form',form))