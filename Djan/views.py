from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse #header files
from .models import Income,Expenditure
from django.db.models import Sum
from .forms import IncomeForm
from .forms import ExpenditureForm
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
    return render(request,'income.html')

def incomed(request):
    if request.method == "POST":
        form = IncomeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('incomedview/')

    else:
        form = IncomeForm()
    return render(request,'incomedetails.html',{'form':form})

def incomedv(request):
     obj = Income.objects.all()
     
     return render(request,'incomedview.html',{'Incomedetail':obj})
def modincome(request):
     obj = Income.objects.all()
     if request.method == "POST":
        obj = Income.objects.all()
        obj.delete()
        messages.success(request, "Post successfully deleted!")
        return redirect('incomedview/')
    
     return render(request,'modifyincome.html',{'Incomedetail':obj})
def expenditure(request):
    if request.method == "POST":
        form = ExpenditureForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('expendetail/')

    else:
        form = ExpenditureForm()
    return render(request,'expenditure.html',{'form':form})

def deleteincome(request,incomeid):
    Income.objects.filter(incomeid=incomeid).delete()    
    messages.success(request, "Post successfully deleted!")
    return redirect('incomedview/')
    return render(request,'modifyincome.html')

def editincome(request,incomeid):
	try:
		obj = Income.objects.get(incomeid = incomeid)
	except Books.DoesNotExist:
		return redirect('modincome/')
	incomeform = IncomeForm(request.POST or None, instance = obj)
	if incomeform.is_valid():
		incomeform.save()
		return redirect('index')
	return render(request, 'editincome.html', {'form':incomeform})


def expendetail(request):
    obj = Expenditure.objects.all()
    return render(request,'expendetail.html',{'Expendetail':obj})
def exmodify(request):
    return render(request,'exmodify.html')

def savings(request):
    obj = Income.objects.all()
    expd = Expenditure.objects.all()
    findtotalIncome = Income.objects.aggregate(Sum('amount'))
    findtotalIncome=findtotalIncome['amount__sum'];
    findtotalExpenditure=Expenditure.objects.aggregate(Sum('amount'))
    findtotalExpenditure=findtotalExpenditure['amount__sum'];
    findsavings=int(findtotalIncome-findtotalExpenditure)
    newval=str(findsavings)
    print(findsavings)
    return render(request,'savings.html',{'Incomedetail':obj,'totalincome':findtotalIncome,'totalexpence':findtotalExpenditure,'savings':newval,'Expend':expd})
