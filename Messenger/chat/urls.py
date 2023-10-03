from django.urls import path
from . import views


urlpatterns = [
  path('', views.index, name='index'),
  path('<str:room_name>/', views.room, name='room'),
  path('room/<str:room_name>/', views.chat_room, name='chat_room'),
  path('room/<str:room_name>/options/', views.chat_room_edit, name='room_options'),
  path('<str:room_name>/options/', views.chat_room_edit, name='room_options'),
  ]
