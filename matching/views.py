from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from resumes.models import Resume
from jobs.models import  Job

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

from .build_index import build_job_index

model=SentenceTransformer("all-MiniLM-L6-v2")
job_store=build_job_index()

class ResumeJobMatchAPIView(APIView):
    permission_classes=[IsAuthenticated]

    def get(self,request):
        resume=Resume.objects.filter(candidate=request.user).first()

        if not resume or not resume.extracted_text:
            return Response({"error":"Resume text not found"},status=400)
        
        if job_store is None:
            return Response({"error":"No joobs indexed"},status=400)
        
        resume_embedding=model.encode(resume.extracted_text)

        top_job_ids=job_store.search(resume_embedding,top_k=5)

        jobs=Job.objects.filter(id__in=top_job_ids)
        results=[]
        for job in jobs:
            job_embedding=model.encode(job.description)

            score=cosine_similarity(
                [resume_embedding],
                [job_embedding]
            )[0][0]

        

            results.append({
                "job_id":job.id,
                "title":job.title,
                "match_score":round(score*100,2)
            })

        results.sort(key=lambda x:x["match_score"],reverse=True)

        return Response(results)
