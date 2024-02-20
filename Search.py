import streamlit as st

import repo

db_repo = repo.Repository()
db_repo.open_db()

st.set_page_config(
    page_title="Faktenspeicher",
)

if 'data' not in st.session_state:
    st.session_state.data = db_repo.search("")


def search():
    st.session_state.data = db_repo.search(st.session_state.search_input)


st.markdown("""
    # Willkommen zum Faktenspeicher
""")

text_field = st.text_input(label="Suche", max_chars=2000, on_change=search, key='search_input')
a = st.dataframe(st.session_state.data, column_config={'Beweis': st.column_config.LinkColumn("Beweis", display_text="//(.*?)/")}, hide_index=True)
