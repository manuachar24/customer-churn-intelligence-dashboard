
import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

st.set_page_config(
    page_title="Visualization",
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

.card {
    background: rgba(17,24,39,0.75);
    border-radius: 24px;
    padding: 24px;
    border: 1px solid rgba(255,255,255,0.08);
    margin-bottom: 24px;
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

try:

    df = pd.read_excel(
        r"C:\Users\LENOVO\OneDrive\Desktop\DATASETS\customer-churn-prediction\Telco_customer_churn.xlsx"
    )

except Exception as e:

    st.error(f"Dataset Error: {e}")
    st.stop()

st.markdown("""
<div class="hero">
    <h1>📈 Customer Analytics</h1>
    <p>Interactive business intelligence and customer behavior visualization.</p>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="card">', unsafe_allow_html=True)

st.subheader("📊 Churn Distribution")

fig1 = px.histogram(
    df,
    x="Churn Label",
    color="Churn Label"
)

fig1.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    font_color='white'
)

st.plotly_chart(
    fig1,
    use_container_width=True
)

st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="card">', unsafe_allow_html=True)

st.subheader("💰 Monthly Charges vs Churn")

fig2 = px.box(
    df,
    x="Churn Label",
    y="Monthly Charges",
    color="Churn Label"
)

fig2.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    font_color='white'
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

st.markdown('</div>', unsafe_allow_html=True)

try:

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("👥 Customer Segmentation")

    features = [
        'Tenure Months',
        'Monthly Charges',
        'Total Charges'
    ]

    X = df[features].copy()

    X['Total Charges'] = pd.to_numeric(
        X['Total Charges'],
        errors='coerce'
    )

    X = X.fillna(0)

    scaler = StandardScaler()

    X_scaled = scaler.fit_transform(X)

    kmeans = KMeans(
        n_clusters=4,
        random_state=42,
        n_init=10
    )

    clusters = kmeans.fit_predict(X_scaled)

    pca = PCA(n_components=2)

    components = pca.fit_transform(X_scaled)

    pca_df = pd.DataFrame({
        'PCA1': components[:,0],
        'PCA2': components[:,1],
        'Cluster': clusters.astype(str)
    })

    fig3 = px.scatter(
        pca_df,
        x='PCA1',
        y='PCA2',
        color='Cluster'
    )

    fig3.update_layout(
        height=600,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font_color='white'
    )

    st.plotly_chart(
        fig3,
        use_container_width=True
    )

    st.markdown('</div>', unsafe_allow_html=True)

except Exception as e:

    st.error(f"Segmentation Error: {e}")


c1,c2 = st.columns(2)

with c1:

    if st.button("⬅ Dashboard"):
        st.switch_page("pages/dashboard.py")

with c2:

    if st.button("🧠 Explainable AI"):
        st.switch_page("pages/explainable_ai.py")
