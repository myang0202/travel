from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name = 'my_index'),
    url(r'^user/create$', views.create, name = "my_create"),
    url(r'^travels$', views.login, name = 'my_home'),
    url(r'^travels/add$',views.addtravel,name = "my_travel"),
    url(r'^travels/submit/$',views.submittravel, name = "my_submit"),
    url(r'^travels/destination/(?P<id>\d+)$',views.destination, name = "my_destination"),
    url(r'^travels/join/(?P<id>\d+)$',views.join, name = "my_join"),
    url(r'^logout$',views.logout, name = "my_logout"),
    

]
