# 🎓 Student Score Predictor

A Machine Learning powered web application that predicts a student's final exam score based on academic performance, study habits, digital behavior, lifestyle factors, and mental well-being.

Built using **Python**, **Scikit-Learn**, and **Streamlit**.

---

## 🚀 Features

- Predict final exam scores using Machine Learning
- Interactive and user-friendly Streamlit interface
- Academic performance analysis
- Digital habits assessment
- Mental health and productivity evaluation
- Lifestyle and environmental factor consideration
- Responsive modern UI with custom styling
- Instant prediction results with personalized feedback

---

## 📊 Input Parameters

### 📚 Academic Information
- Age
- Study Hours Per Day
- Deep Work Sessions
- Assignment Completion Rate
- Attendance Percentage

### 📱 Digital Habits
- Social Media Usage
- Doomscrolling Before Sleep
- Notification Distractions
- AI Tool Usage
- Gaming Hours

### 🧠 Mental & Productivity Factors
- Stress Level
- Motivation Level
- Focus Score
- Procrastination Index
- Sleep Hours

### 🏃 Lifestyle Factors
- Caffeine Intake
- Physical Activity Hours

### 🌍 Environment Factors
- Internet Quality
- Family Support
- Financial Stress

### ⚡ Study Efficiency
- Productivity After Midnight
- Revision Efficiency
- Burnout Risk
- Consistency Score

### 🎯 Mental State
- Focused
- Distracted
- Burnout

---

## 🛠️ Technologies Used

### Frontend
- Streamlit

### Backend
- Python

### Machine Learning
- Scikit-Learn
- Pandas
- NumPy
- Joblib

---

## 📂 Project Structure

```text
Student-Score-Predictor/
│
├── app.py
├── student_score_model.pkl
├── scaler.pkl
├── requirements.txt
├── README.md
│
├── dataset/
│   └── student_data.csv
│
├── notebooks/
│   └── model_training.ipynb
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YashChandiramani/Student_Score_Prediction_ML_Project.git
```

### 2. Navigate to Project Folder

```bash
cd Student_Score_Prediction_ML_Project
```

### 3. Create Virtual Environment (Optional)

```bash
python -m venv venv
```

Activate:

Windows

```bash
venv\Scripts\activate
```

Linux/Mac

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run Application

```bash
streamlit run app2_working.py
```

---

## 📈 Machine Learning Workflow

1. Data Collection
2. Data Cleaning
3. Feature Engineering
4. Data Scaling
5. Model Training
6. Model Evaluation
7. Model Serialization using Joblib
8. Deployment with Streamlit

---

## 🎯 Prediction Output

The model predicts a student's expected final exam score on a scale of:

```text
0 - 100
```

Performance Categories:

| Score Range | Category |
|------------|----------|
| 85 - 100 | Excellent |
| 70 - 84 | Good |
| 50 - 69 | Average |
| Below 50 | Needs Improvement |

---



---

## 🔮 Future Enhancements

- User Authentication System
- Prediction History Storage
- MySQL Database Integration
- Personalized Study Recommendations
- Dashboard Analytics
- Cloud Deployment
- Mobile Responsive Design

---

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to your branch
5. Open a Pull Request

---

## 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Yash Chandiramani**

Passionate about Machine Learning, Data Science, and Full Stack Development.

---

### ⭐ If you found this project useful, consider giving it a star on GitHub!
