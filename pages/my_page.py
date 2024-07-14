import streamlit as st
import pandas as pd

def about_me():
    st.header('Girik Sanghi', divider=True)

    with st.container(border=False):
        st.write('''Role : Software Developer<br>
                    Ph : <a href='tel:8885548849'>+91 8885548849</a><br>
                    Email : girik2001@gmail.com<br>
                    Linkedin : <a href = 'https://www.linkedin.com/in/giriksanghi/'>giriksanghi</a>''', unsafe_allow_html=True)

    with st.container(border=True):
        st.subheader('Experience')
        st.write('''<p style='font-weight:bold; font-size:20px; margin:0; border:0;'>Tata Consultancy Services - TCS</p>
        <p style='font-weight:bold; font-size:16px; margin:0; border:0;'>( Systems Engineer : 2022 - present )</p>
        <ul>
            <li>Gained accelerated cloud expertise through TCS’ Google Business Unit, culminating in Associate Cloud Engineer certification.</li>
            <li>Pivotal role in AI.Cloud, developing innovative generative AI, data engineering, and ML-based solutions for diverse client needs.</li>
            <li>Collaborated closely with clients to conceptualize, develop, and deliver high-impact AI-driven use cases.</li>
        </ul>''', unsafe_allow_html=True) 

    with st.container(border=True):
        st.subheader('Education')   
        edu_df = pd.DataFrame(data={'Course':['Secondary', 'Higher Secondary', 'UnderGraduate'], 'School/College Name':['Gitanjali Devashray', 'Sri Chaitanya Jr Kalashala', 'Malla Reddy Institute of Engineering and Technology'], 'Specialization Name':['Science', 'Science', 'Information Technology'], 'Year of Passing':[2016, 2018, 2022], 'GPA':[9.8, 9.56, 7.7]})
        st.dataframe(edu_df, use_container_width=True, hide_index=True)

    col1, col2 = st.columns([1,1])
    with col2:
        with st.container(border=True):
            st.subheader('Languages Known')
            st.write('''<ul>
            <li>English</li>
            <li>Hindi</li>
            <li>Telugu</li>
        </ul>''', unsafe_allow_html=True)
    with col1:
        with st.container(border=True):
            st.subheader('Technical Languages Known')
            st.write('''<ul>
            <li>Python</li>
            <li>C</li>
            <li>C++</li>
            <li>Java</li>
            <li>HTML</li>
            <li>CSS</li>
            <li>JS</li>
            <li>SQL</li>
        </ul>''', unsafe_allow_html=True)

    col1, col2 = st.columns([1,1])
    with col1:
        with st.container(border=True):
            st.subheader('Skills')
    with col2:
        with st.container(border=True):
            st.subheader('Hobbies')

    with st.container(border=True):
        st.subheader('Consent')
        st.write('''I hereby declare that all the information given above is true and correct to the best of
my knowledge and belief.''')