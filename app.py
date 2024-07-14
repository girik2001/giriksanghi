import streamlit as st

if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

if 'username' not in st.session_state:
    st.session_state.username = None

if 'page' not in st.session_state:
    st.session_state.page = 'login'



login_page = st.Page('pages/login_page.py', title='Login', icon=":material/login:")
sign_up_page = st.Page('pages/signup_page.py', title='Signup', icon=":material/login:")
home_page = st.Page('pages/home_page.py', title='Girik Sanghi')



if st.session_state.logged_in:
    pg = st.navigation(
        {
            "About Me" : [home_page],
        }
    )
else:
    if st.session_state.page == 'login':
        pg = st.navigation([login_page])
    elif st.session_state.page == 'signup':
        pg = st.navigation([sign_up_page])

pg.run()