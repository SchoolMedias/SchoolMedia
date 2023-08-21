from django.urls import path
from . import views 

urlpatterns = [
    path('rooms',views.rooms),
    path('room/<int:roomid>',views.room),
    path('managers/<int:roomid>',views.managers),
    path('manager/add',views.addmanager),
    path('manager/<int:mid>',views.manager),
    path('prohibits/<int:roomid>',views.prohibits),
    path('prohibit/add',views.addprohibit),
    path('prohibit/<int:pid>',views.prohibit)
]