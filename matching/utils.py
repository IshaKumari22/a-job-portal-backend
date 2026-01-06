import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
# def clean_text(text):
#     text=text.lower()
#     text=re.sub(r"[^a-z0-9\s]","",text)
#     return set(text.split())

# def keyword_match_score(resume_text,job_text):
#     resume_words=clean_text(resume_text)
#     job_words=clean_text(job_text)
#     if not resume_words or not job_words:
#         return 0
#     matched=resume_words.intersection(job_words)
#     score=(len(matched)/len(job_words))*100
#     return round(score,2)

def tfidf_match_score(resume_text,job_text):
    if not resume_text or not job_text:
        return 0
    
    documents=[
        resume_text,
        job_text
    ]
    vectorizer=TfidfVectorizer(stop_words="english")
    tfidf_matrix=vectorizer.fit_transform(documents)

    similarity=cosine_similarity(tfidf_matrix[0:1],tfidf_matrix[1:2])[0][0]

    return round(similarity*100,2)


from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

embdding_model=SentenceTransformer("all-MiniLM-L6-v2")

def embedding_match_score(resume_text,job_text):
    if not resume_text or not job_text:
        return 0
    
    embeddings=embdding_model.encode(
        [resume_text,job_text],
        convert_to_tensor=False
    )
    similarity=cosine_similarity(
        [embeddings[0]],
        [embeddings[1]]
    )[0][0]

    return round(similarity*100,2)

