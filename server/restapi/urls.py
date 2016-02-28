from django.conf.urls import url, include
from rest_framework import routers

from restapi.views import RecordViewSet

#: Defines the default router.
router = routers.DefaultRouter()

#: Register endpoints:
router.register(r"records", RecordViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r"^", include(router.urls)),
    url(r"^api-auth/", include("rest_framework.urls", namespace="rest_framework"))
]
