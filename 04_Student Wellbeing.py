import streamlit as st
import pandas as pd
import plotly.express as px
st.title("STUDENT WELLBEING")
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

c1 , c2 , c3, c4 = st.columns(4)
with c1 : 
    st.metric("Burnout" , df["Burnout_Risk_Level"].nunique())
with c2 :
    st.metric("Avg Anxiety" , df["Anxiety_Level_During_Exams"].mean())

high=((df["Burnout_Risk_Level"]=="High").mean()*100)

with c3 :
   st.metric("High Burnout %",f"{high:.1f}%")
with c4 :
    st.metric("Avg Dependency" , df["Perceived_AI_Dependency"].mean())

    
burnout_count = df["Burnout_Risk_Level"].value_counts().reset_index()
burnout_count.columns = ["Burnout Risk", "Count"]

fig1 = px.pie( burnout_count, names="Burnout Risk", values="Count", hole=0.6, color="Burnout Risk", title= "Burnout Risk Level" ,
        color_discrete_map={
        "Low": "#2ECC71",
        "Medium": "#F1C40F",
        "High": "#E74C3C"
    }
)

fig1.update_layout(
    template="plotly_dark",
    paper_bgcolor="#181818",
    font_color="white"
)

st.plotly_chart(fig1)

fig2 = px.sunburst(
    df,
    path=["Anxiety_Level_During_Exams"],
    title="Anxiety Distribution",
    color="Anxiety_Level_During_Exams",
    color_discrete_sequence=px.colors.sequential.Reds
)

fig2.update_layout(
    template="plotly_dark",
    paper_bgcolor="#181818",
    font_color="white"
)

st.plotly_chart(fig2)

plot_bg = "#181818"
paper_bg = "#181818"
font_color = "white"

fig3 = px.scatter(
    df,
    x="Perceived_AI_Dependency",
    y="Burnout_Risk_Level",
    color="Weekly_GenAI_Hours",
    size="Tool_Diversity",
    hover_name="Major_Category",
    hover_data=[
        "Year_of_Study",
        "Primary_Use_Case",
        "Prompt_Engineering_Skill"
    ],
    color_continuous_scale=["#4E79A7", "#F28E2B"],
    title="AI Dependency vs Burnout Risk"
)

fig3.update_layout(
    template="plotly_dark",
    paper_bgcolor="#181818",
    font_color="white"
)

st.plotly_chart(fig3)

fig4 = px.scatter(
    df,
    x="Traditional_Study_Hours",
    y="Burnout_Risk_Level",
    color="Post_Semester_GPA",
    size="Weekly_GenAI_Hours",
    hover_name="Major_Category",
    hover_data=[
        "Year_of_Study",
        "Primary_Use_Case",
        "Prompt_Engineering_Skill"
    ],
    color_continuous_scale=["#4E79A7", "#F28E2B"],
    title="Study Hours vs Burnout Risk"
)

fig4.update_layout(
    template="plotly_dark",
    paper_bgcolor="#181818",
    font_color="white"
)

st.plotly_chart(fig4)

fig5 = px.box(
    df,
    x="Burnout_Risk_Level",
    y="Skill_Retention_Score",
    color="Burnout_Risk_Level",
    color_discrete_sequence=[
        "#4E79A7",
        "#F28E2B",
        "#59A14F"
    ],
    title="Skill Retention by Burnout Risk"
)

fig5.update_layout(
    template="plotly_dark",
    paper_bgcolor="#181818",
    font_color="white"
)

st.plotly_chart(fig5)

fig6 = px.sunburst(
    df,
    path=["Year_of_Study", "Burnout_Risk_Level"],
    title="Year of Study → Burnout_Risk_Level",
    color="Burnout_Risk_Level",
    color_discrete_sequence=px.colors.qualitative.Set2
)

fig6.update_layout(
    plot_bgcolor="#181818",
    paper_bgcolor="#181818",
    font_color="white",
    title_x=0.5,
    margin=dict(t=50, l=20, r=20, b=20)
)

st.plotly_chart(fig6)


st.subheader("📌 Dashboard Insights")

st.info("""
🔥 Burnout Levels: Displays the number of burnout risk categories (Low, Medium, High).

😟 Average Anxiety: Shows the average anxiety level experienced by students during exams.

📈 High Burnout %: Indicates the percentage of students classified as having high burnout risk.

🤖 Average AI Dependency: Represents the average reliance on AI tools among students.
""")

st.success(""" 🔥 Burnout Risk Level

• Shows the distribution of students across Low, Medium, and High burnout risk.

• Helps identify the overall mental well-being of the student population.
""")

st.success(""" 😟 Anxiety Distribution

• Displays how students are distributed across different anxiety levels during exams.

• Helps understand the prevalence of exam-related anxiety.
""")

st.success(""" 🤖 AI Dependency vs Burnout Risk

• Examines the relationship between AI dependency and burnout risk.

• Bubble size represents tool diversity, while color indicates weekly AI usage.

• Helps identify whether students with higher AI dependency also experience greater burnout.
""")

st.success(""" 📚 Study Hours vs Burnout Risk

• Shows how traditional study hours relate to burnout risk.

• Bubble size represents weekly AI usage, and color represents post-semester GPA.

• Helps explore whether study habits are associated with burnout levels.
""")

st.success(""" 🧠 Skill Retention by Burnout Risk

• Compares skill retention scores across burnout risk levels.

• Highlights differences in median performance, variability, and outliers.
""")

st.success(""" 🎓 Year of Study → Burnout Risk

• Visualizes burnout risk across different academic years.

• Helps identify which year of study has the highest proportion of students experiencing burnout.
""")

st.markdown("---")
st.subheader("📌 Overall Dashboard Summary")

st.info("""
This dashboard analyzes students' mental well-being alongside AI usage and academic factors.

Key insights include:
• Distribution of burnout risk and exam anxiety.
• Relationship between AI dependency and burnout.
• Impact of traditional study hours on burnout levels.
• Comparison of skill retention across burnout categories.
• Burnout trends across different years of study.

These visualizations help identify patterns between AI usage, academic performance, and students' mental health.
""")