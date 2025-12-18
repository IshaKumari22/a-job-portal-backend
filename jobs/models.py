from django.db import models
from accounts.models import User

class Job(models.Model):
        recruiter=models.ForeignKey(
                User,
                on_delete=models.CASCADE,
                limit_choices_to={'role':'RECRUITER'}
        )
        title=models.CharField(max_length=200)
        description=models.TextField()
        skills=models.TextField(help_text="Comma-separated skills")
        location=models.CharField(max_length=100)
        experience_required=models.IntegerField(help_text="Years of experience")
        created_at=models.DateTimeField(auto_now_add=True)


        def __str__(self):
                return self.title


