from django.urls import path
from . import views


urlpatterns = [
    path("",views.index,name="index-page"),
    path("create/",views.registration, name="account-registration-page"),
    path("login/",views.login, name="login-page"),
    path("create_emp/",views.create_employee, name="create-emp-page"),
    path("create_device/",views.create_device, name="create-device-page"),

]