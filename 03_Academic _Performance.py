import streamlit as st
import pandas as pd
import plotly.express as px

st.header("🤖 Academic performance ")
df = pd.read_csv("cleaned_ai_student_impact_dataset.csv.csv")
# st.dataframe(df)
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

GPA_Improvement  = df["GPA Improvement"] = (df["Post_Semester_GPA"]-df["Pre_Semester_GPA"])

c1,c2,c3,c4=st.columns(4)

with c1:
   st.metric("Highest GPA",df["Post_Semester_GPA"].max())

with c2:
   st.metric("Lowest GPA",df["Post_Semester_GPA"].min())

with c3 :
    st.metric("Avg Improvement",df["GPA Improvement"].mean())

with c4:
    st.metric("Highest Skill Retention",df["Skill_Retention_Score"].max())


plot_bg = "#181818"
paper_bg = "#181818"
font_color = "white"

fig1 = px.histogram(
    df,
    x="Weekly_GenAI_Hours",
    nbins=15,
    color_discrete_sequence=["#00CC96"],
    title="Distribution of Weekly GenAI Hours"
)

fig1.update_layout(
    plot_bgcolor="#181818",
    paper_bgcolor="#181818",
    font_color="white",
    title_x=0.5,
    xaxis_title="Weekly GenAI Hours",
    yaxis_title="Number of Students",
    bargap=0.05
)

st.plotly_chart(fig1)

fig2 = px.histogram(
    df,
    x="Traditional_Study_Hours",
    nbins=15,
    color_discrete_sequence=["#00CC96"],
    title="Distribution of Study Hours per Week"
)

fig2.update_layout(
    plot_bgcolor="#181818",
    paper_bgcolor="#181818",
    font_color="white",
    title_x=0.5,
    xaxis_title="Traditional_Study_Hours",
    yaxis_title="Number of Students"
)

st.plotly_chart(fig2)

Avg_GPA_by_Major = df.groupby("Major_Category")[
    ["Pre_Semester_GPA", "Post_Semester_GPA"]
].mean().reset_index()

fig3 = px.bar(
    Avg_GPA_by_Major,
    x="Major_Category",
    y=["Pre_Semester_GPA", "Post_Semester_GPA"],
    barmode="group",
    color_discrete_sequence=["#4E79A7", "#F28E2B"],
    title="Average GPA by Major"
)
fig3.update_layout(
    plot_bgcolor="#181818",
    paper_bgcolor="#181818",
    font_color="white"
)
st.plotly_chart(fig3)

fig4 = px.violin(
    df,
    x="Prompt_Engineering_Skill",
    y="Skill_Retention_Score",
    color="Prompt_Engineering_Skill",
    box=True,
    color_discrete_sequence=px.colors.qualitative.Bold,
    title="Skill Retention by Prompt Engineering Skill"
)

fig4.update_layout(
    plot_bgcolor="#181818",
    paper_bgcolor="#181818",
    font_color="white"
)

st.plotly_chart(fig4)

major_counts = df["Major_Category"].value_counts().reset_index()
major_counts.columns = ["Major", "Students"]

fig5 = px.bar(
    major_counts,
    x="Major",
    y="Students",
    color="Major",
    color_discrete_sequence=[
        "#4E79A7",
        "#F28E2B",
        "#59A14F",
        "#E15759",
        "#B07AA1"
    ],
    title="Students by Major"
)

fig5.update_layout(
    plot_bgcolor="#181818",
    paper_bgcolor="#181818",
    font_color="white"
)
st.plotly_chart(fig5)


st.subheader("📌 Dashboard Insights")

st.info("""
🏆 Highest GPA: Displays the highest post-semester GPA achieved by any student.

📉 Lowest GPA: Displays the lowest post-semester GPA recorded.

📈 Average GPA Improvement: Shows the average improvement in GPA after AI adoption.

🧠 Highest Skill Retention: Indicates the maximum skill retention score among students.
""")

st.success(""" 📊 Distribution of Weekly GenAI Hours

• Shows how frequently students use GenAI each week.

• Helps identify whether most students are light, moderate, or heavy AI users.
""")

st.success("""📚 Distribution of Traditional Study Hours

• Displays how many hours students spend on traditional studying each week.

• Helps understand overall study habits and identify the most common study-hour range.
""")

st.success(""" 📈 Average GPA by Major

• Compares the average pre-semester GPA and post-semester GPA across different majors.

• Helps evaluate how academic performance changed after AI adoption for each major.
""")

st.success(""" 🎻 Skill Retention by Prompt Engineering Skill

• Compares skill retention scores across different prompt engineering skill levels.

• Shows the distribution, median, and variability of skill retention within each group.
""")

st.success(""" 🎓 Students by Major

• Displays the number of students in each academic major.

• Helps identify which majors have the highest representation in the dataset.
""")

st.markdown("---")
st.subheader("📌 Overall Dashboard Summary")

st.info("""
This dashboard focuses on academic performance, study habits, and skill retention.

Key insights include:
• Comparison of pre-semester and post-semester GPA across majors.
• Distribution of weekly AI usage and traditional study hours.
• Relationship between prompt engineering skills and skill retention.
• Student distribution across academic majors.
• Overall improvement in academic performance after AI adoption.
""")