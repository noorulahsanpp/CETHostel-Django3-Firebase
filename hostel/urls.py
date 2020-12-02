from django.urls import path

from hostel import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('adminSignup/', views.adminSignup, name='adminSignup'),
    path('', views.landingPage, name='index'),
    path('LHHome/', views.LHHome, name='LHHome'),
    path('MHHome/', views.MHHome, name='MHHome'),
    path('adminLogin/', views.adminLogin, name='adminLogin'),
    path('adminHome/', views.adminHome, name='adminHome'),
    path('logout/', views.logoutAdmin, name='logoutAdmin'),
    path('registration/', views.studentregistration, name='studentregistration'),
    path('viewallstudents/', views.viewallstudents, name='viewallstudents'),
    path('signupMessSec/', views.signupMessSec, name='signupMessSec'),
    path('loginMessSec/', views.loginMessSec, name='loginMessSec'),
    path('sendNotification/', views.sendNotification, name='sendNotification'),

]