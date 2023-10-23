import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_pills import pills
import openai

st.set_page_config(page_title="DALL-E", page_icon="🤖")

openai.api_key = st.secrets["api_key"]

st.sidebar.header("Recommend Keyword")
with st.sidebar:
    with st.form("keyword"):
        #st.subheader("To mix it up")
        keyword = pills("Mix and match keywords to create your own Images", 
                        ["Awkward", "Adorable", "Ambitious", "Attractive", "Beautiful", "Brave", "Cute", 
                         "Charming", "Dazzling", "Delightful", "Easy-going", "Elegance", "Extrovert", 
                         "Fascinating", "Fetching", "Genial", "Graceful", "Introvert", "Mesmerizing", 
                         "Mysterious", "Selfish", "Sociable", "Thoughtful", "Sunny", "Rainy", "Snowy",
                         ])
        submit = st.form_submit_button("Make")

st.title("Make your own Image")

st.info("🤖 prompt(e.g. Adorable Cat, 귤 먹는 사람)")
with st.form("form"):
    user_input = st.text_input("User Prompt") #text box
    size = st.selectbox("Image Size", ["256x256", "512x512", "1024x1024"])
    Transparency = st.slider("Style", 0.0, 1.0, 0.5, 0.05)
    submit = st.form_submit_button("Submit")

if submit and user_input:
    gpt_prompt = [{
        "role": "system",
        "content": 
        "Imagine the detail appearance of the input. Response it shortly around 25 words."
    }]

    gpt_prompt.append({
        "role": "user",
        "content": user_input
    })
    #st.write(user_input)

    with st.spinner("Waiting for Response"):
        gpt_response = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            messages = gpt_prompt
        )

    prompt = gpt_response["choices"][0]["message"]["content"]
    st.write(f'🤖 {prompt}')

    with st.spinner("Waiting for Create"):
        with st.form("image"):
            dalle_response = openai.Image.create(
                prompt=prompt,
                size=size
            )
            dalle_response2 = openai.Image.create(
                prompt=prompt,
                size=size
            )
            
    n = dalle_response["data"][0]["url"]
    n1 = dalle_response2["data"][0]["url"]

    html_code = f"""
        <div style="display: flex; justify-content: space-between;">
            <div style="flex: 1; margin-right: 10px;">
                <img src="{n}" alt="Image 1" width="100%">
            </div>
            <div style="flex: 1; margin-left: 10px;">
                <img src="{n1}" alt="Image 2" width="100%">
            </div>
        </div>
        """

    st.image(n)
    st.image(n1)

    image_list = [n, n1]

    st.markdown(
        """
        <style>
        .image-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));  #이미지 폭에 따라 동적으로 조정
            gap: 10px;  #이미지 간 간격 조정
        }
        </style>
        """,
        unsafe_allow_html=True,

        
    )
    #이미지 그리드 레이아웃
    st.markdown('<div class="image-grid">', unsafe_allow_html=True)

    for image in image_list:
        st.image(image, width=100)  #이미지 폭

    st.markdown('</div>', unsafe_allow_html=True)


