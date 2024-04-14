import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Subhajit Portfolio", layout="wide")

def about_me():
    st.title("About Me")

    st.write('''Hi Folks :wave:, My name is **Subhajit Guha Thakurta**. I am a Data Science Engineer with over 2 years of experience at Infosys, where I have been deeply involved in the realm of data engineering. My expertise lies in **crafting robust data pipelines, optimizing SQL queries, and implementing diverse data retrieval techniques**. Currently, I am immersed in the fascinating world of **Large Language Models (LLMs)**, leveraging them to analyze data and drive strategic decision-making processes.

Driven by a passion for creating functional and user-friendly data science applications, I am dedicated to pushing the boundaries of what is possible with data. My journey in the field has been marked by a commitment to excellence and a constant pursuit of innovative solutions that make a tangible impact.

I look forward to connecting with like-minded professionals and contributing to the ever-evolving landscape of data science.''')

    st.markdown("# **Education**")

    data = {
        'Degree': ['M.Tech', 'B.Tech'],
        'College/University': ['Kalyani Government Engineering College', 'Guru Nanak Institute Of Technology'],
        'Passing Year': [2021,2019],
        'Result': ['CGPA:8.67', 'CGPA:7.75']
    }
    df = pd.DataFrame(data)
    st.table(df)

def work():
    st.title("Work @ Infosys")

    st.markdown("""
    <ul>
      <li>Analyzing data by using OpenAI and Client Models, extracting valuable insights, and informing strategic decision-making.</li>
      <li>Built robust and efficient data pipelines, ensuring seamless flow and integration of data.</li>
      <li>Developed and implemented different function techniques, enabling swift and effortless retrieval of data from the database.</li>
      <li>Enhanced SlackBot functionality by incorporating diverse use cases along with fine-tuning Large Language Models if possible, enhancing convenience for clients.</li>
    </ul>
    """, unsafe_allow_html=True)

    st.markdown("# **Tools**")
    labels = ['PostGres', 'Oracle', 'Snowflake', 'CI/CD Pipeline', 'AWS S3', 'Streamlit', 'Hugging Face', 'LLMs', 'Milvus-Vector DB']
    values = [5, 8, 30, 15, 5, 15, 4, 10, 8]

    fig = px.pie(names=labels, values=values)
    st.plotly_chart(fig)

    st.markdown("# **Languages**")

    categories = ['Python', 'SQL', 'Scala', 'Spark']
    values = [50, 35, 5, 10]

    fig = px.bar(x=categories, y=values, labels={'x': 'Categories', 'y': 'Values'})
    st.plotly_chart(fig)

def project():
    st.title("Projects :computer:")

    project_1 = st.container()
    with project_1:
        st.header("**ANTON-2.0**")
        st.write('''A Python script that works like an AI assistant to find CPU details,email,
Wikipedia-google-youtube search, text-to-speech, etc. on one click.''')
        st.write("Link to project: https://github.com/SubhajitGT/ANTON-2.0")
    project_2 = st.container()
    with project_2:
        st.header("**Stock Analysis**")
        st.write('''Predicting stock price based on Yahoo finaince historical data.''')
        st.write("Project Live at: https://stock-market-forecast.streamlit.app/")
    project_3 = st.container()
    with project_3:
        st.header("**SELF-DRIVING CAR**")
        st.write('''Predict steering angle and display on the front camera of a car data,this
project works on Convolutional Neural Network-Regression Model.''')
        st.write("Link to project: https://github.com/SubhajitGT/Self_Driving_Car")
    project_4 = st.container()
    with project_4:
        st.header("**WORLD CUP TRACKER**")
        st.write('''Cricket and Soccer world cup statistics till now in one place.''')
        st.write("Link to project: https://github.com/SubhajitGT/World-Cup-Stats-Checker")

    st.write("**You can find, some more interesting projects from here**:  https://github.com/SubhajitGT?tab=repositories")

def contact():
    st.title("**Get in touch :lower_left_paintbrush:**")
    st.write("**Email :e-mail:** : Subhajitguha79@gmail.com")
    st.write("**Mobile No. :calling:** : +91 8621954638")
    st.write("**LinkedIn Profile** : https://www.linkedin.com/in/subhajit-guha-thakurta-229199126/")
    st.write("**GitHub Profile** : https://github.com/SubhajitGT")

with st.sidebar:
    st.sidebar.image("pc.jpg", use_column_width=True)
    st.write("Data Science Engineer @Infosys Ltd.")

pages = {
        "About Me": about_me,
        "Experience": work,
        "Project": project,
        "Contact": contact,
    }

selected_page = st.sidebar.selectbox("**Welcome :raised_hand_with_fingers_splayed:**", list(pages.keys()))
pages[selected_page]()


