def analyze_student(data):
    attendance = data["attendance"]
    assignments = data["assignments"]
    marks = data["marks"]
    previous = data["previous"]
    participation = data["participation"]

    participation_map = {
        "Low": 40,
        "Medium": 70,
        "High": 100
    }

    participation_score = participation_map.get(participation, 70)

    score = (
        0.25 * attendance +
        0.20 * assignments +
        0.25 * marks +
        0.15 * previous +
        0.15 * participation_score
    )

    if score >= 75:
        risk = "Low Risk"
        color = "green"
    elif score >= 50:
        risk = "Medium Risk"
        color = "orange"
    else:
        risk = "High Risk"
        color = "red"

    reasons = []
    if attendance < 75:
        reasons.append("Low attendance")
    if assignments < 60:
        reasons.append("Poor assignment performance")
    if marks < 60:
        reasons.append("Weak internal marks")
    if participation == "Low":
        reasons.append("Low classroom participation")

    actions = []
    if risk != "Low Risk":
        actions.append("Academic counseling recommended")
    if attendance < 75:
        actions.append("Improve attendance")
    if assignments < 60:
        actions.append("Assignment mentoring required")

    return {
        "score": round(score, 2),
        "risk": risk,
        "color": color,
        "reasons": reasons,
        "actions": actions
    }
