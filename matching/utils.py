import re

def clean_text(text):
    text=text.lower()
    text=re.sub(r"[^a-z0-9\s]","",text)
    return set(text.split())

def keyword_match_score(resume_text,job_text):
    resume_words=clean_text(resume_text)
    job_words=clean_text(job_text)
    if not resume_words or not job_words:
        return 0
    matched=resume_words.intersection(job_words)
    score=(len(matched)/len(job_words))*100
    return round(score,2)