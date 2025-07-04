## Resume–Job Match Scorer

A simple AI-powered web app that scores how well your resume matches a job description using NLP (TF-IDF + cosine similarity).

## Features
- Upload resume (PDF/DOCX/TXT)
- Paste job description
- Get a match score (0–100%) with suggestions

## Built With
- Python
- Streamlit
- scikit-learn
- PyPDF2 + docx2txt

## Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
