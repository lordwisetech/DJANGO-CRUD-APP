from django.urls import path

from . import views
from .models import data
from .views import showdata

urlpatterns = [

    path('', showdata.as_view(), name="showdataurl"),
    path('add', views.hello, name="adddataurl"),
    path('delete/<int:pk>', views.delete, name="deleteurl"),
    path('update/<int:pk>', views.update,name="updateurl")

]
