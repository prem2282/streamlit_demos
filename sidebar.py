import streamlit as st
import OpenAI_API.p1_intro
import OpenAI_API.p2a_max_tokens_n
import OpenAI_API.p2b_temp_top_p
import OpenAI_API.p3_seed
import OpenAI_API.p4_streaming
import OpenAI_API.p5_penalty
import OpenAI_API.p6_stop
import OpenAI_API.p7_image_input
import OpenAI_API.p8_structured_output

def home_page_for_intro():
    st.header("Welcome to the OpenAI Chat Tutorial")

    st.markdown('''
    The OpenAI Chat API allows you to generate human-like text responses to given prompts.
    This tutorial will help you understand the various parameters that can be used to customize the OpenAI Chat API.

    ##### Chapters:                
    Select a chapter from the sidebar to learn more about each parameter:
    1. **Introduction** - Learn about the OpenAI Chat API and how it works.
    2. **Cost affecting Parameters**: These parameters can affect the cost of the API call as they determine the number of tokens generated.
    3. **Randomness Parameters**: These parameters control the randomness of the generated text. This affects the diversity of responses.
    4. **Consistency Parameter**: This parameter allows you to generate deterministic responses by setting a seed.
    5. **Penalty Parameters**: These parameters allow you to penalize certain tokens in the generated text.
    6. **Stop Parameter**: This parameter allows you to stop the generation of tokens based on certain words or phrases.
    7. **Streaming**: This parameter allows you to stream the response in real-time.
    8. **Image Input**: Learn how to provide image input to the model.
                
    ##### References:
    - [OpenAI API Reference](https://platform.openai.com/docs/api-reference/introduction)
    - [OpenAI API Documentation ](https://platform.openai.com/docs/overview)
    - [Get OpenAI API Key](https://platform.openai.com/api-keys)
                

                    ''')



def home_page_for_embedding():
    st.header("Welcome to the OpenAI Embedding Tutorial")

def set_sidebar():
    # Function to set the API key in the session state

    st.session_state.OPENAI_API_KEY = st.sidebar.text_input("Enter OpenAI API Key", type="password")
    st.session_state.MODEL_NAME = st.sidebar.selectbox("Select Chat Model", ["gpt-4o-mini", "gpt-4o",  "gpt-4o-2024-08-06"])
    st.session_state.TUTORIAL = st.sidebar.selectbox("Select Tutorial", ["OpenAI Chat", "Embedding"])

    # Check if API key is already in session state
    # if "api_key" not in st.session_state:
    #     save_api_key()
    # else:
    #     st.sidebar.success("API Key is already set")

    st.sidebar.markdown('''---''')

    if st.session_state.TUTORIAL == "OpenAI Chat":

        page = st.sidebar.radio("Select Chapter", ["Home","Intro", "Cost affecting Parameters","Randomness Parameters", "Consistancy parameter",  "Penalty Parameters", "Stop Parameter", "Streaming", "Image Input", "Structured Output"])

    elif st.session_state.TUTORIAL == "Embedding":
            
            page = st.sidebar.radio("Select Chapter", ["Home","Embedding"])
    # Add footer note in the sidebar
    footer_note = """
    ---
    **Created By:** *PremAnand*.
    """

    st.sidebar.markdown(footer_note)
    # Load the selected page

    

    if page == "Home":
        if st.session_state.TUTORIAL == "OpenAI Chat":
            home_page_for_intro()
        elif st.session_state.TUTORIAL == "Embedding":
            home_page_for_embedding()
    elif page == "Intro":
        OpenAI_API.p1_intro.display()
    elif page == "Cost affecting Parameters":
        OpenAI_API.p2a_max_tokens_n.display()
    elif page == "Randomness Parameters":
        OpenAI_API.p2b_temp_top_p.display()    
    elif page == "Consistancy parameter":
        OpenAI_API.p3_seed.display()
    elif page == "Streaming":
        OpenAI_API.p4_streaming.display()        
    elif page == "Penalty Parameters":
        OpenAI_API.p5_penalty.display()         
    elif page == "Stop Parameter":
        OpenAI_API.p6_stop.display()         
    elif page == "Image Input":
        OpenAI_API.p7_image_input.display()   
    elif page == "Structured Output":
        OpenAI_API.p8_structured_output.display()      

