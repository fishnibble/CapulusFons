from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^bluebottlecoffee', views.bluebottlecoffee, name='bluebottlecoffee'),
]