from django.urls import path
from .views import studlist, studcreate, studupdate, studdelete


# from .views import ListAPI

urlpatterns = [
    
    path('studlist', studlist.as_view()),
    path('studcreate', studcreate.as_view()),
    path('studupdate/<int:pk>/' , studupdate.as_view()),
    path('studdelete/<int:pk>/', studdelete.as_view())


]