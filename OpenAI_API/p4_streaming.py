import streamlit as st
from openai import OpenAI
import json

def display():
    OPENAI_API_KEY = st.session_state.OPENAI_API_KEY
    MODEL_NAME = st.session_state.MODEL_NAME
    st.header("OpenAI API - Streaming")
    col1, col2 = st.columns(2)

    with col1:
        st.markdown('''
                    <h4 style="color:blue">stream</h4>
                    The OpenAI API allows you to stream the response as it is generated.\n 
                    This is useful when you want to display the response as it is generated, rather than waiting for the entire response to be generated before displaying it. \n
                    <code>stream: True</code>
                    ''', unsafe_allow_html=True)

    with col2:
        st.markdown('''
                    <h4 style="color:blue">stream_options</h4>
                    Only set when stream is true. \n
                    Use this option to include the usage field in the response. The usage field provides information about the number of tokens used in the response. \n
                    <code>include_usage: True</code>
                    ''', unsafe_allow_html=True)    

    st.markdown('<hr>', unsafe_allow_html=True)
    col1, col2, col3= st.columns(3) 
    
    with col1:
        SYSTEM_MESSAGE = st.text_input("Enter the system message", help="Provide general context and instructions for the AI" ,value="You are a helpful assistant")
        USER_MESSAGE = st.text_input("Enter the user message", help="Ask a question or provide a prompt for the AI to respond to",value="What is the capital of France?")


    with col2:
        MAX_TOKENS = st.slider("max_tokens: ", value=200, min_value=1, max_value=2048, step=1, help="The maximum number of tokens to generate a response")


    with col3:
        STREAM = st.checkbox("stream", value=True, help="Set to true to stream the response as it is generated")
        INCLUDE_USAGE = st.checkbox("include_usage", value=False, help="Set to true to include the usage field in the response")




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
                    stream=STREAM,
                    stream_options={"include_usage": INCLUDE_USAGE}
                )
        '''
        )

        st.write('Response is streamed as chunks of data. You can access the token text and the entire chat response as shown below:')
        st.code('''
        chat_response = ''
        for chunk in response:
            token_text = chunk.choices[0].delta.content
            print(token_text) // print the token text
            chat_response += token_text   
        print(chat_response) // print the entire chat response                            
        ''')
    with col2:
        st.caption("Parameters:")

        col1, col2 = st.columns(2)
        with col1:
            st.write("MODEL_NAME:")
            st.write("MAX_TOKENS:")
            st.write("STREAM:")            
            st.write("INCLUDE_USAGE:")
        with col2:
            st.markdown(f'##### {MODEL_NAME}')
            st.markdown(f'##### {MAX_TOKENS}')
            st.markdown(f'##### {STREAM}')            
            st.markdown(f'##### {INCLUDE_USAGE}')        

    with col3:
        st.caption("Messages")
        st.write(MESSAGES)
    st.markdown('<hr>', unsafe_allow_html=True)
    show_response_details = st.checkbox("Show response details", value=False, help="Show response details")
    if st.button("Submit"):

        

        client = OpenAI(api_key=OPENAI_API_KEY)

        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=MESSAGES,
            max_tokens=MAX_TOKENS,
            stream=STREAM,
            stream_options={"include_usage": INCLUDE_USAGE},
        )

        st.subheader("AI message:")

        if show_response_details:
            chat_response = ''
            for chunk in response:
    
                # if 'choices' in chunk:
                col1, col2, col3 = st.columns(3)

                with col1:
                    # st.write(chunk)
                    response_dict = chunk.to_dict() 
                    response_json = json.dumps(response_dict, indent=2)
                    st.json(response_json)                    
                with col2:
                    try:
                        if chunk.choices[0].delta.content == None:
                            st.warning("content=None")
                            st.warning("This is the end of the response")
                        else:
                            token_text = chunk.choices[0].delta.content
                            st.subheader(token_text)
                            chat_response += token_text
                    except:
                        if len(chunk.choices) == 0:
                            st.success("This is the usage data")


                with col3:
                    if len(chunk.choices) == 0:
                        usage = chunk.usage
                        st.write("Prompt Tokens:", usage.prompt_tokens)
                        st.write("Completion Tokens:", usage.completion_tokens)
                        st.write("Total Tokens:", usage.total_tokens)

                st.markdown('<hr>', unsafe_allow_html=True)
            with st.chat_message("assistant"):
                st.write(chat_response)

        else:
            with st.chat_message("assistant"):
                st.write_stream(response)

