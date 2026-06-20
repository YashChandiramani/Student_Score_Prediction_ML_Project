import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="Student Score Predictor",
    page_icon="🎓",
    layout="wide"
)

st.markdown("""
<style>

/* Background */
.stApp {
    background: linear-gradient(
        135deg,
        #0f172a 0%,
        #1e293b 50%,
        #334155 100%
    );
}

/* Main container */
.block-container {
    padding-top: 1rem;
    max-width: 1200px;
}

/* Title */
.main-title {
    text-align: center;
    font-size: 3rem;
    font-weight: 800;
    color: white;
    margin-bottom: 0px;
}

.subtitle {
    text-align: center;
    color: #cbd5e1;
    font-size: 1.1rem;
    margin-bottom: 30px;
}

/* Section headers */
.section-header {
    background: linear-gradient(
        90deg,
        #2563eb,
        #06b6d4
    );
    color: white;
    padding: 12px 20px;
    border-radius: 12px;
    font-size: 20px;
    font-weight: bold;
    margin-top: 25px;
    margin-bottom: 15px;
}

/* Labels */
label {
    color: white !important;
    font-weight: 500 !important;
}

/* Sliders */
.stSlider {
    padding-top: 5px;
    padding-bottom: 10px;
}

/* Number inputs */
.stNumberInput input {
    border-radius: 10px !important;
}

/* Selectboxes */
.stSelectbox > div {
    border-radius: 10px;
}

/* Button */
.stButton > button {
    width: 100%;
    height: 60px;
    border-radius: 15px;
    border: none;
    font-size: 22px;
    font-weight: bold;
    background: linear-gradient(
        90deg,
        #2563eb,
        #06b6d4
    );
    color: white;
    transition: all 0.3s ease;
}

.stButton > button:hover {
    transform: scale(1.02);
}

/* Prediction card */
.result-card {
    background: linear-gradient(
        135deg,
        #22c55e,
        #16a34a
    );
    color: white;
    text-align: center;
    padding: 25px;
    border-radius: 20px;
    font-size: 28px;
    font-weight: bold;
    margin-top: 20px;
    box-shadow: 0px 8px 25px rgba(0,0,0,0.3);
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #111827;
}

/* Scrollbar */
::-webkit-scrollbar {
    width: 8px;
}

::-webkit-scrollbar-thumb {
    background: #3b82f6;
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)


# Load model and scaler
model = joblib.load("student_score_model.pkl")
scaler = joblib.load("scaler.pkl")

st.set_page_config(page_title="Student Score Predictor", page_icon="🎓")

st.markdown("""
<div class="main-title">
🎓 Student Score Predictor
</div>

<div class="subtitle">
Predict your final exam score using machine learning,

Please be honest while filling the input fields
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:

    st.markdown("""
    <div class='section-header'
         style='color:white !important;'>
         📚 Academic Information
    </div>
    """, unsafe_allow_html=True)

    age = st.slider("Age", 4, 50, 20)

    study_hours_per_day = st.slider(
        "Study Hours Per Day", 0.0, 9.0, 4.0, 0.1
    )

    deep_work_sessions = st.slider(
        "How many hours you actually do work?", 0, 7, 3
    )

    assignment_completion_rate = st.slider(
        "How many Assignments have you completed?", 0, 100, 80
    )

    attendance_percentage = st.slider(
        "Attendance Percentage (%)", 0, 100, 80
    )

with col2:

    st.markdown("""
    <div class='section-header'
         style='color:white !important;'>
         📱 Digital Habits
    </div>
    """, unsafe_allow_html=True)

    social_media_hours = st.slider(
        "How many hours you spend on Social Media?", 0.0, 9.0, 2.0, 0.1
    )

    doomscrolling_before_sleep = st.selectbox(
        "Do you do Doomscrolling Before Sleep",
        [0, 1],
        format_func=lambda x: "Yes" if x == 1 else "No"
    )

    notification_distractions = st.slider(
        "Do Notifications distract you?(Grade yourself from 5 to 120)", 5, 120, 50
    )

    ai_tool_usage_hours = st.slider(
        "For how many hours do you use AI Tools?", 0.0, 5.0, 1.0, 0.1
    )

    gaming_hours = st.slider(
        "How many hours on Gaming?", 0.0, 7.5, 2.0, 0.1
    )

col3, col4 = st.columns(2)

with col3:

    st.markdown("""
    <div class='section-header'
         style='color:white !important;'>
         🧠 Mental & Productivity Factors
    </div>
    """, unsafe_allow_html=True)

    stress_level = st.slider(
        "Do you feel Stressed out? (Score yourself on 1-10)", 1, 10, 5
    )

    motivation_level = st.slider(
        "What is your motivation level while studying? (Score yourself on 1-10)", 1, 10, 5
    )

    focus_score = st.slider(
        "What is you Focus Score? (Score yourself on 1-10)", 1.0, 10.0, 5.0, 0.1
    )

    procrastination_index = st.slider(
        "Do you Procastinate? (Score yourself on 1-10)", 0, 10, 5
    )

    sleep_hours = st.slider(
        "How many hours do you Sleep?", 3.0, 10.0, 7.0, 0.1
    )

with col4:

    st.markdown("""
    <div class='section-header'
         style='color:white !important;'>
         🏃 Lifestyle
    </div>
    """, unsafe_allow_html=True)

    caffeine_intake = st.slider(
        "How many cups of Caffeine(Tea/Coffee) you consume everday?", 0, 7, 2
    )

    physical_activity_hours = st.slider(
        "How much are you giving time to your Physical Health?", 0.0, 4.0, 1.0, 0.1
    )

col5, col6 = st.columns(2)

with col5:

    st.markdown("""
    <div class='section-header'
         style='color:white !important;'>
         🌍 Environment
    </div>
    """, unsafe_allow_html=True)

    internet_quality = st.slider(
        "How is your Internet Quality of place you live?", 1, 10, 5
    )

    family_support = st.slider(
        "Is your family supportive?", 1, 10, 5
    )

    financial_stress = st.slider(
        "Are you having any financial stress? (Study Loan, etc)", 1, 10, 5
    )

with col6:

    st.markdown("""
    <div class='section-header'
         style='color:white !important;'>
         ⚡ Study Efficiency
    </div>
    """, unsafe_allow_html=True)

    productivity_after_midnight = st.slider(
        "Do you study late nights (if yes then for how long)?", 1, 10, 5
    )

    revision_efficiency = st.slider(
        "How much Last minute revision helps you in the exam? (Score yourself on 1-10)", 1, 10, 5
    )

    burnout_risk = st.slider(
        "Do you consider yourself Burned out? (if yes (Score yourself on 1-10))", 1, 10, 5
    )

    consistency_score = st.slider(
        "Are you a consitent performer? (Score yourself on 1-10)", 1, 10, 5
    )

_, center_col, _ = st.columns([1, 2, 1])

with center_col:

    st.markdown("""
    <div class='section-header'
         style='color:white !important; text-align:center;'>
         🎯 Mental State
    </div>
    """, unsafe_allow_html=True)

    mental_state = st.selectbox(
        "Current Mental State",
        ["Focused", "Distracted", "Burnout"]
    )

mental_state_burnout = 1 if mental_state == "Burnout" else 0
mental_state_distracted = 1 if mental_state == "Distracted" else 0
mental_state_focused = 1 if mental_state == "Focused" else 0

# --------------------------
# Prediction
# --------------------------

col1, col2, col3 = st.columns([2,1,2])

with col2:
    predict_clicked = st.button("Predict Score")

if predict_clicked:

    data = [[
        age,
        study_hours_per_day,
        deep_work_sessions,
        assignment_completion_rate,
        attendance_percentage,
        social_media_hours,
        doomscrolling_before_sleep,
        notification_distractions,
        ai_tool_usage_hours,
        gaming_hours,
        stress_level,
        motivation_level,
        focus_score,
        procrastination_index,
        sleep_hours,
        caffeine_intake,
        physical_activity_hours,
        internet_quality,
        family_support,
        financial_stress,
        productivity_after_midnight,
        revision_efficiency,
        burnout_risk,
        consistency_score,
        mental_state_burnout,
        mental_state_distracted,
        mental_state_focused
    ]]

    data_scaled = scaler.transform(data)

    prediction = model.predict(data_scaled)[0]

    prediction = max(0, min(100, prediction))

    st.success(f"🎯 Predicted Final Exam Score: {prediction:.2f}")

    if prediction >= 85:
        st.balloons()
        st.info("Excellent performance expected!")
    elif prediction >= 70:
        st.info("Good performance expected.")
    elif prediction >= 50:
        st.warning("Average performance expected.")
    else:
        st.error("Low predicted score. Consider improving study habits.")