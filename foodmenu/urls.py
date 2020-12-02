from django.urls import path

from foodmenu import views

urlpatterns = [
    path('setmenu/', views.setmenu, name='setmenu'),
    path('viewfoodmenu/<int:no>', views.viewmenu, name='viewmenu'),

]