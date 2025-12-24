from django.urls import path
from .views import JobListCreateAPIView,JobRetriveUpdateDeleteAPIView

urlpatterns=[
    path('',JobListCreateAPIView.as_view(),name='job-list-create'),
    path('<int:pk>/',JobRetriveUpdateDeleteAPIView.as_view(),name='job-detail'),
]