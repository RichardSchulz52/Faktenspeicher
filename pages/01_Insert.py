import streamlit as st
import repo


def insert():
    repo.save_line(st.session_state.text_field, st.session_state.url_field)


if st.session_state.get("authentication_status", False):

    with st.form(key='insert', clear_on_submit=True):
        col1, col2 = st.columns(2)
        col1.text_input("text", max_chars=2000, key="text_field")
        col2.text_input("url", max_chars=2000, key="url_field")
        submit = st.form_submit_button(label='Update', on_click=insert)


else:
    st.write("Please login")