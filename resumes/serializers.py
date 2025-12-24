from rest_framework import serializers
from .models import Resume


class ResumeSerializer(serializers.ModelSerializer):
    resume_file = serializers.FileField()

    class Meta:
        model = Resume
        fields = ['id', 'resume_file', 'uploaded_at']
