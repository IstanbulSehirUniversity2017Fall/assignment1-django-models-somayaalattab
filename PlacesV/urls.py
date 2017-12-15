from django.conf.urls import url
from PlacesV import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<country_id>[0-9]+)/$', views.country_order, name='country')
]