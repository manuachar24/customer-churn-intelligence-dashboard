
import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="AI Customer Intelligence",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

@st.cache_resource
def load_model():
    return joblib.load("best_churn_pipeline.pkl")

pipeline = load_model()

st.markdown("""
<style>

.stApp {
    background: linear-gradient(
        135deg,
        #020617,
        #0f172a,
        #111827
    );
}

.main-box {
    background: rgba(17,24,39,0.72);
    border-radius: 28px;
    padding: 35px;
    border: 1px solid rgba(255,255,255,0.08);
    backdrop-filter: blur(12px);
}

.hero {
    background: linear-gradient(
        135deg,
        #7c3aed,
        #2563eb,
        #06b6d4
    );
    padding: 45px;
    border-radius: 30px;
    margin-bottom: 30px;
}

.hero-title {
    color: white;
    font-size: 58px;
    font-weight: 900;
}

.hero-sub {
    color: rgba(255,255,255,0.82);
    font-size: 20px;
    margin-top: 12px;
}

.stButton > button {
    width: 100%;
    background: linear-gradient(
        135deg,
        #7c3aed,
        #2563eb
    );
    color: white;
    border-radius: 16px;
    border: none;
    padding: 14px;
    font-size: 18px;
    font-weight: 700;
}

h1,h2,h3,h4,h5,p,label {
    color: white !important;
}

[data-baseweb="select"] {
    background-color: #111827;
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
    <div class="hero-title">📊 AI Customer Intelligence</div>
    <div class="hero-sub">
        Premium AI-powered customer churn prediction and retention analytics platform.
    </div>
</div>
""", unsafe_allow_html=True)
st.markdown('<div class="main-box">', unsafe_allow_html=True)
st.subheader("📝 Customer Information")
left, right = st.columns(2)
with left:
    gender = st.selectbox(
        "Gender",
        ["Male", "Female"]
    )
    senior = st.selectbox(
        "Senior Citizen",
        [0,1]
    )
    partner = st.selectbox(
        "Partner",
        ["Yes", "No"]
    )
    dependents = st.selectbox(
        "Dependents",
        ["Yes", "No"]
    )
    tenure = st.slider(
        "Tenure Months",
        0,
        72,
        12
    )
    contract = st.selectbox(
        "Contract Type",
        [
            "Month-to-month",
            "One year",
            "Two year"
        ]
    )
with right:
    internet = st.selectbox(
        "Internet Service",
        ["DSL", "Fiber optic", "No"]
    )
    security = st.selectbox(
        "Online Security",
        ["Yes", "No", "No internet service"]
    )
    tech_support = st.selectbox(
        "Tech Support",
        ["Yes", "No", "No internet service"]
    )
    payment = st.selectbox(
        "Payment Method",
        [
            "Electronic check",
            "Mailed check",
            "Bank transfer (automatic)",
            "Credit card (automatic)"
        ]
    )
    monthly = st.slider(
        "Monthly Charges",
        0,
        200,
        75
    )
    total = st.number_input(
        "Total Charges",
        0,
        10000,
        1500
    )
st.write("")
if st.button("🚀 Analyze Customer"):

    input_df = pd.DataFrame([{
        'Gender': gender,
        'Senior Citizen': senior,
        'Partner': partner,
        'Dependents': dependents,
        'Tenure Months': tenure,
        'Phone Service': 'Yes',
        'Internet Service': internet,
        'Online Security': security,
        'Tech Support': tech_support,
        'Contract': contract,
        'Paperless Billing': 'Yes',
        'Payment Method': payment,
        'Monthly Charges': monthly,
        'Total Charges': total
    }])

    prediction = pipeline.predict(input_df)[0]

    probability = pipeline.predict_proba(input_df)[0][1]

    st.session_state["prediction"] = prediction
    st.session_state["probability"] = probability
    st.session_state["input_df"] = input_df

    st.switch_page("pages/dashboard.py")

st.markdown('</div>', unsafe_allow_html=True)
