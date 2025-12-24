from django.db import models
from accounts.models import User

class Resume(models.Model):
    candidate=models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        limit_choices_to={'role':'CANDIDATE'}

    )
    resume_file=models.FileField(upload_to='resumes/')
    uploaded_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.candidate.username}'s Resume"
