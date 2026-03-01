import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load job description
with open("data/job_description.txt", "r", encoding="utf-8") as file:
    job_description = file.read()

# Load resumes
resumes = []
resume_names = []

resume_folder = "data/resumes"

for filename in os.listdir(resume_folder):
    if filename.endswith(".txt"):
        with open(os.path.join(resume_folder, filename), "r", encoding="utf-8") as file:
            resumes.append(file.read())
            resume_names.append(filename)

# Combine job description and resumes
documents = [job_description] + resumes

# Convert text to vectors
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(documents)

# Compute similarity
similarity_scores = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:]).flatten()

# Show results
print("\nResume Ranking Based on Similarity:\n")

for name, score in sorted(zip(resume_names, similarity_scores), key=lambda x: x[1], reverse=True):
    print(f"{name} → Match Score: {round(score * 100, 2)}%")