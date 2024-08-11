import streamlit as st
import json
from openai import OpenAI

def display():
    st.header("OpenAI API - Introduction")

    st.subheader("Model Name")

    st.markdown("The model name is the name of the model you want to use for the completion. You can find the list of available models in the OpenAI API documentation.")

    st.subheader("Message Roles")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown('''
                    <h4 style="color:blue">System</h4>
                    Provides general context and instructions for the AI. It is the first message in the conversation. 
                    ''', unsafe_allow_html=True)

    with col2:
        st.markdown('''
                    <h4 style="color:blue">User</h4>
                    The user message is the second message in the conversation. It asks a question or provides a prompt for the AI to respond to.
                       ''', unsafe_allow_html=True)  


    with col3:
        st.markdown('''
                    <h4 style="color:blue">Assistant</h4>
                    The AI message is the response generated by the AI based on the system and user messages.
                       ''', unsafe_allow_html=True)  
    st.markdown('<hr>', unsafe_allow_html=True)

    OPENAI_API_KEY = st.session_state.OPENAI_API_KEY
    MODEL_NAME = st.session_state.MODEL_NAME

    col1, col2, col3 = st.columns(3) 

    with col1:
        SYSTEM_MESSAGE = st.text_input("Enter the system message", help="Provide general context and instructions for the AI" ,value="You are a helpful assistant")

    with col2:
        USER_MESSAGE = st.text_input("Enter the user message", help="Ask a question or provide a prompt for the AI to respond to",value="What is the capital of France?")

    MESSAGES = [{"role": "system", "content": SYSTEM_MESSAGE}, {"role": "user", "content": USER_MESSAGE}]

    st.markdown('<hr>', unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)

    with col1:
        st.code(
            '''
            from openai import OpenAI

            client = OpenAI(api_key=OPENAI_API_KEY)

            response = client.chat.completions.create(
                model=MODEL_NAME,
                messages=MESSAGES,
            )
            ''')
        
    with col2:
        st.caption("Parameters:")
        col1, col2 = st.columns(2)
        with col1:
            st.write("MODEL_NAME:")
        with col2:
            st.markdown(f'##### {MODEL_NAME}')

    with col3:
        st.caption("MESSAGES:")
        st.write("The message is a list of dictionaries containing the role and content of each message in the conversation. The role can be 'system', 'user' or 'assistant.")
        st.write(MESSAGES)

    st.markdown('<hr>', unsafe_allow_html=True)
    if st.button("Submit"):

        client = OpenAI(api_key=OPENAI_API_KEY)

        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=MESSAGES,
        )
        response_dict = response.to_dict() 
        response_json = json.dumps(response_dict, indent=2)
        st.json(response_json)

        st.subheader("Assistant Message can be accessed from:")
        st.code("response.choices[0].message.content")

        st.subheader("Role can be found in:")
        st.code("response.choices[0].message.role")


        with st.chat_message("assistant"):
            st.write(response.choices[0].message.content)

        st.subheader("Token Usage:")
        st.code("response.usage")
        st.write(response.usage)
        st.caption("Token Usage:")
        st.write("Prompt Tokens:", response.usage.prompt_tokens)
        st.write("Completion Tokens:", response.usage.completion_tokens)
        st.write("Total Tokens:", response.usage.total_tokens)


# Voice Narration of the Page
'''
Hello! Welcome to the chapter on Introduction to OpenAI API. 
In this chapter, We will learn how to interact with the OpenAI API to generate responses to user queries.
The OpenAI API allows you to build AI-powered conversational agents that can respond to user queries in a natural and engaging way.
We will be using the OpenAI Python library to Interact with OpenAI.

What is the python library?
it is openai, which is a Python client library for the OpenAI API.
Install the openai library using the terminal comman pip install openai.

Let's start by getting the API key from the OpenAI website.
Head over to platform.openai.com and create an account if you don't have one.
Once you have created an account, you can generate an API key from the API keys section.
Copy the API key and save it in a safe place.
Paste it in the API Key field on the sidebar.

Next, we need to select the model we want to use for the completion.
We can choose from a list of available models in the OpenAI API documentation.
In this tutorial, we will use the gpt-3.5 turbo and gpt-4 models as needed.

The OpenAI API uses a message-based interface to generate responses to user queries.
There are three types of messages: system, user, and assistant.
The system message provides general context and instructions for the AI.
The user message asks a question or provides a prompt for the AI to respond to.
The assistant message is the response generated by the AI based on the system and user messages.

Enter the system and user messages in the text fields provided.
For example, lets set the system message to "You are a helpful assistant" and the user message to "What is the capital of India?".

Here is the code snippet to generate a response using the OpenAI API.
First, we import the OpenAI library and create a client object with the API key.

Next, we call the chat.completions.create method with the model name and messages as parameters.

Before we submit the request, let's take a look at the parameters and messages we have set.
The MODEL_NAME should be the name of the model we want to use. In this case, we will use the gpt-3.5 turbo model.
Then we create a list of messages containing the system and user messages.
You can see that the MESSAGE is a list of dictionaries containing the role and content of each message in the conversation.

Finally, we call the chat.completions.create method with the model name and messages as parameters.
The response object contains the generated response from the AI.

Let's understand the response object.
There is a unique id for each response, a list of choices containing the generated response, and the usage field providing information about the number of tokens used in the response.
There is also information about the model used, timestamp in unix format, and the object type.

Lets take a closer look at the choices.
It has the message object containing the role and content of the response. The role is the assistant and the content is the generated response.
The finish_reason indicates the reason the conversation ended. In this case, it is "stop".

Now, lets see the usage field.
It provides information about the number of tokens used in the response.
The prompt_tokens are the tokens used in the prompt message.
The completion_tokens are the tokens used in the generated response.
The total_tokens are the total number of tokens used in the conversation.

And that's it! You have learned how to generate responses using the OpenAI API. 
Now, you can experiment with different models and messages to create your own AI-powered conversational agents.
Head on to your favorite code editor and start building your own AI chatbot with the OpenAI API.

'''
