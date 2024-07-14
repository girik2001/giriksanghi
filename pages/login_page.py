import streamlit as st
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import urllib.parse

username = urllib.parse.quote_plus(st.secrets.MONGO_DB_USERNAME)
password = urllib.parse.quote_plus(st.secrets.MONGO_DB_PASSWORD)

st.set_page_config(layout='centered')

client = MongoClient(f'mongodb+srv://{username}:{password}@my-cluster.k0gdeoi.mongodb.net/?retryWrites=true&w=majority&appName=my-cluster', server_api=ServerApi('1'))
database = client[st.secrets.MONGO_DB_DBNAME]
collection = database[st.secrets.MONGO_DB_COLLECTION_NAME]

def login_user_button_clicked(username, password):
    
    if collection.count_documents({'username':username})!=0:
        if collection.find_one({'username':username})['password'] == password:
            st.session_state.logged_in = True
            st.session_state.username = username
            st.success("User logged in Successfully.")
        else:
            st.error('Invalid Credentials')
    else:
        st.error('User not registered! Sign Up to continue...')
        st.session_state.page = 'signup'

def login_to_signup_nav_button_clicked():
    st.session_state.page = 'signup'

# def login():
st.title('Login Page')

with st.container(border=False):
    col1, col2 = st.columns([1,2.5])
    with col1:
        st.write('''<p style='margin-top:20px; margin-bottom:0; font-size:32px'>Username</p>''', unsafe_allow_html=True)
    with col2:
        username = st.text_input('Username', key = 'login_username', placeholder='Username', label_visibility='hidden')
with st.container(border=False):
    col1, col2 = st.columns([1,2.5])
    with col1:
        st.write('''<p style='margin-top:20px; margin-bottom:0; font-size:32px'>Password</p>''', unsafe_allow_html=True)
    with col2:    
        password = st.text_input('Password', type='password', key='login_password', placeholder='Password', label_visibility='hidden')

st.write('''''', unsafe_allow_html=True)
col1, col2 = st.columns([1,1])
with col1:
    st.button('Login', use_container_width=True, on_click=login_user_button_clicked, args=(username, password), type='primary')       
with col2:
    st.button('Sign Up', use_container_width=True, on_click=login_to_signup_nav_button_clicked)