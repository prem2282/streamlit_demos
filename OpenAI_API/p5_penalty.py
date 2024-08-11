import streamlit as st
from openai import OpenAI

def display():
    OPENAI_API_KEY = st.session_state.OPENAI_API_KEY
    MODEL_NAME = st.session_state.MODEL_NAME
    st.header("OpenAI API - Penalty Parameters")
    col1, col2 = st.columns(2)

    with col1:
        st.markdown('''
                    <h4 style="color:blue">presence_penalty</h4>
                    Number between -2.0 and 2.0. Positive values penalize new tokens based on whether they appear in the text so far, increasing the model's likelihood to talk about new topics.
                    <code>presence_penalty: true</code>
                    ''', unsafe_allow_html=True)

    with col2:
        st.markdown('''
                    <h4 style="color:blue">frequency_penalty</h4>
                    Number between -2.0 and 2.0. Positive values penalize new tokens based on their existing frequency in the text so far, decreasing the model's likelihood to repeat the same line verbatim. 
                    <code>frequency_penalty:true</code>
                    ''', unsafe_allow_html=True)    

    st.markdown('<hr>', unsafe_allow_html=True)
    col1, col2, col3= st.columns(3) 
    
    with col1:
        SYSTEM_MESSAGE = st.text_input("Enter the system message", help="Provide general context and instructions for the AI" ,value="You are a helpful assistant")
        USER_MESSAGE = st.text_input("Enter the user message", help="Ask a question or provide a prompt for the AI to respond to",value="What is the capital of France?")


    with col2:
        MAX_TOKENS = st.slider("max_tokens: ", value=200, min_value=1, max_value=2048, step=1, help="The maximum number of tokens to generate a response")


    with col3:
        PRESENCE_PENALTY = st.slider("presence_penalty: ", value=0.0, min_value=-2.0, max_value=2.0, step=0.1, help="Number between -2.0 and 2.0. Positive values penalize new tokens based on whether they appear in the text so far, increasing the model's likelihood to talk about new topics.")
        FREQENCY_PENALTY = st.slider("frequency_penalty: ", value=0.0, min_value=-2.0, max_value=2.0, step=0.1, help="Number between -2.0 and 2.0. Positive values penalize new tokens based on their existing frequency in the text so far, decreasing the model's likelihood to repeat the same line verbatim.")



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
                    present_penalty=PRESENCE_PENALTY,
                    frequency_penalty=FREQENCY_PENALTY,
                )
        '''
        )

    with col2:
        st.caption("Parameters:")
        col1, col2 = st.columns(2)
        with col1:
            st.write("MODEL_NAME:")
            st.write("MAX_TOKENS:")
            st.write("PRESENCE_PENALTY:")
            st.write("FREQENCY_PENALTY:")
        with col2:
            st.markdown(f'##### {MODEL_NAME}')
            st.markdown(f'##### {MAX_TOKENS}')
            st.markdown(f'##### {PRESENCE_PENALTY}')
            st.markdown(f'##### {FREQENCY_PENALTY}')            


    with col3:
        st.caption("Messages")
        st.write(MESSAGES)
    st.markdown('<hr>', unsafe_allow_html=True)
    if st.button("Submit"):

        client = OpenAI(api_key=OPENAI_API_KEY)


        col1, col2 = st.columns(2)

        with col1:  
            st.subheader("Without Penalty")
            response = client.chat.completions.create(
                model=MODEL_NAME,
                messages=MESSAGES,
                max_tokens=MAX_TOKENS
            )

            with st.chat_message("assistant"):
                without_penalty = response.choices[0].message.content
                st.write(without_penalty)



        with col2:
            st.subheader("With Penalty")
            response = client.chat.completions.create(
                model=MODEL_NAME,
                messages=MESSAGES,
                max_tokens=MAX_TOKENS,
                presence_penalty=PRESENCE_PENALTY,
                frequency_penalty=FREQENCY_PENALTY,
            )

            with st.chat_message("assistant"):
                with_penalty = response.choices[0].message.content
                st.write(with_penalty)


        st.markdown('<hr>', unsafe_allow_html=True)

        st.subheader("AI Response Analysis:")

        SYSTEM_MESSAGE_2 = "Analyse the AI response with and without penalty and explain how the penalty parameters affect the AI response. Your response should be in the form of a bullet points highlighting the difference." 
        USER_MESSAGE_1 = "Response without AI:" + without_penalty + "Response with AI:" + with_penalty

        MESSAGES_2 = [{"role": "system", "content": SYSTEM_MESSAGE_2}, {"role": "user", "content": USER_MESSAGE_1}]

        response_3 = client.chat.completions.create(
            model=MODEL_NAME,
            messages=MESSAGES_2,
            max_tokens=1000,
        )

        st.write(response_3.choices[0].message.content)


# Voice Narration of the Page
'''
Hello!
Welcome to our tutorial on the penalty parameters.

Presence penalty and frequency penalty are two parameters that can be used to influence the AI's response.

The presence penalty helps to reduce repetition in AI responses. When the AI generates text, it tends to favor words it has already used, leading to repetitive and sometimes monotonous outputs. The presence penalty steps in to counteract this tendency.

Here's how it works: When the AI considers using a word it has already mentioned, the presence penalty decreases the likelihood of choosing that word again. This encourages the AI to explore new vocabulary and generate more varied and engaging responses.

The frequency penalty, on the other hand ,is designed to reduce the repetition of individual words in AI responses. When generating text, the AI can sometimes overuse certain words, making the output less interesting and more predictable. The frequency penalty helps to address this issue.

Here's how it works: The frequency penalty decreases the probability of the AI using a word again based on how often it has already appeared in the text. This encourages the AI to choose different words and phrases, leading to more diverse and engaging content.

Both the presence penalty and frequency penalty range between -2.0 and 2.0. Positive values for these parameters increase the penalty, while negative values decrease it. 
Lets experiment with different values for the presence penalty and frequency penalty.

As usual, we will start by entering the system and user messages. Then we will set the max_tokens parameter to control the length of the AI response. Finally, we will adjust the presence penalty and frequency penalty sliders to see how they affect the AI's output.

The AI will generate two responses: one without any penalty and one with the specified penalty values. We will compare the two responses to see how the penalty parameters influence the AI's output.

Here is an analysis of the AI response with and without penalty. The analysis highlights the differences between the two responses and explain how the penalty parameters affect the AI's output.

You can also experiment with different values for penalty to see how they impact the AI's response.

What are you waiting for? Give it a try!

Have fun and we will see in the next video.

'''