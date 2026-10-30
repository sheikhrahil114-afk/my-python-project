# ResumeLens — Python Resume & Job-Match Analyzer

A polished local web app that compares resume text with a job description and shows:
- A simple keyword-overlap percentage
- Skills detected in the resume and job description
- Matching skills and potential gaps
- Suggestions for improving the resume

## Requirements
- Python 3.9+
- Internet connection is only needed to download Flask during setup. The page's optional Google Font may fall back to system fonts offline.
- No AI API key is required. This is a keyword-based project, not a true AI model.

## Run on Windows
1. Extract `AI_Resume_Builder.zip`.
2. Open the extracted folder.
3. Click the folder address bar, type `cmd`, and press Enter.
4. Run:
   `py -m pip install -r requirements.txt`
5. Then run:
   `py app.py`
6. Open the local address shown in the terminal (usually `http://127.0.0.1:5000`).

If `py` doesn't work, try replacing `py` with `python`.

## Important privacy note
The app processes text locally in your browser-to-local-server session; it does not send resume text to an external AI service. Avoid pasting sensitive information unless needed. Do not expose the local server to the public internet.

## How the score works
The app detects a predefined list of skill keywords. Its percentage is:
matched detected job-description skills / all detected job-description skills × 100.
This is a simple educational indicator—not an actual ATS score, hiring recommendation, or guarantee of an interview. Keyword detection can miss synonyms and context. Never add skills you do not genuinely have.

## Suggested upgrades
- Save reports to CSV or SQLite
- Add PDF/DOCX resume upload
- Add charts and more skill synonyms
- Add a genuine NLP model with transparent evaluation
