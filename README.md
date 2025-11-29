# Rizq Career Guide – A Qur’an-based AI Career Advisor
#### CS50x Final Project by ImranX

## Overview
Rizq Career Guide is a Flask-powered Qur’an-based AI Advisor that helps users find guidance related to **career, rizq, skills, motivation, hardship, planning, tawakkul, gratitude, and self-improvement**.
It returns relevant Qur’anic ayat based on keywords from the user’s question.

This project blends **Islamic values**, **career guidance**, and **AI-like logic**, offering a simple but powerful tool for students, job seekers, career explorers, and anyone looking for spiritual direction.

---

## Features
- Ask any question about **career, rizq, jobs, skills, money, future**.
- The app scans **50+ curated Qur'anic ayat** stored in `quran_data.json`.
- Smart keyword-matching engine in `helpers.py`.
- Clean UI using HTML, CSS.
- Fully working Flask web app with user input + dynamic response.

---

## How It Works
1. User asks a question in the form.
2. Flask sends the question to `get_rizq_answer()` in `helpers.py`.
3. The function matches keywords with tags from the JSON dataset.
4. The matching Qur’anic ayah is returned.
5. The answer appears beautifully in the UI.

---

## File Structure

rizqais/
│
├── app.py
├── helpers.py
├── quran_data.json
│
├── templates/
│ ├── index.html
│ └── answer.html
│
├── static/
│ └── styles.css
│
├── README.md
└── requirements.txt


---

## File Descriptions

### **app.py**
- Main Flask application
- Handles routing (“/” GET + POST)
- Connects question input to backend logic

### **helpers.py**
- Contains `get_rizq_answer()`
- Reads JSON data (loaded globally)
- Matches user question with keywords/tags

### **quran_data.json**
- Contains 50+ Qur’anic ayat
- Each ayah has:
  - Surah
  - Ayah number
  - Translation
  - Tags/keywords for matching

### **templates/index.html**
- Main UI page
- User inputs question

### **templates/answer.html**
- Displays:
  - User's question
  - Qur’an-based answer

### **static/styles.css**
- Styles and layout
- Clean, simple UI

---

## How to Run the App

### **On CS50 IDE (cs50.dev)**

cd rizqais
flask run


OR:

python app.py


App will run at:


https://eimransardar.cs50.dev:8080


---

## Technologies Used
- Python
- Flask
- HTML, CSS
- JSON data processing
- Keyword-matching algorithm

---

## Example Questions You Can Ask
- “How will I get a job?”
- “What does Islam say about halal rizq?”
- “I’m worried about my future.”
- “How do I improve my skills?”
- “I feel stuck in life.”
- “What if my rizq feels limited?”

---

## Sample Output

User asks:
**“I’m scared about my rizq decreasing.”**

App responds:

**Surah At-Talaq, Ayah 3**
*"And He will provide for him from where he does not expect."*

---

## Final Project Video
Video demonstrates:

- What the app does
- Why you built it
- Live demo
- Code explanation
- How helpers.py works
- How JSON ayat dataset powers the system

Video link (YouTube, 1–3 mins):
**(You will upload your recording here.)**

---

## Inspiration
This project is part of an initiative to provide an **ethical, faith-aligned, halal, spiritually grounded career advisor** based on Qur’anic principles of rizq, tawakkul, patience, effort, and gratitude.

---

## CS50
This was **my Final Project for Harvard University’s CS50**.

“This was CS50!”


