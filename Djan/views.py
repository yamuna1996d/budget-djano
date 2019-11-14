from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse #header files
#from .forms import NewUserForm
# from django.contrib.auth import UserForm
from django.contrib.auth.forms import AuthenticationForm
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
        # create a form instance and populate it with data from the request:
        form = RegisterForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            if User.objects.filter(username=form.cleaned_data['username']).exists():
                return render(request, template, {
                    'form': form,
                    'error_message': 'Username already exists.'
                })
            
            elif form.cleaned_data['password'] != form.cleaned_data['password_repeat']:
                return render(request, template, {
                    'form': form,
                    'error_message': 'Passwords do not match.'
                })
            else:
                # Create the user:
                user = User.objects.create_user(
                    form.cleaned_data['username'],
                    form.cleaned_data['password']
                )
                user.first_name = form.cleaned_data['first_name']
                user.last_name = form.cleaned_data['last_name']
                user.phone_number = form.cleaned_data['phone_number']
                user.save()
               
                # Login the user
                login(request, user)
               
                # redirect to accounts page:
                return redirect("djan:index")
    # if request.method =="POST":
    #    form =UserCreateForm(request.POST)
    #    if form.is_valid():
    #        user = form.save()
    #        username = form.cleaned_data.get('username')
    #        login(request, user)
    #        return redirect("djan:index")
    #     # else:
    #     #     for messages in form.error_messages:
    #     #         print(form.error_messages[messages])
    
    # form = UserCreateForm
    return render(request,'register.html') 
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