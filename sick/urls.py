from django.urls import path

from sick import views

urlpatterns = [
    path('viewsick/', views.viewsick, name='viewsick'),

]