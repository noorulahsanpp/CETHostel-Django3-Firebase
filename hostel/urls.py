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
    path('absentees/', views.absentees, name='viewabsentees'),
    path('test/', views.test, name='test'),
    path('calendar/', views.calendar, name='calendar'),
    path('contacts/', views.contacts, name='contacts'),
    path('contactus/', views.contactus, name='contactus'),
    path('invoice/', views.invoice, name='invoice'),
    path('invoiceprint/', views.invoiceprint, name='invoiceprint'),
    path('mailcompose/', views.mailcompose, name='mailcompose'),
    path('mailbox/', views.mailbox, name='mailbox'),
    path('mailread/', views.mailread, name='mailread'),
    path('viewnotification/', views.viewnotification, name='viewnotification'),
    path('allinmates/', views.allinmates, name='allinmates'),
]