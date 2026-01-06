from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from .models import User


class UserListAPIView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        users = User.objects.all().values(
            "id", "username", "email", "role"
        )
        return Response(users)
