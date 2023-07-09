from django.urls import path
from . import views


urlpatterns = [
    path("",views.index,name="index-page"),
    path("create/",views.registration, name="account-registration-page"),
    path("login/",views.login, name="login-page"),
    path("create_emp/",views.create_employee, name="create-emp-page"),
    path("create_device/",views.create_device, name="create-device-page"),
    path("allocate_device/",views.allocate_device, name="allocate-device-page"),
    path("search_device/",views.search_device, name="search-device-page"),
    path("deallocate_device/<slug:slug>",views.deallocate_device, name="deallocate-device-page"),
   

]