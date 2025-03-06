from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.urls import path

app_name="musicPlayerApp"
urlpatterns=[
    path("",views.index,name='index'),
]