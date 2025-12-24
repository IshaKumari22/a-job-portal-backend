from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Resume
from .serializers import ResumeSerializer
from .permissions import IsCandidate


class ResumeUploadAPIView(APIView):
    permission_classes = [IsCandidate]
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request):
        resume, created = Resume.objects.get_or_create(
            candidate=request.user
        )

        serializer = ResumeSerializer(
            resume,
            data=request.data,
            partial=True
        )

        if not serializer.is_valid():
           
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()

        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED if created else status.HTTP_200_OK
        )
