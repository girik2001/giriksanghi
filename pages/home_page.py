import streamlit as st
from pages.my_page import about_me

st.set_page_config(layout='wide')

def logout_button_clicked():
    st.session_state.logged_in = False
    st.session_state.page = 'login'

def about_user_page_trigger():
    st.session_state.page = 'About the User'

if st.session_state.page == 'About the User':
    about_me()

with st.sidebar:
    st.header('Projects : ', divider=True)
    st.button('About the Developer', use_container_width=True, on_click=about_user_page_trigger)
    st.button('Logout', type='primary', on_click=logout_button_clicked)