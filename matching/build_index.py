from jobs.models import Job
from sentence_transformers import SentenceTransformer
from .vector_store import JobVectorStore

model=SentenceTransformer("all-MiniLM-L6-v2")

def build_job_index():
    jobs=Job.objects.all()
    if not jobs.exists():
        return None
    texts=[job.description for job in jobs]
    ids=[job.id for job in jobs]

    embeddings=model.encode(texts)
    store=JobVectorStore(dim=len(embeddings[0]))
    store.add(embeddings,ids)

    return store
