import streamlit as st
import pandas as pd

import pickle

st.set_page_config(
    page_title="Student Dropout Early Warning System",
    page_icon="🎓",
    layout="wide"
)


@st.cache_resource
def load_artifacts():
    with open('model.pkl', 'rb') as f_model:
        model = pickle.load(f_model)
    with open('scaler.pkl', 'rb') as f_scaler:
        scaler = pickle.load(f_scaler)
    return model, scaler

try:
    model, scaler = load_artifacts()
except FileNotFoundError:
    st.error("⚠️ Model or Scaler file not found! Please run the training script first.")
    st.stop()

st.title("🎓 Student Dropout Early Warning System")
st.markdown("Predict early dropout risk based on academic, financial, and socio-demographic indicators.")

st.divider()


st.header("📋 Enter Student Profile Data")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Financial & Profile")
    tuition_fees = st.selectbox("Tuition Fees Up To Date", [1, 0], format_func=lambda x: "Yes" if x == 1 else "No")
    debtor = st.selectbox("Debtor (Outstanding Unpaid Fees)", [0, 1], format_func=lambda x: "No" if x == 0 else "Yes")
    scholarship = st.selectbox("Scholarship Holder", [0, 1], format_func=lambda x: "No" if x == 0 else "Yes")
    age = st.number_input("Age at Enrollment", min_value=15, max_value=70, value=20)
    gender = st.selectbox("Gender", [1, 0], format_func=lambda x: "Male" if x == 1 else "Female")
    displaced = st.selectbox("Displaced (Living away from home)", [1, 0], format_func=lambda x: "Yes" if x == 1 else "No")

with col2:
    st.subheader("1st Semester Metrics")
    sem1_enrolled = st.number_input("1st Sem Units Enrolled", min_value=0, max_value=25, value=6)
    sem1_approved = st.number_input("1st Sem Units Approved", min_value=0, max_value=25, value=5)
    sem1_evaluations = st.number_input("1st Sem Evaluations", min_value=0, max_value=40, value=6)
    sem1_grade = st.number_input("1st Sem Avg Grade (0-20)", min_value=0.0, max_value=20.0, value=12.0)

with col3:
    st.subheader("2nd Semester Metrics")
    sem2_enrolled = st.number_input("2nd Sem Units Enrolled", min_value=0, max_value=25, value=6)
    sem2_approved = st.number_input("2nd Sem Units Approved", min_value=0, max_value=25, value=4)
    sem2_evaluations = st.number_input("2nd Sem Evaluations", min_value=0, max_value=40, value=6)
    sem2_grade = st.number_input("2nd Sem Avg Grade (0-20)", min_value=0.0, max_value=20.0, value=11.0)

# Sidebar Defaults for Macro / Background Features
st.sidebar.header("⚙️ Macroeconomic & Demographics")
marital_status = st.sidebar.number_input("Marital Status Code", value=1)
application_mode = st.sidebar.number_input("Application Mode Code", value=1)
application_order = st.sidebar.number_input("Application Order", value=1)
course = st.sidebar.number_input("Course Code", value=5)
daytime_evening = st.sidebar.selectbox("Attendance", [1, 0], format_func=lambda x: "Daytime" if x == 1 else "Evening")
prev_qual = st.sidebar.number_input("Previous Qualification Code", value=1)
nacionality = st.sidebar.number_input("Nationality Code", value=1)
mother_qual = st.sidebar.number_input("Mother's Qualification", value=1)
father_qual = st.sidebar.number_input("Father's Qualification", value=1)
mother_occ = st.sidebar.number_input("Mother's Occupation", value=1)
father_occ = st.sidebar.number_input("Father's Occupation", value=1)
special_needs = st.sidebar.selectbox("Educational Special Needs", [0, 1], format_func=lambda x: "No" if x == 0 else "Yes")
international = st.sidebar.selectbox("International Student", [0, 1], format_func=lambda x: "No" if x == 0 else "Yes")

unemp_rate = st.sidebar.number_input("Unemployment Rate (%)", value=10.8)
inflation = st.sidebar.number_input("Inflation Rate (%)", value=1.4)
gdp = st.sidebar.number_input("GDP Growth Rate (%)", value=1.74)


st.divider()

if st.button("🚀 Analyze Student Risk Status", type="primary", use_container_width=True):
    

    pass_ratio_1st = sem1_approved / (sem1_enrolled + 1e-5)
    pass_ratio_2nd = sem2_approved / (sem2_enrolled + 1e-5)
    grade_change = sem2_grade - sem1_grade
    fin_risk = debtor + (1 - tuition_fees)
    
    
    input_data = {
        'Marital status': marital_status,
        'Application mode': application_mode,
        'Application order': application_order,
        'Course': course,
        'Daytime/evening attendance': daytime_evening,
        'Previous qualification': prev_qual,
        'Nacionality': nacionality,
        "Mother's qualification": mother_qual,
        "Father's qualification": father_qual,
        "Mother's occupation": mother_occ,
        "Father's occupation": father_occ,
        'Displaced': displaced,
        'Educational special needs': special_needs,
        'Debtor': debtor,
        'Tuition fees up to date': tuition_fees,
        'Gender': gender,
        'Scholarship holder': scholarship,
        'Age at enrollment': age,
        'International': international,
        'Curricular units 1st sem (credited)': 0,
        'Curricular units 1st sem (enrolled)': sem1_enrolled,
        'Curricular units 1st sem (evaluations)': sem1_evaluations,
        'Curricular units 1st sem (approved)': sem1_approved,
        'Curricular units 1st sem (grade)': sem1_grade,
        'Curricular units 1st sem (without evaluations)': 0,
        'Curricular units 2nd sem (credited)': 0,
        'Curricular units 2nd sem (enrolled)': sem2_enrolled,
        'Curricular units 2nd sem (evaluations)': sem2_evaluations,
        'Curricular units 2nd sem (approved)': sem2_approved,
        'Curricular units 2nd sem (grade)': sem2_grade,
        'Curricular units 2nd sem (without evaluations)': 0,
        'Unemployment rate': unemp_rate,
        'Inflation rate': inflation,
        'GDP': gdp,
        '1st_sem_pass_ratio': pass_ratio_1st,
        '2nd_sem_pass_ratio': pass_ratio_2nd,
        'grade_change': grade_change, 'financial_risk_score': fin_risk
    }
    
    input_df = pd.DataFrame([input_data])
    
    
    scaled_input = scaler.transform(input_df)
    pred_class = model.predict(scaled_input)[0]
    pred_prob = model.predict_proba(scaled_input)[0][1]
    
    
    st.subheader("🔍 Prediction Results")
    res_col1, res_col2 = st.columns(2)
    
    with res_col1:
        st.metric("Predicted Dropout Probability", f"{pred_prob * 100:.1f}%")
        
        if pred_class == 1:
            st.error("🚨 **ALERT: HIGH DROPOUT RISK FLAGGED**")
        else:
            st.success("✅ **STATUS: LOW RISK / ON TRACK TO GRADUATE**")
            
    with res_col2:
        st.subheader("Recommended Retention Actions")
        if tuition_fees == 0 or debtor == 1:
            st.warning("💳 **Financial Action:** Send notice to Financial Aid office for fee installment plans.")
        if sem2_approved < sem2_enrolled:
            st.warning("📚 **Academic Action:** Assign academic counseling and peer tutoring for unapproved units.")
        if pred_class == 0 and tuition_fees == 1:
            st.info("ℹ️ No immediate critical interventions required. Maintain progress tracking.")