from flask import Flask, render_template, request
import csv
import os

app = Flask(__name__)
CSV_FILE = "students.csv"

if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            "Name", "Attendance", "Internal",
            "Assignment", "Exam", "StudyHours",
            "Score", "Risk"
        ])

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    name = request.form["name"]
    attendance = int(request.form["attendance"])
    internal = int(request.form["internal"])
    assignment = int(request.form["assignment"])
    exam = int(request.form["exam"])
    study_hours = int(request.form["study_hours"])

    score = round(
        attendance * 0.25 +
        internal * 0.25 +
        assignment * 0.15 +
        exam * 0.25 +
        study_hours * 2
    )

    if score >= 75:
        risk = "Low"
        risk_class = "low"
    elif score >= 50:
        risk = "Medium"
        risk_class = "medium"
    else:
        risk = "High"
        risk_class = "high"

    if risk == "Low":
        risk_description = "Student is stable and performing well academically."
    elif risk == "Medium":
        risk_description = "Student needs monitoring and improvement support."
    else:
        risk_description = "Student is academically at risk and needs intervention."

    reasons = []
    if attendance < 75:
        reasons.append("low attendance")
    if internal < 60:
        reasons.append("weak internal marks")
    if assignment < 70:
        reasons.append("average assignments")
    if exam < 50:
        reasons.append("low exam score")
    if study_hours < 2:
        reasons.append("insufficient study hours")

    if reasons:
        explanation = "Academic performance affected due to " + ", ".join(reasons) + "."
    else:
        explanation = "Student shows consistent performance across all parameters."

    if risk == "Low":
        tasks = [
            "Maintain daily study routine",
            "Explore advanced learning topics",
            "Participate in academic competitions",
            "Mentor fellow students"
        ]
    elif risk == "Medium":
        tasks = [
            "Increase daily study hours",
            "Focus on weak subjects",
            "Revise internal test topics",
            "Monthly academic review"
        ]
    else:
        tasks = [
            "Attend remedial classes",
            "Daily structured study plan",
            "Weekly mentor meetings",
            "Focus on exam preparation"
        ]

    with open(CSV_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            name, attendance, internal,
            assignment, exam, study_hours,
            score, risk
        ])

    return render_template(
        "report.html",
        name=name,
        attendance=attendance,
        internal=internal,
        assignment=assignment,
        exam=exam,
        study_hours=study_hours,
        score=score,
        risk=risk,
        risk_class=risk_class,
        risk_description=risk_description,
        explanation=explanation,
        tasks=tasks
    )

if __name__ == "__main__":
    app.run(debug=True)
