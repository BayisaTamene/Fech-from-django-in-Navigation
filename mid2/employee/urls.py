from django.urls import path
from .views import emplist, empcreate, empupdate, empdelete


# from .views import ListAPI

urlpatterns = [
    
    path('emplist', emplist.as_view()),
    path('empcreate', empcreate.as_view()),
    path('empupdate/<int:pk>/' , empupdate.as_view()),
    path('empdelete/<int:pk>/', empdelete.as_view())


]