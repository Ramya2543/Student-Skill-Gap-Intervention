
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Student Skill Gap Analyzer",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 Student Placement Risk & Skill-Gap Intervention")
st.write(
    "Analyze student performance, identify skill gaps, "
    "and generate personalized learning recommendations."
)

# Sample student data for demonstration
data = {
    "Name": ["Ananya", "Rahul", "Priya", "Arjun", "Sneha"],
    "Coding": [35, 85, 60, 25, 70],
    "Aptitude": [70, 80, 45, 40, 75],
    "Technical": [60, 90, 55, 35, 80],
    "Communication": [80, 75, 65, 45, 85],
    "Interview": [40, 85, 50, 30, 75]
}

df = pd.DataFrame(data)

recommendations = {
    "Coding": "Practice Python, DSA, sorting and searching.",
    "Aptitude": "Practice quantitative aptitude and logical reasoning.",
    "Technical": "Revise DBMS, OS, CN and data structures.",
    "Communication": "Practice presentations and spoken communication.",
    "Interview": "Attend mock interviews and practice STAR answers."
}

def analyze_student(scores):
    gaps = []
    for skill, score in scores.items():
        if score < 50:
            gaps.append((skill, score, "High"))
        elif score < 70:
            gaps.append((skill, score, "Medium"))

    average = sum(scores.values()) / len(scores)

    if average < 50:
        risk = "High"
    elif average < 70:
        risk = "Medium"
    else:
        risk = "Low"

    return average, risk, gaps

st.subheader("📊 Student Performance Dashboard")
st.dataframe(df, use_container_width=True, hide_index=True)

st.subheader("🔍 Analyze an Individual Student")

names = df["Name"].tolist()
selected = st.selectbox("Select a student", names)

student = df[df["Name"] == selected].iloc[0]

scores = {
    "Coding": int(student["Coding"]),
    "Aptitude": int(student["Aptitude"]),
    "Technical": int(student["Technical"]),
    "Communication": int(student["Communication"]),
    "Interview": int(student["Interview"])
}

average, risk, gaps = analyze_student(scores)

col1, col2, col3 = st.columns(3)

col1.metric("Average Score", f"{average:.1f}/100")
col2.metric("Placement Risk", risk)
col3.metric("Skills Needing Improvement", len(gaps))

st.subheader("📈 Skill Performance")
chart_data = pd.DataFrame({
    "Skill": list(scores.keys()),
    "Score": list(scores.values())
}).set_index("Skill")

st.bar_chart(chart_data)

st.subheader("🎯 Personalized Skill-Gap Recommendations")

if not gaps:
    st.success("No major skill gaps detected. Continue regular practice.")
else:
    for skill, score, severity in sorted(gaps, key=lambda x: x[1]):
        st.markdown(f"### {skill} — {severity} Priority")
        st.write(f"Current score: {score}/100")
        st.write(recommendations[skill])

st.caption(
    "Academic prototype: sample data and score-based risk rules. "
    "Risk categories are indicative, not validated placement predictions."
)
