# match_score.py
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load once at module level
model = SentenceTransformer('all-MiniLM-L6-v2')

def get_match_score(resume_text, job_desc):
    # Semantic embedding-based match score
    embeddings = model.encode([resume_text, job_desc])
    score = cosine_similarity([embeddings[0]], [embeddings[1]])[0][0]
    return score * 100
