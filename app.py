import streamlit as st
import pandas as pd
import numpy as np

# ------------------------------
# Title and Description
# ------------------------------
st.set_page_config(page_title="Diabetes Risk Criteria - Pakistan", page_icon="💉", layout="centered")

st.title("💉 Diabetes Risk Assessment (Pakistan)")
st.write("""
This tool provides a simple way to assess your **risk for diabetes** based on locally relevant criteria 
for the Pakistani population (considering factors like BMI, age, lifestyle, and family history).
""")

# ------------------------------
# User Input Section
# ------------------------------
st.header("Enter Your Details")

age = st.number_input("Age (years)", min_value=10, max_value=100, step=1)
gender = st.radio("Gender", ("Male", "Female"))
bmi = st.number_input("BMI (Body Mass Index)", min_value=10.0, max_value=60.0, step=0.1)
waist = st.number_input("Waist Circumference (cm)", min_value=40, max_value=150, step=1)
family_history = st.selectbox("Family history of diabetes?", ("No", "Yes"))
physical_activity = st.selectbox("Physical activity level", ("Active", "Moderate", "Sedentary"))
hypertension = st.selectbox("Do you have high blood pressure?", ("No", "Yes"))
diet = st.selectbox("Diet preference", ("Balanced", "High sugar", "High carbs/fat"))

# ------------------------------
# Risk Calculation (Simplified model)
# ------------------------------
risk_score = 0

# Age factor
if age >= 45:
    risk_score += 2
elif age >= 30:
    risk_score += 1

# Gender factor (men at slightly higher risk in South Asia)
if gender == "Male":
    risk_score += 1

# BMI (using South Asian cutoffs)
if bmi >= 30:
    risk_score += 3
elif bmi >= 27:
    risk_score += 2
elif bmi >= 23:
    risk_score += 1

# Waist Circumference (South Asian risk thresholds)
if (gender == "Male" and waist > 90) or (gender == "Female" and waist > 80):
    risk_score += 2

# Family history
if family_history == "Yes":
    risk_score += 2

# Physical activity
if physical_activity == "Sedentary":
    risk_score += 2
elif physical_activity == "Moderate":
    risk_score += 1

# Hypertension
if hypertension == "Yes":
    risk_score += 2

# Diet
if diet in ["High sugar", "High carbs/fat"]:
    risk_score += 1

# ------------------------------
# Risk Level Interpretation
# ------------------------------
st.header("📊 Your Diabetes Risk Result")

if risk_score <= 3:
    st.success("**Low Risk** — Maintain a healthy lifestyle! 🌿")
    advice = "Continue regular physical activity and a balanced diet."
elif 4 <= risk_score <= 7:
    st.warning("**Moderate Risk** — Consider a screening test (Fasting Blood Sugar). ⚠️")
    advice = "Increase activity, reduce refined sugar intake, and monitor blood pressure."
else:
    st.error("**High Risk** — Visit a doctor for screening and counseling! 🚨")
    advice = "Schedule a blood glucose test soon and adopt a low-carb, high-fiber diet."

st.write(f"**Your Risk Score:** {risk_score}/15")
st.write(f"**Recommendation:** {advice}")

# ------------------------------
# Footer
# ------------------------------
st.markdown("---")
st.caption("© 2025 Diabetes Risk Assessment Tool | Adapted for Pakistan | Powered by Streamlit")
