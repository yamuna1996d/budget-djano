from django.shortcuts import render
from django.http import HttpResponse #header files
from .forms import FacultyForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# Create your views here.
def indexpage(request):             #function
    return render(request,'index.html')
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request,'login.html',context={"form":form})
    
def family(request):
    return render(request,'home.html')
def income(request):
    return render(request,'home.html')
def expenditure(request):
    return render(request,'home.html')
def liability(request):
    return render(request,'home.html')
def savings(request):
    return render(request,'home.html')
def faculty(request):
     form=FacultyForm()
     return render(request,'faculty.html',{'form':form})