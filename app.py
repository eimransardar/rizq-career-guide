from flask import Flask, render_template, request
from helpers import get_rizq_answer

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        question = request.form.get("question", "")
        answer = get_rizq_answer(question)
        return render_template("answer.html", question=question, answer=answer)
    return render_template("index.html")

if __name__ == "__main__":
    app.run()
