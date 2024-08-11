import streamlit as st
import json
from openai import OpenAI

def display():
    OPENAI_API_KEY = st.session_state.OPENAI_API_KEY
    MODEL_NAME = st.session_state.MODEL_NAME
    st.header("OpenAI API - Image input")
    st.markdown('''
                <h4 style="color:blue">OpenAI Vision</h4>

                *image_url*: The URL of the image to be processed. The image must be accessible to the OpenAI API. The image should be in JPEG, PNG, or GIF format. \n
                *detail*: By controlling the detail parameter, which has three options, low, high, or auto, you have control over how the model processes the image and generates its textual understanding. By default, the model will use the auto setting which will look at the image input size and decide if it should use the low or high setting.\n
                Visit for detailed info:  <a>  https://platform.openai.com/docs/guides/vision </a>
                ''', unsafe_allow_html=True)


    st.markdown('<hr>', unsafe_allow_html=True)
    col1, col2, col3= st.columns(3) 
    
    with col1:
        SYSTEM_MESSAGE = st.text_input("Enter the system message", help="Provide general context and instructions for the AI" ,value="You are a helpful assistant")
        USER_TEXT = st.text_input("Enter the user message", help="Ask a question or provide a prompt for the AI to respond to",value="What is the capital of France?")


    with col2:
        MAX_TOKENS = st.slider("max_tokens: ", value=200, min_value=1, max_value=2048, step=1, help="The maximum number of tokens to generate a response")
        IMAGE_URL = st.text_input("Image URL", placeholder="https://example.com/image.jpg")
        DETAIL = st.radio("Detail",["auto", "high", "low"], help="By controlling the detail parameter, which has three options, low, high, or auto, you have control over how the model processes the image and generates its textual understanding. By default, the model will use the auto setting which will look at the image input size and decide if it should use the low or high setting.")

    with col3:
        if IMAGE_URL:
            st.image(IMAGE_URL, caption="User given Image", use_column_width=True)

    USER_MESSAGE = {
        "role": "user",
        "content": [
            {
                "type": "text",
                "text": USER_TEXT
            },            
            {
                "type": "image_url",
                "image_url" : {
                    "url": IMAGE_URL,
                    "detail": DETAIL
                }
            }
        ]
    }


    MESSAGES = [{"role": "system", "content": SYSTEM_MESSAGE}, USER_MESSAGE]


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
        )

        response_dict = response.to_dict() 
        response_json = json.dumps(response_dict, indent=2)
        st.json(response_json)
        response_text = response.choices[0].message.content
        with st.chat_message("assistant"):
            st.write(response_text)


# Voice Narration of the Page
'''
Hello Buddy, in this section, we will see how to input an image to the OpenAI API. 
The model gpt-4o is capable of processing images and generating textual understanding.
We will provide an image URL and let the AI look at the image and explain us about the image.

The message object is little different here. The user message will have a two parts. text and an image_url.

The text part will have the user message. Here we can ask a question or provide a prompt for the AI to respond to.
The image_url will have the url of the image and the detail parameter which has three options, low, high, or auto.
There can be more than one image_url in the message object.

The detail parameter controls how the model processes the image.
If it is set to low, the model will use a lower resolution version of the image. This can be useful if you want the model to focus on the general content of the image rather than the details. This will also consume fewer tokens.

If it is set to high, the model will use a higher resolution version of the image. This can be useful if you want the model to focus on the details of the image. This will consume more tokens.

By default, the model will use the auto setting which will look at the image input size and decide if it should use the low or high setting.

Lets try this out. 
We will provide an image URL of a cat. It's so cute, isn't it?
Now, lets set the detail parameter to low.

On the user message, we will ask the AI to describe the image. This goes into the text part of the user message.

Lets see what the AI has to say about the image.

Look at the response. It's amazing, isn't it?
Also, see that the tokens consumed is very less.

Now, lets try with the detail parameter set to high.
The AI will focus on the details of the image.

The response is more detailed and the tokens consumed is more.

Setting the detail parameter to auto, the model will decide if it should use the low or high setting based on the image input size.
In this case, the model will use the high setting. We can see that from the tokens consumed.

Hope you enjoyed this section. Have fun exploring!

'''

image_url = 'https://images.pexels.com/photos/104827/cat-pet-animal-domestic-104827.jpeg'