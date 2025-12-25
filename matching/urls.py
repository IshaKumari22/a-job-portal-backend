from django.urls import path
from .views import ResumeJobMatchAPIView

urlpatterns=[
    path('match/',ResumeJobMatchAPIView.as_view())
]