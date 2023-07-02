from django.urls import path
from . import views




urlpatterns = [
    path('DataTest/',views.DataTest.as_view()),
    path('Search/',views.Search.as_view()),
    path('addtest/',views.add_book),
]