from django.urls import path
from . import views
urlpatterns = [
    path("",views.vlog,name="vlog"),
    path("blogpost/<int:myid>",views.vlogpost,name="vlogpost"),
]