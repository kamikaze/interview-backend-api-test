from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from app.views import EventViewSet

router = DefaultRouter()
router.register(r'events', EventViewSet, basename='event')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('users/<int:user_id>/events/', EventViewSet.as_view({'get': 'get_events_by_user_id'}), name='user-events'),
    path('repos/<int:repo_id>/events/', EventViewSet.as_view({'get': 'get_events_by_repo_id'}), name='repo-events'),
]
