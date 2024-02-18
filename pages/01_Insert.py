import streamlit as st
import repo
import validators

repo = repo.Repository()


def insert():
    if validators.url(
            st.session_state.url_field) and st.session_state.url_field.strip() and st.session_state.text_field.strip():
        repo.save_line(st.session_state.text_field, st.session_state.url_field, st.session_state.extra_text_field)
        st.write("Added!")
    else:
        st.write("Malformed Input!")


if st.session_state.get("authentication_status", False):

    with st.form(key='insert', clear_on_submit=True):
        col1, col2 = st.columns(2)
        col1.text_input("Fakt", max_chars=2000, key="text_field")
        col2.text_input("Url", max_chars=2000, key="url_field")
        st.text_input("Erläuterung", max_chars=2000, key="extra_text_field")
        submit = st.form_submit_button(label='Update', on_click=insert)


else:
    st.write("Please login")
