import streamlit as st
import pandas as pd
import plotly.express as px

st.title("OVERVIEW")
df = pd.read_csv("cleaned_ai_student_impact_dataset.csv.csv")
#st.dataframe(df)

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

c1,c2,c3,c4 = st.columns(4)
with c1:
    st.metric("Total Students" , df["Student_ID"].nunique())
with c2:
    st.metric("Avg Pre GPA" , df["Pre_Semester_GPA"].mean())
with c3:
    st.metric("Avg Post GPA" , df["Post_Semester_GPA"].mean())
with c4:
    st.metric("Avg Weekly AI Hours" , df["Weekly_GenAI_Hours"].mean())

c5,c6,c7,c8 = st.columns(4)
with c5:
     st.metric("Avg Traditional Study Hours" , df["Traditional_Study_Hours"].mean())
with c6:
    st.metric("Avg Skill Retention" , df["Skill_Retention_Score"].mean())
with c7:
    st.metric("Avg AI Dependency" , df["Perceived_AI_Dependency"].mean()) 

paid_subscription_percent = (df["Paid_Subscription"].mean() * 100)
with c8 :
  st.metric(label="💳 Paid Subscription %",value=f"{paid_subscription_percent:.1f}%")

plot_bg = "#181818"
paper_bg = "#181818"
font_color = "white"


fig1 = px.pie(
    df,
    names="Major_Category",
    title="Students by Major",
    hole=0.55,
    color_discrete_sequence=px.colors.qualitative.Bold
)

fig1.update_layout(
    plot_bgcolor=plot_bg,
    paper_bgcolor=paper_bg,
    font_color=font_color
)
st.plotly_chart(fig1)

fig2 = px.pie(
    df,
    names="Paid_Subscription",
    title="Paid vs Free Users",
    hole=0.55,
    color_discrete_sequence=["#00C853", "#E53935"]
)

fig2.update_layout(
    plot_bgcolor=plot_bg,
    paper_bgcolor=paper_bg,
    font_color=font_color
)

st.plotly_chart(fig2)



fig3 = px.histogram(
    df,
    x="Weekly_GenAI_Hours",
    nbins=15,
    title="Distribution of Weekly AI Hours"
)

fig3.update_layout(
    template="plotly_dark",
    paper_bgcolor="#181818",
    plot_bgcolor="#181818",
    font_color="white",
    xaxis_title="Weekly AI Hours",
    yaxis_title="Number of Students",
    title_x=0.5
)

st.plotly_chart(fig3)

fig4 = px.box(
    df,
    x="Major_Category",
    y="Post_Semester_GPA",
    color="Major_Category",
    title="Post GPA by Major"
)

fig4.update_layout(
    plot_bgcolor=plot_bg,
    paper_bgcolor=paper_bg,
    font_color=font_color,
    showlegend=False
)

st.plotly_chart(fig4, use_container_width=True)

Avg_Post_GPA_by_Major = (
    df.groupby("Major_Category")["Post_Semester_GPA"]
      .mean()
      .reset_index()
)

fig5 = px.bar(
    Avg_Post_GPA_by_Major,
    x="Major_Category",
    y="Post_Semester_GPA",
    title="Average Post GPA by Major",
    color="Post_Semester_GPA",
    color_continuous_scale="Reds"
)

fig5.update_layout(
    plot_bgcolor=plot_bg,
    paper_bgcolor=paper_bg,
    font_color=font_color
)

st.plotly_chart(fig5)

fig6 = px.treemap(
    df,
    path=["Major_Category", "Year_of_Study"],
    title="Students by Major & Year",
    color="Weekly_GenAI_Hours",
    color_continuous_scale="Reds"
)

fig6.update_layout(
    plot_bgcolor=plot_bg,
    paper_bgcolor=paper_bg,
    font_color=font_color
)

st.plotly_chart(fig6)


st.subheader("📌  Overview Dashboard Insights")



st.info("""
👨‍🎓 **Total Students:** Displays the total number of unique students included in the analysis.

🎓 **Average Pre GPA:** Represents students' average GPA before using AI tools.

📈 **Average Post GPA:** Shows the average GPA after AI adoption to evaluate its academic impact.

🤖 **Average Weekly AI Hours:** Indicates the average time students spend using AI every week.

📚 **Average Traditional Study Hours:** Shows the average time students spend on traditional studying.

🧠 **Average Skill Retention:** Reflects how well students retain knowledge while using AI.

🔗 **Average AI Dependency:** Indicates students' reliance on AI tools for academic work.

💳 **Paid Subscription %:** Shows the percentage of students using paid AI tools.
""")

st.success(""" 📊 Students by Major

• Shows the distribution of students across different academic majors.

• Helps identify which majors have the highest student participation.
""")

st.success("""💳 Paid vs Free Users

• Compares students using paid AI tools with those using free versions.

• Helps understand AI subscription adoption among students.
""")

st.success(""" 📈 Distribution of Weekly AI Hours

• Shows how students' AI usage is distributed.

• Identifies whether most students are light, moderate, or heavy AI users.
""")

st.success(""" 📦 Post GPA by Major

• Compares GPA distributions across different majors.

• Highlights variations and possible outliers.
""")

st.success(""" 📊 Average Post GPA by Major

• Compares average GPA among different majors.

• Helps identify majors with relatively higher or lower academic performance.
""")

st.success(""" 🌳 Students by Major & Year

• Displays the hierarchical distribution of students by major and year.

• Color intensity represents average weekly AI usage.
""")

st.markdown("---")
st.subheader("📌 Overall Dashboard Summary")

st.info("""
This dashboard provides a comprehensive overview of students' AI usage, academic performance,
study habits, skill retention, and AI dependency.

Key findings include:
- AI adoption among students.
- Comparison of GPA before and after AI usage.
- Distribution of AI usage across students.
- Academic performance across majors.
- Student distribution by major and year of study.
- AI subscription trends.
""")