from django.urls import path
from .views import ResumeUploadAPIView
urlpatterns=[
    path('',ResumeUploadAPIView.as_view(),name='resume-upload')
]