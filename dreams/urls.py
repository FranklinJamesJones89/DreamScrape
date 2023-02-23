from django.urls import path

from . import views

app_name = 'dreams'
urlpatterns = [
    path('', views.home, name = 'home'),
    path('room/<str:pk>', views.room, name = 'room')
]
