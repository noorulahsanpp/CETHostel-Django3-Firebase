from django.urls import path

from foodmenu import views

urlpatterns = [
    path('setmenu/', views.setmenu, name='setmenu'),
    path('viewfoodmenu/', views.viewmenu, name='viewmenu'),

]