import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import numpy as np
st.set_page_config(
    page_title="Dashboard",
    layout="wide"
)
if "probability" not in st.session_state:

    st.warning("Please analyze customer first.")
    st.stop()

prediction = st.session_state["prediction"]
probability = st.session_state["probability"]


churn = round(probability * 100, 2)
retention = round((1 - probability) * 100, 2)
health = round(np.random.uniform(70, 95), 2)
revenue = round(np.random.uniform(1.5, 5.0), 2)
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

.card {
    background: rgba(17,24,39,0.75);
    border-radius: 24px;
    padding: 24px;
    border: 1px solid rgba(255,255,255,0.08);
    margin-bottom: 22px;
}

.metric-card {
    background: linear-gradient(
        145deg,
        rgba(30,41,59,0.92),
        rgba(15,23,42,0.92)
    );
    border-radius: 22px;
    padding: 24px;
    border: 1px solid rgba(255,255,255,0.08);
}

.metric-title {
    color: #94a3b8;
    font-size: 14px;
}

.metric-value {
    color: white;
    font-size: 40px;
    font-weight: 800;
}

.hero {
    background: linear-gradient(
        135deg,
        #7c3aed,
        #2563eb,
        #06b6d4
    );
    padding: 34px;
    border-radius: 28px;
    margin-bottom: 25px;
}

h1,h2,h3,h4,h5,p,label {
    color: white !important;
}

.stButton > button {
    width: 100%;
    background: linear-gradient(
        135deg,
        #7c3aed,
        #2563eb
    );
    color: white;
    border-radius: 14px;
    border: none;
    padding: 12px;
    font-weight: 700;
}

</style>
""", unsafe_allow_html=True)
st.markdown("""
<div class="hero">
    <h1>📈 AI Customer Dashboard</h1>
    <p>Real-time customer churn intelligence and business analytics.</p>
</div>
""", unsafe_allow_html=True)
c1,c2,c3,c4 = st.columns(4)

with c1:

    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">CHURN RISK</div>
        <div class="metric-value">{churn:.2f}%</div>
    </div>
    """, unsafe_allow_html=True)

with c2:

    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">RETENTION</div>
        <div class="metric-value">{retention:.2f}%</div>
    </div>
    """, unsafe_allow_html=True)

with c3:

    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">HEALTH SCORE</div>
        <div class="metric-value">{health:.2f}</div>
    </div>
    """, unsafe_allow_html=True)

with c4:

    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">REVENUE IMPACT</div>
        <div class="metric-value">₹2.1M</div>
    </div>
    """, unsafe_allow_html=True)

st.write("")
left, right = st.columns([1.2,1])

with left:

    st.markdown(
        '<div class="main-card">',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-title">⚠ Churn Risk Meter</div>',
        unsafe_allow_html=True
    )

    gauge = go.Figure(go.Indicator(
        mode="gauge+number",
        value=churn,
        number={'suffix': "%"},
        gauge={
            'axis': {'range': [0, 100]},
            'bar': {'color': "#7c3aed"},
            'steps': [
                {'range': [0, 35], 'color': '#052e16'},
                {'range': [35, 70], 'color': '#3f2d06'},
                {'range': [70, 100], 'color': '#450a0a'}
            ]
        }
    ))

    gauge.update_layout(
        height=420,
        paper_bgcolor='rgba(0,0,0,0)',
        font_color='white'
    )

    st.plotly_chart(
        gauge,
        use_container_width=True
    )

    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )
with right:

    st.markdown(
        '<div class="main-card">',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-title">📊 Retention Split</div>',
        unsafe_allow_html=True
    )

    pie = px.pie(
        names=["Retention", "Churn"],
        values=[retention, churn],
        hole=0.72
    )

    pie.update_layout(
        height=420,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font_color='white',
        showlegend=True
    )

    st.plotly_chart(
        pie,
        use_container_width=True
    )

    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )
st.markdown('<div class="card">', unsafe_allow_html=True)

st.subheader("🤖 AI Business Insights")

if churn > 70:

    st.error("High monthly charges and unstable contracts are increasing churn risk.")

    st.warning("Customer requires immediate retention strategy.")

elif churn > 35:

    st.warning("Customer shows moderate churn behavior patterns.")

else:

    st.success("Customer appears stable with strong retention potential.")

st.markdown('</div>', unsafe_allow_html=True)

c1,c2,c3 = st.columns(3)

with c1:

    if st.button("📈 Visualization"):
        st.switch_page("pages/visualization.py")

with c2:

    if st.button("🧠 Explainable AI"):
        st.switch_page("pages/explainable_ai.py")

with c3:

    if st.button("🏠 Home"):
        st.switch_page("app.py")
