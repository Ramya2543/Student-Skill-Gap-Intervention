# Student Placement Failure Risk & Skill-Gap Intervention

## Project Overview

The **Student Placement Failure Risk & Skill-Gap Intervention** project aims to help identify students who may need additional preparation for campus placements. It focuses on skill areas such as coding, aptitude, technical knowledge, communication, and interview readiness.

A Streamlit web application has been created as the initial prototype. The current version uses sample student data and rule-based logic to demonstrate a basic dashboard, risk categories, and skill-improvement suggestions.

## Current Status

**Current stage: Prototype completed; machine-learning implementation is planned.**

Implemented so far:
- Streamlit web application.
- Dashboard using sample student records.
- Student selection and score summary.
- Basic placement-risk categorisation using predefined score thresholds.
- Skill-gap indicators and improvement suggestions.
- Public deployment through Streamlit Community Cloud.

> Important: The current version does not yet use a trained machine-learning model. Its risk categories are based on predefined rules and are intended only to demonstrate the concept.

## Planned Machine-Learning Implementation

The next phase will develop and integrate a machine-learning model after suitable student placement data is obtained and reviewed.

Planned work:
1. Collect or identify an appropriate dataset with student skill indicators and placement outcomes.
2. Clean the data and select relevant input features.
3. Train and compare suitable classification algorithms, such as Logistic Regression, Decision Tree, and Random Forest.
4. Evaluate the selected model using appropriate metrics, such as accuracy, precision, recall, F1-score, and a confusion matrix.
5. Integrate the evaluated model into the Streamlit application.
6. Accept new student details and skill scores through a form.
7. Display the model's predicted placement outcome/risk category along with skill-gap recommendations.

The final algorithm will be selected based on the dataset and evaluation results. No model accuracy or predictive performance is claimed at this stage.

## Planned Inputs and Outputs

**Potential inputs**
- Coding score
- Aptitude score
- Technical knowledge score
- Communication score
- Interview-readiness score
- Other relevant fields, if available in the dataset

**Planned outputs**
- Estimated placement outcome or risk category
- Skill areas that may need improvement
- Suggested preparation activities

Predictions will be estimates, not guarantees of an individual student's placement outcome.

## Technology Stack

- Python
- Streamlit
- Pandas
- scikit-learn (listed as a dependency for the planned ML phase)
- GitHub
- Streamlit Community Cloud

## Run Locally

1. Install Python.
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. Install dependencies:

   ```bash
   python -m pip install -r requirements.txt
   ```

5. Run the application:

   ```bash
   python -m streamlit run app.py
   ```

## Links

- **Live prototype:** https://ramya2543-student-skill-gap-intervention.streamlit.app/
- **GitHub repository:** https://github.com/Ramya2543/Student-Skill-Gap-Intervention

## Limitations

- The current prototype uses sample data.
- Current risk categorisation is rule-based, not ML-based.
- A suitable labelled dataset is needed to train and meaningfully evaluate the future model.
- The planned ML features and evaluation have not yet been completed.

## Future Scope

- Upload student data through CSV.
- Train and evaluate a classification model using suitable historical data.
- Add visual reports and model evaluation results.
- Improve recommendations based on identified skill gaps.
- Document model limitations, fairness considerations, and appropriate use of predictions.
