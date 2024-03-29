import streamlit as st
import requests
import time

def login_page(applicant_token):
    if (applicant_token):
        st.write("The user is logged in.")

        st.write('login content and logic comes here')

    else:
        with st.form("my_form"):
            email = st.text_input(label='email')
            password = st.text_input(label='password', type='password')
            submit_res = st.form_submit_button(label='Login')

            if submit_res:
                st.write('Login clicked.')

                headers = {'content-type':'application/json; charset=utf-8'}
                response = requests.post('http://127.0.0.1:8000/api/accounts/api_auth/',
                    headers=headers, json={'email':email, 'password':password})
                
                response_json = response.json()

                if response.status_code == 200:
                    applicant_token = response_json['token']

                    if applicant_token:
                        st.session_state.key = 'applicant-token'
                        st.session_state['applicant-token'] = applicant_token
                        st.experimental_rerun()

    

def register(applicant_token):
    if applicant_token:
        with st.form("my_form"):
            st.write("You need to logout before registering")
            submit_res = st.form_submit_button(label='Logout here')

            if submit_res:
                st.write("You are now logged out.")
                del st.session_state['applicant-token']
                time.sleep(3)

                st.experimental_rerun()

    else:
        with st.form('my_form'):
            email = st.text_input(label='email')
            username = st.text_input(label='username')
            password = st.text_input(label='password', type='password')
            submit_res = st.form_submit_button(label='Register')

            if submit_res:
                st.write("Registered clicked.")

                headers = {'Content-type':'application/json; charset=utf-8'}
                response = requests.post('http://127.0.0.1:8000/api/accounts/api_register/',
                    headers=headers, json={'email':email, 'username':username, 'password':password})
                
                if response.status_code == 200:
                    st.experimental_rerun()
                

def log_out(applicant_token):
    if applicant_token:
        with st.form("my_form"):
            st.write("Do you want to log out?")
            submit_res = st.form_submit_button(label='Logout')

            if submit_res:
                if 'applicant-token' in st.session_state:
                    del st.session_state['applicant-token']
                st.write("You are now logged out.")

    else:
        st.write("You are now logged out")

def load_view():
    add_selectbox = st.sidebar.selectbox(
        "Please select an option",
        ("Login","Register","Log Out")
    )

    applicant_token = ''

    if 'applicant-token' in st.session_state:
        applicant_token = st.session_state['applicant-token']

    if add_selectbox == "Login":
        login_page(applicant_token=applicant_token)

    elif add_selectbox == "Register":
        register(applicant_token=applicant_token)

    elif add_selectbox == "Log Out":
        log_out(applicant_token=applicant_token)

if __name__ == '__main__':
    load_view()