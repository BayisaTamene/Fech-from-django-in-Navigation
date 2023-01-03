from django.urls import path
from .views import teachlist, teachcreate, teachupdate, teachdelete


# from .views import ListAPI

urlpatterns = [
    
    path('teachlist', teachlist.as_view()),
    path('teachcreate', teachcreate.as_view()),
    path('teachupdate/<int:pk>/' , teachupdate.as_view()),
    path('teachdelete/<int:pk>/', teachdelete.as_view())


]