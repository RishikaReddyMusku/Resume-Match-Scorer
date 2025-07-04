
import streamlit as st
from utils import extract_text
from match_score import get_match_score



st.set_page_config(page_title="Resume Match Scorer", page_icon="🧾", layout="centered")

st.markdown("""
<div class="custom-header">
    <h1 style='text-align: center;'>Resume–Job Match Scorer</h1>
    <p style='text-align: center; font-size: 18px;'>Upload your resume and paste a job description to get an AI-based match score.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("###  Upload Your Resume")
resume_file = st.file_uploader("Supported formats: PDF, DOCX, TXT", type=["pdf", "docx", "txt"])

st.markdown("###  Paste Job Description")
job_desc = st.text_area("Paste the job description here", height=200)

if st.button(" Get Match Score"):
    if not resume_file or not job_desc.strip():
        st.warning("⚠️ Please upload a resume and enter a job description.")
    else:
        with st.spinner("Analyzing..."):
            resume_text = extract_text(resume_file)
            score = get_match_score(resume_text, job_desc)

        rounded_score = round(score, 2)
        st.markdown(f"""
<h3 style='color:#4CAF50;'>
✅ Match Score:
<span style='color:#6fa8dc;'>{rounded_score}%</span>
</h3>
""", unsafe_allow_html=True)

       
        if rounded_score < 40:
            st.error(" Low match. Tailor your resume with more relevant keywords.")
        elif rounded_score < 80:
            st.info(" Fair match. You can still improve your resume.")
        else:
            st.success(" Great match! Your resume fits the job well.")
            st.balloons()

st.markdown("""
<hr style='border: 1px solid #ccc;' />
<div style='text-align: center; font-size: 20px; color: gray;'>
Made with ❤️ using Streamlit
</div>
""", unsafe_allow_html=True)


def add_background():
    st.markdown(
        """
        <style>
        /* Global background and font */
        body, .stApp {
            background-color: #f8fcff;
            font-family: 'Segoe UI', sans-serif;
        }

        /* Centered app container with soft white card look */
        .css-18e3th9 {
            background-color: #ffffffdd !important;
            border-radius: 14px;
            padding: 2rem 2rem 1rem 2rem;
            box-shadow: 0 8px 24px rgba(0,0,0,0.06);
        }

        /* Header styling */
        .custom-header {
            background-color: #e3f2fd;
            border: 1px solid #cfe3f3;
            border-radius: 10px;
            padding: 20px;
            margin-bottom: 20px;
        }

        h1 {
            color: #2c3e50;
            font-size: 32px;
        }

        p {
            color: #5f6f81;
        }

        /* Button and text area tweaks */
        .stButton > button {
            background-color: #4a90e2;
            color: white;
            border-radius: 8px;
            padding: 10px 20px;
            font-weight: 600;
        }

        .stTextArea textarea {
            background-color: #f0f7ff;
            border: 1px solid #d0e3f3;
            border-radius: 8px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
add_background()
def lighten_button():
    st.markdown("""
        <style>
        /* Light pastel blue button */
        .stButton > button {
            background-color: #d0e8ff !important;
            color: #003366 !important;
            border: 1px solid #bcdff7;
            padding: 0.6em 1.4em;
            border-radius: 8px;
            font-weight: 600;
            transition: 0.3s ease-in-out;
        }

        .stButton > button:hover {
            background-color: #e6f2ff !important;
            color: #001f4d !important;
            border-color: #a2d4f5;
        }
        </style>
    """, unsafe_allow_html=True)

lighten_button()
