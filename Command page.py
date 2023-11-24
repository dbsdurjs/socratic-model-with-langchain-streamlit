import streamlit as st
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(
    page_title = "Command page",
    page_icon = "👋",
    layout="centered"
)

openai_api_key = "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"

st.title('명령어를 입력해주세요')

if 'user_input' not in st.session_state:
    st.session_state['user_input'] = ''

input = st.text_input("command")

if input:
    st.session_state['user_input'] = input

st.write("입력 정보: ", st.session_state['user_input'])

if st.button("go to execute"):
    con = st.container()
    switch_page("socratic model excute")



