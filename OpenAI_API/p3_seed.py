import streamlit as st
from openai import OpenAI
import json
def display():
    OPENAI_API_KEY = st.session_state.OPENAI_API_KEY
    MODEL_NAME = st.session_state.MODEL_NAME
    st.header("OpenAI API - Seed parameter")
    st.markdown('''
                <h4 style="color:blue">seed</h4>
                This feature is in Beta. If specified, our system will make a best effort to sample deterministically, such that repeated requests with the same seed and parameters should return the same result. Determinism is not guaranteed, and you should refer to the system_fingerprint response parameter to monitor changes in the backend.
                ''',unsafe_allow_html=True)
    st.markdown('<hr>', unsafe_allow_html=True)
    col1, col2 = st.columns(2) 

    with col1:
        SYSTEM_MESSAGE = st.text_input("Enter the system message", help="Provide general context and instructions for the AI" ,value="You are a helpful assistant", )
        USER_MESSAGE = st.text_input("Enter the user message", help="Ask a question or provide a prompt for the AI to respond to",value="Give me 10 historical facts about India")


    with col2:
        MAX_TOKENS = st.slider("max_tokens: ", value=200, min_value=1, max_value=2048, step=1, help="The maximum number of tokens to generate a response")
        col1, col2 = st.columns(2)
        with col1:
            SEED_1 = st.number_input("seed 1", value=25, help="A random seed to use for the chat completion. If you set the seed, you will get the same result each time you run the code with the same seed value.")
        with col2:
            SEED_2 = st.number_input("seed 2", value=25, help="A random seed to use for the chat completion. If you set the seed, you will get the same result each time you run the code with the same seed value.")
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
                    seed=SEED
                )
        '''
        )

    with col2:
        st.caption("Parameters:")
        col1, col2 = st.columns(2)
        with col1:
            st.write("MODEL_NAME:")
            st.write("MAX_TOKENS:")
        with col2:
            st.markdown(f'##### {MODEL_NAME}')
            st.markdown(f'##### {MAX_TOKENS}')
            st.markdown(f'##### {SEED_1} / {SEED_2}')

    with col3:
        st.caption("Messages")
        st.write(MESSAGES)
    st.markdown('<hr>', unsafe_allow_html=True)
    if st.button("Submit"):



        

        client = OpenAI(api_key=OPENAI_API_KEY)

        def get_response(seed):

            response = client.chat.completions.create(
                model=MODEL_NAME,
                messages=MESSAGES,
                max_tokens=MAX_TOKENS,
                seed=seed
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

        col1, col2 = st.columns(2)

        with col1:
            st.subheader(f"With Seed {SEED_1}" )
            get_response(SEED_1)

        with col2:
            st.subheader(f"With Seed {SEED_2}")
            get_response(SEED_2)

# Voice Narration of the Page
'''
Hello!
OpenAI API has a added a feature called seed. 
This feature is in Beta. 
If specified, the system will make a best effort to sample deterministically, such that repeated requests with the same seed and parameters should return the same result. Determinism is not guaranteed, and you should refer to the system_fingerprint response parameter to monitor changes in the backend.
You can provide a random seed to use for the chat completion. If you set the seed, you will get the same result each time you run the code with the same seed value.

Let's see how it works.

We will provide a system message and a user message.
The system message is "You are a helpful assistant" and the user message is "Give me 5 science facts".
We will make two requests with different seeds and see if the response is same or not.

First, lets keep the seed as 25 and 25. This means we are providing the same seed for both the requests.
This should return almost the same response for both the requests. 
Note that the system fingerprint is same for both the requests. It means that OpenAI has ensured that the response is generated from the same backend which makes it's response consistent for the same seed.

Now, let's change one of the seed to say, 90000. This should return different responses as the seed is different.

From the response, you can see that the response is different for different seeds.
Also, the system fingerprint is different for different seeds, which means that the response is generated from different backend.

Note that the response is not guaranteed to be same for different seeds. It is just a best effort to make the response deterministic for the same seed.

That's all for the seed parameter.
Hope you understood! Lets meet in the next feature.
Until then, Good Bye!


'''