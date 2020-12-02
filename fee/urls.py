from django.urls import path

from fee import views
urlpatterns = [
    path('', views.feehome, name = 'feehome'),
    path('postfee/', views.postfee, name = 'postfee'),
    path('viewfee/', views.viewfee, name='viewfee'),

]