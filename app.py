import streamlit as st
import pandas as pd
import joblib
import plotly.graph_objects as go
import plotly.express as px


st.set_page_config(
    page_title="Customer Churn Intelligence Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)


model = joblib.load("best_churn_pipeline.pkl")

st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #0b1220, #111827, #172554);
    color: white;
}

[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0f172a, #111827);
    color: white;
}

.block-container {
    padding-top: 1.5rem;
    padding-bottom: 2rem;
}

.hero-card {
    background: linear-gradient(135deg, rgba(37,99,235,0.25), rgba(168,85,247,0.25));
    backdrop-filter: blur(16px);
    border: 1px solid rgba(255,255,255,0.12);
    border-radius: 26px;
    padding: 34px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.28);
    margin-bottom: 22px;
}

.metric-card {
    background: rgba(255,255,255,0.08);
    backdrop-filter: blur(16px);
    border: 1px solid rgba(255,255,255,0.12);
    border-radius: 24px;
    padding: 22px;
    text-align: center;
    box-shadow: 0 8px 24px rgba(0,0,0,0.24);
    margin-bottom: 18px;
}

.section-card {
    background: rgba(255,255,255,0.08);
    backdrop-filter: blur(16px);
    border: 1px solid rgba(255,255,255,0.12);
    border-radius: 24px;
    padding: 24px;
    box-shadow: 0 8px 24px rgba(0,0,0,0.22);
    margin-bottom: 18px;
}

.big-title {
    font-size: 40px;
    font-weight: 800;
    color: white;
    margin-bottom: 6px;
}

.subtitle {
    font-size: 17px;
    color: #cbd5e1;
}

.card-title {
    font-size: 24px;
    font-weight: 700;
    color: white;
    margin-bottom: 14px;
}

.small-text {
    font-size: 14px;
    color: #cbd5e1;
}

.kpi-label {
    font-size: 14px;
    color: #cbd5e1;
}

.kpi-value {
    font-size: 28px;
    font-weight: 800;
    color: white;
}

.badge-green, .badge-yellow, .badge-red {
    display: inline-block;
    padding: 10px 18px;
    border-radius: 999px;
    font-weight: 700;
    font-size: 16px;
}

.badge-green {
    background: rgba(34,197,94,0.18);
    color: #4ade80;
}

.badge-yellow {
    background: rgba(250,204,21,0.18);
    color: #fde047;
}

.badge-red {
    background: rgba(239,68,68,0.18);
    color: #f87171;
}

.insight-pill {
    display: inline-block;
    padding: 8px 14px;
    margin: 6px 8px 6px 0;
    border-radius: 999px;
    background: rgba(255,255,255,0.10);
    border: 1px solid rgba(255,255,255,0.10);
    color: white;
    font-size: 14px;
}

footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)


st.sidebar.markdown("## 🎛 Customer Controls")
st.sidebar.write("Adjust the customer profile and run churn prediction.")

gender = st.sidebar.selectbox("Gender", ["Male", "Female"])
senior_citizen = st.sidebar.selectbox("Senior Citizen", [0, 1])
partner = st.sidebar.selectbox("Partner", ["Yes", "No"])
dependents = st.sidebar.selectbox("Dependents", ["Yes", "No"])
tenure_months = st.sidebar.slider("Tenure Months", 0, 72, 12)
phone_service = st.sidebar.selectbox("Phone Service", ["Yes", "No"])
internet_service = st.sidebar.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
online_security = st.sidebar.selectbox("Online Security", ["Yes", "No", "No internet service"])
tech_support = st.sidebar.selectbox("Tech Support", ["Yes", "No", "No internet service"])
contract = st.sidebar.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
paperless_billing = st.sidebar.selectbox("Paperless Billing", ["Yes", "No"])
payment_method = st.sidebar.selectbox(
    "Payment Method",
    [
        "Electronic check",
        "Mailed check",
        "Bank transfer (automatic)",
        "Credit card (automatic)"
    ]
)
monthly_charges = st.sidebar.number_input("Monthly Charges", min_value=0.0, value=70.0)
total_charges = st.sidebar.number_input("Total Charges", min_value=0.0, value=1000.0)

predict_btn = st.sidebar.button("🚀 Run Prediction", use_container_width=True)

input_data = pd.DataFrame([{
    'Gender': gender,
    'Senior Citizen': senior_citizen,
    'Partner': partner,
    'Dependents': dependents,
    'Tenure Months': tenure_months,
    'Phone Service': phone_service,
    'Internet Service': internet_service,
    'Online Security': online_security,
    'Tech Support': tech_support,
    'Contract': contract,
    'Paperless Billing': paperless_billing,
    'Payment Method': payment_method,
    'Monthly Charges': monthly_charges,
    'Total Charges': total_charges
}])

risk_flags = []

if contract == "Month-to-month":
    risk_flags.append("Short-term contract")
if internet_service == "Fiber optic":
    risk_flags.append("Fiber plan churn tendency")
if online_security == "No":
    risk_flags.append("No online security")
if tech_support == "No":
    risk_flags.append("No tech support")
if monthly_charges > 80:
    risk_flags.append("High monthly bill")
if tenure_months < 12:
    risk_flags.append("New customer")
if paperless_billing == "Yes":
    risk_flags.append("Paperless billing segment")
if payment_method == "Electronic check":
    risk_flags.append("Electronic check payment")


st.markdown("""
<div class="hero-card">
    <div class="big-title">📊 Customer Churn Intelligence Dashboard</div>
    <div class="subtitle">
        Premium AI-powered telecom churn analytics dashboard with predictive scoring, risk insights, and retention strategies.
    </div>
</div>
""", unsafe_allow_html=True)


k1, k2, k3, k4 = st.columns(4)

with k1:
    st.markdown(f"""
    <div class="metric-card">
        <div class="kpi-label">📅 Tenure</div>
        <div class="kpi-value">{tenure_months} Months</div>
    </div>
    """, unsafe_allow_html=True)

with k2:
    st.markdown(f"""
    <div class="metric-card">
        <div class="kpi-label">💳 Monthly Charges</div>
        <div class="kpi-value">₹ {monthly_charges:.2f}</div>
    </div>
    """, unsafe_allow_html=True)

with k3:
    st.markdown(f"""
    <div class="metric-card">
        <div class="kpi-label">💰 Total Charges</div>
        <div class="kpi-value">₹ {total_charges:.2f}</div>
    </div>
    """, unsafe_allow_html=True)

with k4:
    st.markdown(f"""
    <div class="metric-card">
        <div class="kpi-label">📄 Contract</div>
        <div class="kpi-value">{contract}</div>
    </div>
    """, unsafe_allow_html=True)


tab1, tab2, tab3 = st.tabs(["🏠 Overview", "🎯 Prediction", "📈 Insights"])

prediction = None
probability = None

if predict_btn:
    prediction = model.predict(input_data)[0]
    probability = float(model.predict_proba(input_data)[0][1])

    if probability < 0.30:
        risk_label = "Low Risk"
        badge_class = "badge-green"
        risk_distribution = [82, 18]
    elif probability < 0.70:
        risk_label = "Medium Risk"
        badge_class = "badge-yellow"
        risk_distribution = [55, 45]
    else:
        risk_label = "High Risk"
        badge_class = "badge-red"
        risk_distribution = [22, 78]

with tab1:
    left, right = st.columns([1.2, 1])

    with left:
        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.markdown('<div class="card-title">👤 Customer Snapshot</div>', unsafe_allow_html=True)
        st.dataframe(input_data.T, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with right:
        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.markdown('<div class="card-title">🧠 Risk Indicators</div>', unsafe_allow_html=True)

        if risk_flags:
            for flag in risk_flags:
                st.markdown(f'<span class="insight-pill">⚡ {flag}</span>', unsafe_allow_html=True)
        else:
            st.markdown('<span class="insight-pill">Stable profile</span>', unsafe_allow_html=True)

        st.write("")
        st.caption("These are business-facing churn signals based on the customer profile.")
        st.markdown('</div>', unsafe_allow_html=True)

with tab2:
    if predict_btn:
        colA, colB = st.columns([1.1, 1])

        with colA:
            st.markdown('<div class="section-card">', unsafe_allow_html=True)
            st.markdown('<div class="card-title">🎯 Churn Score</div>', unsafe_allow_html=True)

            gauge = go.Figure(go.Indicator(
                mode="gauge+number",
                value=probability * 100,
                number={'suffix': "%"},
                title={'text': "Predicted Churn Probability"},
                gauge={
                    'axis': {'range': [0, 100]},
                    'bar': {'color': "white"},
                    'steps': [
                        {'range': [0, 30], 'color': "#16a34a"},
                        {'range': [30, 70], 'color': "#ca8a04"},
                        {'range': [70, 100], 'color': "#dc2626"}
                    ]
                }
            ))
            gauge.update_layout(
                paper_bgcolor="rgba(0,0,0,0)",
                font={'color': "white", 'size': 18},
                height=350
            )
            st.plotly_chart(gauge, use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)

        with colB:
            st.markdown('<div class="section-card">', unsafe_allow_html=True)
            st.markdown('<div class="card-title">📌 Prediction Result</div>', unsafe_allow_html=True)

            if prediction == 1:
                st.error("⚠️ This customer is likely to churn.")
            else:
                st.success("✅ This customer is likely to stay.")

            st.write(f"### Churn Probability: **{probability:.2%}**")
            st.markdown(f'<div class="{badge_class}">{"🟢" if risk_label=="Low Risk" else "🟡" if risk_label=="Medium Risk" else "🔴"} {risk_label}</div>', unsafe_allow_html=True)
            st.write("")
            st.caption("Risk category is derived from the churn probability score.")
            st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.markdown('<div class="card-title">💡 Retention Strategy</div>', unsafe_allow_html=True)

        if probability > 0.70:
            st.write("### Immediate Retention Action Required")
            st.write("- Offer **loyalty discounts or personalized retention plans**")
            st.write("- Provide **priority technical support**")
            st.write("- Encourage migration to a **1-year or 2-year contract**")
            st.write("- Review **billing pain points** and service quality")
            st.write("- Trigger a **high-priority retention campaign**")
        elif probability > 0.30:
            st.write("### Moderate Retention Opportunity")
            st.write("- Send **engagement and bundle offers**")
            st.write("- Promote **support and service add-ons**")
            st.write("- Encourage long-term value plans")
            st.write("- Monitor satisfaction and service usage")
        else:
            st.write("### Stable Customer Strategy")
            st.write("- Maintain strong service experience")
            st.write("- Offer occasional rewards and upsell campaigns")
            st.write("- Preserve engagement with personalized communication")

        st.markdown('</div>', unsafe_allow_html=True)

    else:
        st.info("Use the sidebar and click **Run Prediction** to generate the churn analysis.")

with tab3:
    if predict_btn:
        left, right = st.columns([1, 1])

        with left:
            st.markdown('<div class="section-card">', unsafe_allow_html=True)
            st.markdown('<div class="card-title">🟠 Risk Mix</div>', unsafe_allow_html=True)

            donut = go.Figure(data=[go.Pie(
                labels=["Stable Probability", "Churn Probability"],
                values=risk_distribution,
                hole=0.65
            )])
            donut.update_layout(
                paper_bgcolor="rgba(0,0,0,0)",
                font={'color': "white"},
                height=350,
                showlegend=True
            )
            st.plotly_chart(donut, use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)

        with right:
            st.markdown('<div class="section-card">', unsafe_allow_html=True)
            st.markdown('<div class="card-title">📊 Business Interpretation</div>', unsafe_allow_html=True)

            insight_rows = []
            insight_rows.append(["Contract Type", contract])
            insight_rows.append(["Internet Service", internet_service])
            insight_rows.append(["Tech Support", tech_support])
            insight_rows.append(["Online Security", online_security])
            insight_rows.append(["Payment Method", payment_method])
            insight_rows.append(["Tenure Segment", "Low" if tenure_months < 12 else "Medium" if tenure_months < 36 else "High"])
            insight_rows.append(["Billing Pressure", "High" if monthly_charges > 80 else "Moderate" if monthly_charges > 50 else "Low"])

            insight_df = pd.DataFrame(insight_rows, columns=["Business Factor", "Current Status"])
            st.dataframe(insight_df, use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.markdown('<div class="card-title">⚡ Top Churn Drivers (Business View)</div>', unsafe_allow_html=True)

        driver_scores = {
            "Month-to-month contract": 90 if contract == "Month-to-month" else 20,
            "No tech support": 80 if tech_support == "No" else 20,
            "No online security": 75 if online_security == "No" else 20,
            "High monthly charges": 85 if monthly_charges > 80 else 40,
            "Electronic check": 70 if payment_method == "Electronic check" else 25,
            "Low tenure": 88 if tenure_months < 12 else 35
        }

        driver_df = pd.DataFrame({
            "Factor": list(driver_scores.keys()),
            "Impact Score": list(driver_scores.values())
        }).sort_values("Impact Score", ascending=True)

        bar = px.bar(
            driver_df,
            x="Impact Score",
            y="Factor",
            orientation="h",
            text="Impact Score"
        )
        bar.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font=dict(color="white"),
            height=420
        )
        st.plotly_chart(bar, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    else:
        st.info("Insights will appear after you run a prediction.")

st.markdown("")
st.caption("Built with Streamlit | ML Pipeline + XGBoost | Customer Churn Intelligence System")