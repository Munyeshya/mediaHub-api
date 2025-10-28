from django.urls import path, include
from rest_framework import routers
from .views import ServiceOfferingViewSet, BookingViewSet  # we will create later

router = routers.DefaultRouter()
# router.register(r'offerings', ServiceOfferingViewSet)
# router.register(r'bookings', BookingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
