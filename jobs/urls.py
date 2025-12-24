from django.urls import path
from .views import JobListCreateAPIView

urlpatterns=[
    path('',JobListCreateAPIView.as_view(),name='job-list-create'),
]