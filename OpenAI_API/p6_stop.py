import streamlit as st
import json
from openai import OpenAI
def display():
    OPENAI_API_KEY = st.session_state.OPENAI_API_KEY
    MODEL_NAME = st.session_state.MODEL_NAME
    st.header("OpenAI API - Stop Parameter")
    

    st.markdown('''
                    <h4 style="color:blue">stop</h4>
                    Up to 4 sequences where the API will stop generating further tokens.\n
                    A single string: <code>stop: "end"</code> \n
                    Multiple strings: <code>stop: ["at", "today"]</code>
                    ''', unsafe_allow_html=True)
    st.markdown('<hr>', unsafe_allow_html=True)
    col1, col2, col3= st.columns(3) 
    
    with col1:
        SYSTEM_MESSAGE = st.text_input("Enter the system message", help="Provide general context and instructions for the AI" ,value="You are a helpful assistant")
        USER_MESSAGE = st.text_input("Enter the user message", help="Ask a question or provide a prompt for the AI to respond to",value="What is the capital of France?")


    with col2:
        MAX_TOKENS = st.slider("max_tokens: ", value=200, min_value=1, max_value=2048, step=1, help="The maximum number of tokens to generate a response")


    with col3:
        STOP_1 = st.text_input("stop 1",placeholder="any word or phrase")
        STOP_2 = st.text_input("stop 2",placeholder="any word or phrase")
        STOP_3 = st.text_input("stop 3",placeholder="any word or phrase")
        STOP_4 = st.text_input("stop 4",placeholder="any word or phrase")

        STOP = []
        if STOP_1:
            STOP.append(STOP_1)
        if STOP_2:
            STOP.append(STOP_2)
        if STOP_3:
            STOP.append(STOP_3)
        if STOP_4:
            STOP.append(STOP_4)

    MESSAGES = [{"role": "system", "content": SYSTEM_MESSAGE}, {"role": "user", "content": USER_MESSAGE}]



    st.markdown('<hr>', unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with  col1:
        st.code(
            '''
                    from openai import OpenAI

                client = OpenAI(api_key=OPENAI_API_KEY)

                response = client.chat.completions.create(
                    model=MODEL_NAME,
                    messages=MESSAGES,
                    max_tokens=MAX_TOKENS,
                    stop=STOP
                )
        '''
        )

    with col2:
        st.caption("Parameters:")
        col1, col2 = st.columns(2)
        with col1:
            st.write("MODEL_NAME:")
            st.write("MAX_TOKENS:")
            st.write("STOP:")
        with col2:
            st.markdown(f'##### {MODEL_NAME}')
            st.markdown(f'##### {MAX_TOKENS}')
            st.markdown(f'##### {STOP}')

    with col3:
        st.caption("Messages")
        st.write(MESSAGES)
    st.markdown('<hr>', unsafe_allow_html=True)
    if st.button("Submit"):

        client = OpenAI(api_key=OPENAI_API_KEY)


        st.subheader("AI Response:")
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=MESSAGES,
            max_tokens=MAX_TOKENS,
            stop=STOP
        )

        response_dict = response.to_dict() 
        response_json = json.dumps(response_dict, indent=2)
        st.json(response_json)
        response_text = response.choices[0].message.content
        with st.chat_message("assistant"):
            st.write(response_text)

# Voice Narration of the Page
'''
Hi there!
Welcome Back. In this section, we will discuss the stop parameter.

This parameter is essential for controlling when your AI-generated text should end.
You can specify up to four stop sequences.It can be a single string or multiple strings.

Here's how it works: When the AI generates text and encounters the stop sequence you’ve defined, it will immediately cease its output. This gives you precise control over the length and structure of the responses.

Lets see this in action.

Let's give the system and user messages, set the max tokens, and define the stop sequences.
Let's say we want the AI to stop generating text when it encounters the symbol ".".

Click on the submit button to see the AI response.

We see that the AI stops after the first line. Because it encountered the symbol ".". 

You can experiment with different stop sequences to see how it affects the AI response.

Try it out and have fun!
'''