from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from resumes.models import Resume
from jobs.models import  Job
from .utils import keyword_match_score

class ResumeJobMatchAPIView(APIView):
    permission_classes=[IsAuthenticated]

    def get(self,request):
        resume=Resume.objects.filter(candidate=request.user).first()

        if not resume or not resume.extracted_text:
            return Response({"error":"Resume text not found"},status=400)
        
        results=[]

        for job in Job.objects.all():
            score=keyword_match_score(
                resume.extracted_text,
                job.description
            )

            results.append({
                "job_id":job.id,
                "title":job.title,
                "match_score":score
            })

        results.sort(key=lambda x:x["match_score"],reverse=True)

        return Response(results)
