import streamlit as st
import pandas as pd
import plotly.express as px

st.header("🤖 AI Usage Analysis")
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

c1,c2,c3,c4=st.columns(4)

with c1:
   st.metric("Avg Tool Diversity",df["Tool_Diversity"].mean())

with c2:
   st.metric("Avg AI Hours",df["Weekly_GenAI_Hours"].mean())

with c3:
   st.metric("Avg Dependency",df["Perceived_AI_Dependency"].mean())

with c4: 
   st.metric("Paid Users",df["Paid_Subscription"].sum())

use_case = (
    df["Primary_Use_Case"]
    .value_counts()
    .reset_index()
)
use_case.columns = ["Primary_Use_Case", "Count"]

fig1 = px.bar(
    use_case,
    y="Primary_Use_Case",
    x="Count",
    orientation="h",
    color="Count",
    color_continuous_scale="Reds",
    title="Primary Use Case Distribution"
)

fig1.update_layout(
    plot_bgcolor="#181818",
    paper_bgcolor="#181818",
    font_color="white"
)

st.plotly_chart(fig1)

fig2 = px.sunburst(
    df,
    path=["Year_of_Study", "Prompt_Engineering_Skill"],
    title="Prompt Skill by Year"
)

fig2.update_layout(
    plot_bgcolor="#181818",
    paper_bgcolor="#181818",
    font_color="white"
)
st.plotly_chart(fig2)

fig3 = px.box(
    df,
    x="Prompt_Engineering_Skill",
    y="Tool_Diversity",
    color="Prompt_Engineering_Skill",
    color_discrete_sequence=px.colors.qualitative.Bold
)

fig3.update_layout(
    plot_bgcolor="#181818",
    paper_bgcolor="#181818",
    font_color="white"
)
st.plotly_chart(fig3)

df["GenAi_Category"] = pd.cut(df["Weekly_GenAI_Hours"] , bins= 4 , labels= ["1-12" , "12-24", "24-36" , "36-48" ])

fig4 = px.bar(
    df,
    x="GenAi_Category",
    y="Weekly_GenAI_Hours",
    color="Weekly_GenAI_Hours",
    color_continuous_scale=[
        "#4E79A7",
        "#F28E2B",
        "#59A14F",
        "#E15759"
    ],
    title="Weekly GenAI Hours"
)

fig4.update_layout(
    plot_bgcolor="#181818",
    paper_bgcolor="#181818",
    font_color="white"
)
st.plotly_chart(fig4)

fig5 = px.icicle(
    df,
    path=["Major_Category", "Prompt_Engineering_Skill"],
    title="Major Category → Prompt Engineering Skill",
    color="Major_Category",
    color_discrete_sequence=px.colors.qualitative.Set3
)

fig5.update_layout(
    plot_bgcolor="#181818",
    paper_bgcolor="#181818",
    font_color="white",
    title_x=0.5,
    margin=dict(t=50, l=25, r=25, b=25)
)

st.plotly_chart(fig5)

line_df = (
    df.groupby(["Weekly_GenAI_Hours", "Paid_Subscription"], as_index=False)
      .agg({
          "Perceived_AI_Dependency": "mean",
          "Tool_Diversity": "mean"
      })
)

fig6 = px.line(
    line_df,
    x="Weekly_GenAI_Hours",
    y="Perceived_AI_Dependency",
    color="Paid_Subscription",
    markers=True,
    hover_data=["Tool_Diversity"],
    color_discrete_map={
        "Yes": "#00CC96",
        "No": "#EF553B"
    },
    title="Average AI Hours vs AI Dependency (Paid vs Free)"
)

fig6.update_layout(
    plot_bgcolor="#181818",
    paper_bgcolor="#181818",
    font_color="white",
    title_x=0.5,
    xaxis_title="Weekly AI Hours",
    yaxis_title="Average AI Dependency",
    legend_title="Paid Subscription"
)

st.plotly_chart(fig6)


st.subheader("📌 AI usage Overall Dashboard Summary")

st.info("""
🔧 Avg Tool Diversity: Shows the average number of AI tools used by each student.

🤖 Avg AI Hours: Indicates the average weekly time students spend using AI tools.

🔗 Avg Dependency: Represents the average level of students' dependence on AI.

💳 Paid Users: Displays the total number of students using paid AI subscriptions.
""")

st.success(""" 📊 Primary Use Case Distribution

• Shows the most common purposes for which students use AI.

• Helps identify whether AI is mainly used for coding, writing, research, studying, or other tasks.
""")

st.success(""" 🌞 Prompt Skill by Year

• Displays the distribution of prompt engineering skill levels across different academic years.

• Helps identify which year has the highest concentration of advanced prompt engineering skills.
""")

st.success(""" 📦 Tool Diversity by Prompt Engineering Skill

• Compares the number of AI tools used by students with different prompt engineering skill levels.

• Shows the median, spread, and outliers for each skill group.
""")

st.success(""" 📊 Weekly GenAI Hours

• Groups students into AI usage categories based on weekly hours.

• Helps compare AI usage intensity across different usage ranges.
""")

st.success(""" 🌳 Major Category → Prompt Engineering Skill

• Displays the hierarchical relationship between academic majors and prompt engineering skills.

• Helps identify which majors have more students with higher prompt engineering proficiency.
""")

st.success(""" 📈 Average AI Hours vs AI Dependency

• Shows how students' average AI dependency changes as weekly AI usage increases.

• Compares dependency trends between paid and free AI users.
""")

st.markdown("---")
st.subheader("📌 Overall Dashboard Summary")

st.info("""
This dashboard analyzes students' AI usage behavior, prompt engineering skills,
tool diversity, and AI dependency.

Key insights include:
• Students' primary purposes for using AI.
• Prompt engineering skill distribution across academic years.
• Relationship between AI tool diversity and prompt engineering skills.
• Weekly AI usage categories.
• Hierarchical distribution of majors and prompt engineering skills.
• Comparison of AI dependency trends between paid and free AI users.
""")