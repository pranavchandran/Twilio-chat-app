from django.urls import path
from . import views

app_name = 'chat'

urlpatterns=[
    path('',views.all_rooms,name='all_rooms'),
    path('token',views.token,name='token'),
    path('rooms/<slug>/',views.room_detail,name='room_detail')
]
