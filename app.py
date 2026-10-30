from flask import Flask, render_template, request
from pathlib import Path
import re

app = Flask(__name__)

SKILL_KEYWORDS = [
    "python", "java", "c++", "sql", "excel", "power bi", "tableau",
    "machine learning", "data analysis", "pandas", "numpy", "scikit-learn",
    "html", "css", "javascript", "flask", "django", "communication",
    "teamwork", "problem solving", "leadership", "project management",
    "git", "github", "statistics", "deep learning", "artificial intelligence",
    "data visualization", "opencv", "nlp"
]

def clean_text(value):
    return re.sub(r"\s+", " ", (value or "").strip())

def find_skills(text):
    lower = text.lower()
    return sorted({skill.title() for skill in SKILL_KEYWORDS if skill in lower})

def analyze_resume(resume_text, job_description):
    resume_text = clean_text(resume_text)
    job_description = clean_text(job_description)

    resume_skills = find_skills(resume_text)
    job_skills = find_skills(job_description)
    matched = sorted(set(resume_skills) & set(job_skills))
    missing = sorted(set(job_skills) - set(resume_skills))

    if job_skills:
        score = round(len(matched) / len(set(job_skills)) * 100)
    else:
        score = 0

    tips = []
    if not resume_text:
        tips.append("Paste your resume text so it can be reviewed.")
    if len(resume_text.split()) < 80:
        tips.append("Your resume text looks short. Add relevant education, projects, skills, and achievements if applicable.")
    if not re.search(r"\b(project|projects)\b", resume_text, re.I):
        tips.append("Consider adding a Projects section with what you built and which tools you used.")
    if not re.search(r"\b(education|degree|college|university|school)\b", resume_text, re.I):
        tips.append("Consider adding an Education section.")
    if not re.search(r"\b(experience|internship|volunteer)\b", resume_text, re.I):
        tips.append("If relevant, include internship, work, volunteer, or practical experience.")
    if job_skills and missing:
        tips.append("If you genuinely have these skills, include them clearly: " + ", ".join(missing) + ". Do not claim skills you do not have.")
    if not tips:
        tips.append("Keep bullets specific and truthful. Where possible, describe the action, tool, and result.")

    return {
        "score": score,
        "resume_skills": resume_skills,
        "job_skills": job_skills,
        "matched": matched,
        "missing": missing,
        "tips": tips,
        "word_count": len(resume_text.split()),
        "note": "This is a simple keyword-based learning tool, not an employer's ATS score or a guarantee of getting shortlisted."
    }

@app.route("/", methods=["GET", "POST"])
def index():
    report = None
    resume_text = ""
    job_description = ""
    if request.method == "POST":
        resume_text = request.form.get("resume_text", "")
        job_description = request.form.get("job_description", "")
        report = analyze_resume(resume_text, job_description)
    return render_template(
        "index.html",
        report=report,
        resume_text=resume_text,
        job_description=job_description
    )

if __name__ == "__main__":
    app.run(debug=True)
