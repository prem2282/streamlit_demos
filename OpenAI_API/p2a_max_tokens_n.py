import streamlit as st
import json

def display():
    OPENAI_API_KEY = st.session_state.OPENAI_API_KEY
    MODEL_NAME = st.session_state.MODEL_NAME
    st.header("OpenAI API - Cost affecting Parameters")
    st.markdown("""
        <style>
        .column {
            height: 500px;
            overflow-y: auto;
        }
        </style>
        """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown('''
                    <h4 style="color:blue">max_tokens</h4>
                    The maximum number of tokens to generate a response. The higher the value, the longer the response will be.
                    ''', unsafe_allow_html=True)

    with col2:
        st.markdown('''
                    <h4 style="color:blue">n</h4>
                    The number of response choices to generate for each input message. Note that you will be charged based on the number of generated tokens across all of the choices. Keep n as 1 to minimize costs.
                    ''',  unsafe_allow_html=True)



    st.markdown('<hr>', unsafe_allow_html=True)
    col1, col2 = st.columns(2) 

    with col1:
        SYSTEM_MESSAGE = st.text_input("Enter the system message", help="Provide general context and instructions for the AI" ,value="You are a helpful assistant")
        USER_MESSAGE = st.text_input("Enter the user message", help="Ask a question or provide a prompt for the AI to respond to",value="What is the capital of France?")

    with col2:
        MAX_TOKENS = st.slider("max_tokens: ", value=200, min_value=1, max_value=2048, step=1, help="The maximum number of tokens to generate a response")
        N = st.slider("n: number of response choices", value=1, min_value=1, max_value=10, step=1, help="How many chat completion choices to generate for each input message. Note that you will be charged based on the number of generated tokens across all of the choices. Keep n as 1 to minimize costs.")
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
                    n=N,
                )
        '''
        )

    with col2:
        st.caption("Parameters:")
        col1, col2 = st.columns(2)
        with col1:
            st.write("MODEL_NAME:")
            st.write("MAX_TOKENS:")
            st.write("N:")
        with col2:
            st.markdown(f'##### {MODEL_NAME}')
            st.markdown(f'##### {MAX_TOKENS}')
            st.markdown(f'##### {N}')

    with col3:
        st.caption("Messages")
        st.write(MESSAGES)
    st.markdown('<hr>', unsafe_allow_html=True)
    if st.button("Submit"):



        from openai import OpenAI

        client = OpenAI(api_key=OPENAI_API_KEY)

        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=MESSAGES,
            max_tokens=MAX_TOKENS,
            n=N,
        )

        st.subheader("Response:")
        response_dict = response.to_dict() 
        response_json = json.dumps(response_dict, indent=2)
        st.json(response_json)

        st.subheader("AI message:")

        finish_reasons = []
        for index, choice in enumerate(response.choices):
            st.caption(f'Message on index {index} is :',)
            with st.chat_message("assistant"):
                st.write(choice.message.content)
            finish_reasons.append(choice.finish_reason)


        st.caption("Token Usage:")
        st.write("Prompt Tokens:", response.usage.prompt_tokens)
        st.write("Completion Tokens:", response.usage.completion_tokens)
        st.write("Total Tokens:", response.usage.total_tokens)
        st.write("Finish Reasons:", finish_reasons)
        st.write("System Fingerprint:", response.system_fingerprint)

# Voice Narration of the Page
'''
Welcome Back! In this section, we will discuss some important but optional parameters that can be used to customize the response generated by the AI model.

The first parameter is max_tokens. This parameter specifies the maximum number of tokens to generate a response. The higher the value, the longer the response will be. The more tokens you generate, the more it will cost you. So, keep that in mind.

The second parameter is n. This parameter specifies the number of response choices to generate for each input message. Note that you will be charged based on the number of generated tokens across all of the choices. Keep n as 1 to minimize costs. 

Now, let's see how we can use these parameters in our code.
In the code snippet provided, We are passing the model name, messages, max_tokens & n as parameters to the API.

Let's provide some context and instructions for the AI by entering a system message. Then, ask a question or provide a prompt for the AI to respond to by entering a user message.

First, lets play around with the max_tokens. It is set to 200 here. Lets modify it to some lower value.
All other parameters are set to default values.
The messages object contains the system and user messages. 

Now, lets submit and see the output. 
The response is generated but it stops at some point. This is because the AI has reached the maximum token limit.
Taking a closer look at the token usage, we can see the number of tokens used for the completion same as the max_tokens we have set.

Also, the finish reasons tell us why the AI stopped generating the response. It stopped because it reached the length, that is, max_tokens.

Next we will see 'n' parameter. It is set to 1 by default. Lets change it to 2 and see the output.

The AI generates two completions for the same input message. The token usage has doubled as well. It is useful when you want to generate multiple completions for the same input message. At the same time, it increases the cost.

Also, note that, Both the messages are stopped abruptly because they reached the max_tokens limit.

Try playing around with these parameters and see how they affect the response generated by the AI model.
Good Luck!

'''        