from django.conf.urls import url
from rest_framework import routers
from .views import EventViewSet,index

router = routers.DefaultRouter()
router.register(r'event', EventViewSet)
urlpatterns = [
    url(r'$',index, name='index'),
]
