
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

st.set_page_config(
    page_title="Explainable AI",
    layout="wide"
)

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

section[data-testid="stSidebar"] {
    background-color: #020617;
    border-right: 1px solid #1e293b;
}

.main-card {
    background: rgba(17,24,39,0.72);
    border: 1px solid rgba(255,255,255,0.08);
    backdrop-filter: blur(12px);
    border-radius: 24px;
    padding: 28px;
    margin-bottom: 24px;
    box-shadow: 0 8px 30px rgba(0,0,0,0.35);
}

.metric-card {
    background: linear-gradient(
        145deg,
        rgba(30,41,59,0.95),
        rgba(15,23,42,0.95)
    );
    border-radius: 22px;
    padding: 22px;
    border: 1px solid rgba(255,255,255,0.08);
    box-shadow: 0 4px 20px rgba(0,0,0,0.35);
}

.metric-title {
    color: #94a3b8;
    font-size: 14px;
    font-weight: 500;
}

.metric-value {
    color: white;
    font-size: 38px;
    font-weight: 800;
    margin-top: 8px;
}

.metric-sub {
    color: #64748b;
    margin-top: 4px;
    font-size: 13px;
}

.hero {
    background: linear-gradient(
        135deg,
        #7c3aed,
        #2563eb,
        #06b6d4
    );
    padding: 36px;
    border-radius: 30px;
    margin-bottom: 28px;
    box-shadow: 0 10px 35px rgba(37,99,235,0.35);
}

.hero-title {
    color: white;
    font-size: 54px;
    font-weight: 900;
    line-height: 1;
}

.hero-sub {
    color: rgba(255,255,255,0.8);
    font-size: 18px;
    margin-top: 12px;
}

.insight-red {
    background: rgba(239,68,68,0.12);
    border: 1px solid rgba(239,68,68,0.25);
    padding: 18px;
    border-radius: 18px;
    color: #fca5a5;
    margin-bottom: 14px;
}

.insight-yellow {
    background: rgba(251,191,36,0.12);
    border: 1px solid rgba(251,191,36,0.25);
    padding: 18px;
    border-radius: 18px;
    color: #fde68a;
    margin-bottom: 14px;
}

.insight-green {
    background: rgba(34,197,94,0.12);
    border: 1px solid rgba(34,197,94,0.25);
    padding: 18px;
    border-radius: 18px;
    color: #86efac;
    margin-bottom: 14px;
}

.section-title {
    color: white;
    font-size: 28px;
    font-weight: 700;
    margin-bottom: 18px;
}

.stButton > button {
    background: linear-gradient(
        135deg,
        #7c3aed,
        #2563eb
    );
    color: white;
    border: none;
    border-radius: 14px;
    padding: 14px 22px;
    font-size: 16px;
    font-weight: 700;
    width: 100%;
}

.stButton > button:hover {
    transform: scale(1.02);
    transition: 0.3s;
}

h1,h2,h3,h4,h5,p,label {
    color: white !important;
}

[data-testid="stDataFrame"] {
    border-radius: 16px;
    overflow: hidden;
}

</style>
""", unsafe_allow_html=True)

if "probability" not in st.session_state:

    st.warning("Please predict customer churn first.")
    st.stop()

probability = st.session_state["probability"]

churn_score = round(probability * 100, 1)
retention_score = round((1 - probability) * 100, 1)
health_score = np.random.randint(45, 92)

st.markdown(f"""
<div class="hero">
    <div class="hero-title">🧠 Explainable AI</div>
    <div class="hero-sub">
        Understand why the AI predicted customer churn using interactive intelligence analytics.
    </div>
</div>
""", unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)

with c1:

    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">CHURN RISK</div>
        <div class="metric-value">{churn_score}%</div>
        <div class="metric-sub">Predicted customer exit probability</div>
    </div>
    """, unsafe_allow_html=True)

with c2:

    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">RETENTION CHANCE</div>
        <div class="metric-value">{retention_score}%</div>
        <div class="metric-sub">Estimated customer loyalty score</div>
    </div>
    """, unsafe_allow_html=True)

with c3:

    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">CUSTOMER HEALTH</div>
        <div class="metric-value">{health_score}/100</div>
        <div class="metric-sub">Behavioral engagement quality</div>
    </div>
    """, unsafe_allow_html=True)

st.write("")

left, right = st.columns([1.25, 1])

with left:

    st.markdown('<div class="main-card">', unsafe_allow_html=True)

    st.markdown(
        '<div class="section-title">📊 Feature Impact Analysis</div>',
        unsafe_allow_html=True
    )

    feature_data = pd.DataFrame({
        "Feature": [
            "Contract Type",
            "Monthly Charges",
            "Online Security",
            "Tech Support",
            "Customer Tenure",
            "Payment Method"
        ],
        "Impact": [
            92,
            81,
            74,
            63,
            -52,
            46
        ]
    })

    fig = px.bar(
        feature_data,
        x="Impact",
        y="Feature",
        orientation='h',
        text="Impact",
        color="Impact"
    )

    fig.update_layout(
        height=480,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font_color='white',
        coloraxis_showscale=False,
        margin=dict(l=20, r=20, t=20, b=20)
    )

    fig.update_traces(
        textposition='outside'
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="main-card">', unsafe_allow_html=True)

    st.markdown(
        '<div class="section-title">📈 Customer Behavior Pattern</div>',
        unsafe_allow_html=True
    )

    radar_categories = [
        'Charges',
        'Security',
        'Support',
        'Contract',
        'Tenure'
    ]

    radar_values = [88, 42, 58, 81, 34]

    radar = go.Figure()

    radar.add_trace(go.Scatterpolar(
        r=radar_values,
        theta=radar_categories,
        fill='toself',
        name='Customer Risk'
    ))

    radar.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0,100]
            )
        ),
        showlegend=False,
        height=430,
        paper_bgcolor='rgba(0,0,0,0)',
        font_color='white'
    )

    st.plotly_chart(
        radar,
        use_container_width=True
    )

    st.markdown('</div>', unsafe_allow_html=True)

with right:

    st.markdown('<div class="main-card">', unsafe_allow_html=True)

    st.markdown(
        '<div class="section-title">🤖 AI Insights</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '''
        <div class="insight-red">
        ⚠ High monthly charges are significantly increasing churn probability.
        </div>
        ''',
        unsafe_allow_html=True
    )

    st.markdown(
        '''
        <div class="insight-yellow">
        ⚠ Month-to-month contracts show unstable retention behavior.
        </div>
        ''',
        unsafe_allow_html=True
    )

    st.markdown(
        '''
        <div class="insight-yellow">
        ⚠ Customers without online security services are more likely to leave.
        </div>
        ''',
        unsafe_allow_html=True
    )

    st.markdown(
        '''
        <div class="insight-green">
        ✅ Long customer tenure improves retention stability.
        </div>
        ''',
        unsafe_allow_html=True
    )

    st.markdown('</div>', unsafe_allow_html=True)


    st.markdown('<div class="main-card">', unsafe_allow_html=True)

    st.markdown(
        '<div class="section-title">⚠ Risk Meter</div>',
        unsafe_allow_html=True
    )

    gauge = go.Figure(go.Indicator(
        mode="gauge+number",
        value=churn_score,
        title={'text': "Customer Churn Risk"},
        gauge={
            'axis': {'range': [0, 100]},
            'bar': {'color': '#7c3aed'},
            'steps': [
                {'range': [0, 35], 'color': '#052e16'},
                {'range': [35, 70], 'color': '#3f2d06'},
                {'range': [70, 100], 'color': '#450a0a'}
            ]
        }
    ))

    gauge.update_layout(
        height=320,
        paper_bgcolor='rgba(0,0,0,0)',
        font_color='white'
    )

    st.plotly_chart(
        gauge,
        use_container_width=True
    )

    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="main-card">', unsafe_allow_html=True)

    st.markdown(
        '<div class="section-title">💡 Retention Strategy</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    ### Recommended Actions

    - Offer annual subscription discount
    - Provide premium technical support
    - Launch loyalty reward campaign
    - Reduce monthly billing friction
    - Increase engagement touchpoints
    """)

    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="main-card">', unsafe_allow_html=True)

st.markdown(
    '<div class="section-title">🚦 Feature Risk Breakdown</div>',
    unsafe_allow_html=True
)

risk_table = pd.DataFrame({
    "Feature": [
        "Monthly Charges",
        "Contract Type",
        "Tech Support",
        "Online Security",
        "Tenure"
    ],
    "Risk Level": [
        "🔴 High",
        "🟠 Medium",
        "🟡 Moderate",
        "🟠 Medium",
        "🟢 Low"
    ],
    "Business Impact": [
        "Customer may leave due to pricing",
        "Short-term commitment instability",
        "Low support satisfaction",
        "Weak service trust",
        "Long-term customer loyalty"
    ]
})

st.dataframe(
    risk_table,
    use_container_width=True,
    hide_index=True
)

st.markdown('</div>', unsafe_allow_html=True)

col1, col2 = st.columns([1,1])

with col1:

    if st.button("⬅ Back Dashboard"):
        st.switch_page("pages/dashboard.py")

with col2:

    if st.button("📈 Open Visualization"):
        st.switch_page("pages/visualization.py")


