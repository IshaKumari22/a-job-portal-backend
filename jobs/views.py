from rest_framework import generics,permissions
from .models import Job
from .serializers import JobSerializer
from .permissions import IsRecruiter
class JobListCreateAPIView(generics.ListCreateAPIView):
    queryset=Job.objects.all()
    serializer_class=JobSerializer

    def get_permissions(self):
        if self.request.method=='POST':
            return [IsRecruiter()]
        return [permissions.AllowAny()]
    def perform_create(self, serializer):
        serializer.save(recruiter=self.request.user)