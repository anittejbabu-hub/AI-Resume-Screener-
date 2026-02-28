# 🤖 AI Resume Screener – Machine Learning Project

An intelligent Resume Screening System built using Machine Learning that ranks resumes based on similarity to a given Job Description.

---

## 🚀 Project Overview

Recruiters receive hundreds of resumes for a single job posting.  
This project automates resume screening by calculating similarity scores between resumes and job descriptions using NLP and Machine Learning techniques.

The system ranks resumes based on match percentage.

---

## 🧠 How It Works

1. Takes a Job Description as input
2. Reads multiple resumes
3. Converts text into numerical vectors using TF-IDF
4. Calculates Cosine Similarity
5. Ranks resumes based on match score

---

## 🛠 Technologies Used

- Python
- NumPy
- Pandas
- Scikit-learn
- NLTK
- Flask (optional for web app)
- Matplotlib

---

## 📂 Project Structure

```
AI-Resume-Screener/
│
├── main.py
├── data/
│   └── resumes/
├── templates/
├── static/
├── README.md
```

---

## 📊 Sample Output

```
Resume Ranking Based on Similarity:

resume1.txt → Match Score: 41.44%
resume2.txt → Match Score: 8.14%
```

The resume with the highest percentage is the best match.

---

## 🔍 Features

✔ Automatic Resume Ranking  
✔ NLP-Based Text Processing  
✔ Cosine Similarity Matching  
✔ Easy to Expand  
✔ Beginner Friendly ML Project  

---

## ⚙ Installation

1. Clone the repository

```
git clone https://github.com/yourusername/AI-Resume-Screener.git
```

2. Navigate to project folder

```
cd AI-Resume-Screener
```

3. Create virtual environment

```
python -m venv venv
```

4. Activate virtual environment

Windows:
```
venv\Scripts\Activate
```

5. Install dependencies

```
pip install -r requirements.txt
```

6. Run the project

```
python main.py
```

---

## 🎯 Future Improvements

- Web Interface for uploading resumes
- PDF Resume Support
- Skill Extraction Module
- AI-Based Resume Feedback
- Deployment on Cloud

---

## 📌 Author

Developed as a Machine Learning Mini Project.

---

## ⭐ If you like this project

Give it a star ⭐ on GitHub!
