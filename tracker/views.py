from django.shortcuts import render
from .models import Company,Employee,Device,DeviceLog
from .forms import RegistrationForm, LoginForm,CreateEmployeeForm
from django.http import HttpResponseRedirect
# Create your views here.

def registration(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            try:
                form.save()
            except:
                print("cant save!")    

    else:
        form = RegistrationForm()


    return render(request,"tracker/registration.html",{
        "form": form
    })    


def login(request):
    error = ""
    if request.method == "POST":
        form = LoginForm(request.POST)
        
        if form.is_valid():
            try:
                data = form.cleaned_data
                if Company.objects.filter(name = data["company_name"],password = data["password"]).exists():
                    return HttpResponseRedirect("/")
                else:
                    error = "Wrong User Name Or Password !"
            except:
                print("cant login!")    

            
            

    else:
        form = LoginForm()


    return render(request,"tracker/login.html",{
        "form": form,
        "error": error
    }) 
  
def index(request):
     employee_list = Employee.objects.all()
     return render(request,"tracker/index.html",{
        "employee_list": employee_list,
    }) 
  
def create_employee(request):
    if request.method == "POST":
        form = CreateEmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
            except:
                print("cant save!")    

    else:
        form = CreateEmployeeForm()


    return render(request,"tracker/registration.html",{
        "form": form
    })    