import streamlit as st
import pandas as pd


st.set_page_config(page_title="AI Impact on Students Dashboard", page_icon="📊",
    layout="wide"
)

st.title("📊 AI Impact on Students Dashboard")
df = pd.read_csv("cleaned_ai_student_impact_dataset.csv.csv")
st.dataframe(df)

st.markdown("""
<style>

/* Main Background */
.stApp{
    background: linear-gradient(
        135deg,
        #0b0b0b 0%,
        #111111 25%,
        #1a1a1a 50%,
        #111111 75%,
        #080808 100%
    );
}

/* Sidebar */
section[data-testid="stSidebar"]{
    background: #101010;
}

/* Metric Cards */
[data-testid="stMetric"]{
    background: #181818;
    border: 1px solid #2b2b2b;
    border-left: 5px solid #c1121f;
    border-radius: 15px;
    padding: 18px;
    box-shadow: 0 8px 25px rgba(0,0,0,0.5);
    transition: all .3s ease;
}

[data-testid="stMetric"]:hover{
    transform: translateY(-5px);
    border-left: 5px solid #ff3b3b;
    box-shadow: 0 12px 30px rgba(255,0,0,.2);
}

/* Metric Label */
[data-testid="stMetricLabel"]{
    color: #cfcfcf;
    font-size: 15px;
    font-weight: 600;
}

/* Metric Value */
[data-testid="stMetricValue"]{
    color: white;
    font-size: 34px;
    font-weight: 700;
}

/* Delta */
[data-testid="stMetricDelta"]{
    color: #2ecc71;
}

/* Headings */
h1,h2,h3{
    color:white;
}

/* Divider */
hr{
    border-color:#2b2b2b;
}

</style>
""", unsafe_allow_html=True)

