import streamlit as st

def login_page():
    pass

def register():
    pass

def log_out():
    pass

def load_view():
    add_selectbox = st.sidebar.selectbox(
        "Please select an option",
        ("Login","Register","Log Out")
    )

    if add_selectbox == "Login":
        login_page()

    elif add_selectbox == "Register":
        register()

    elif add_selectbox == "Log Out":
        log_out()

if __name__ == '__main__':
    load_view()