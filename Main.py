import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_pills import pills
from PIL import Image


st.set_page_config(
    page_title="Main",
    page_icon="🤖"
)

paths = ['img/img1.png', 'img/img2.png', 'img/img3.png', 'img/img4.png']
imgs = []

with st.form('intro'):
    st.info('❃ DALL-E란?')
    #st.text('OpenAI에서 개발한 텍스트를 입력으로 받아서 이미지를 생성하는 네트워크를 의미함.\nGPT-3 기반이며, 여러 사물의 다양한 상호 작용을 사진 형태로 생성 가능.')
    st.markdown('**- OpenAI에서 개발한 텍스트를 입력으로 받아서 이미지를 생성하는 네트워크를 의미함.**')
    st.markdown('**- GPT-3 기반이며, 여러 사물의 다양한 상호 작용을 사진 형태로 생성 가능.**')
    st.markdown('***')
    st.info('❃ DALL-E를 통해 생성한 이미지 예시')
    for i in paths:
        img = Image.open(i)
        imgs.append(img)
    st.image(imgs, width = 250)
    st.markdown('******')
    submit = st.form_submit_button("OK")

   

    



