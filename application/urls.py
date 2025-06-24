from django.urls import path
from .views import ApplicationCreateAPIView
from .views import check_new_application

urlpatterns = [
    path('api/apply/', ApplicationCreateAPIView.as_view(), name='apply'),
    path('admin/check-new-application/', check_new_application),
]
