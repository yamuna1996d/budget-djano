from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse #header files
#from .forms import NewUserForm
# from django.contrib.auth import UserForm
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,authenticate
# Create your views here.
def indexpage(request):             #function
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('family/')
            else:
                messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    
    return render(request,'index.html',context={"form":form})
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            login(request, user)
            return redirect("djan:index")

        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])
            return render(request = request,
                          template_name = "register.html",
                          context={"form":form})

    form = UserCreationForm
 
    return render(request,'register.html',context={"form":form}) 
    # if form.is_valid():
    #         form.save()
    #         username = form.cleaned_data.get('username')
    #         raw_password = form.cleaned_data.get('password1')
    #         user = authenticate(username=username, password=raw_password)
    #         login(request, user)
    #         return redirect('main:index')
    # else:
    #     form = UserCreationForm()
     
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
# def UserForm(request):
#      form=UserForm()
#      return render(request,'login.html',{'form':form})