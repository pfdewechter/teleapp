from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^register_practitioner/$', views.register_practitioner, name='register_practitioner'),
    url(r'^register_consultee/$', views.register_consultee, name='register_consultee'),
]
