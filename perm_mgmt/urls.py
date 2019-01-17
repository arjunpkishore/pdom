from django.conf.urls import url, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^', include(router.urls)),
    url(r'^add-api', views.add_api, name='add_api'),
    url(r'^request-access', views.request_access, name='request_access'),
    url(r'^add-resource', views.add_target, name='add_target'),
    url(r'^request-received', views.req_received, name='req_received'),
]
