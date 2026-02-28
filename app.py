from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load pretrained model (downloads first time only)
model = SentenceTransformer('all-MiniLM-L6-v2')

def calculate_similarity(job_desc, resume_text):
    # Convert texts into embeddings (numbers)
    embeddings = model.encode([job_desc, resume_text])
    
    # Compare similarity
    similarity = cosine_similarity(
        [embeddings[0]], 
        [embeddings[1]]
    )
    
    return round(float(similarity[0][0]) * 100, 2)
