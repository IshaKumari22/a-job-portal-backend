import faiss
import numpy as np

class JobVectorStore:
    def __init__(self,dim):
        self.index=faiss.IndexFlatL2(dim)
        self.job_ids=[]

    def add(self,embeddings,job_ids):
        vectors=np.array((embeddings).astype("float32"))
        self.index.add(vectors)
        self.job_ids.extend(job_ids)

    def search(self,query_embedding,top_k=5):
        query=np.array([query_embedding]).astype("float32")
        distances,indices=self.index.search(query,top_k)

        results=[]
        for idx in indices[0]:
            if idx<len(self.job_ids):
                results.append(self.job_ids[idx])
        return results