import streamlit as st
import json
from openai import OpenAI

def display():
    OPENAI_API_KEY = st.session_state.OPENAI_API_KEY
    MODEL_NAME = st.session_state.MODEL_NAME
    st.header("OpenAI API - Structured Output")
    st.markdown('''
                <h4 style="color:blue">Structured Output</h4>

                **response_format**: Specify a json schema to structure the response. The schema should be a valid JSON object. The response will be structured according to the schema provided. \n
                Visit for detailed info:  <a>  https://openai.com/index/introducing-structured-outputs-in-the-api/ </a>
                ''', unsafe_allow_html=True)

    st.markdown('<hr>', unsafe_allow_html=True)
    col1, col2, col3= st.columns(3) 

    with col1:
        SYSTEM_MESSAGE = st.text_input("Enter the system message", help="Provide general context and instructions for the AI" ,value="You are a helpful assistant")
        USER_TEXT = st.text_input("Enter the user message", help="Ask a question or provide a prompt for the AI to respond to",value="Tell me about the movie 'Titanic'")
        MAX_TOKENS = st.slider("max_tokens: ", value=300, min_value=1, max_value=2048, step=1, help="The maximum number of tokens to generate a response")

    with col2:
        RESPONSE_FORMAT = {
            "type": "json_schema",
            "json_schema": {
                "name": "movie_trivia",
                "strict": True,
                "schema": {
                    "type": "object",
                    "properties": {
                        "title": {
                            "type": "string"
                        },
                        "storyline": {
                            "type": "string"
                        },
                        "cast": {
                            "type": "array",
                            "items": {
                                "type": "string"
                            }
                        },
                        "year": {
                            "type": "number"
                        },
                        "genre": {
                            "type": "string"
                        },
                    },
                    "required": ["title", "storyline","cast","year", "genre"],
                    "additionalProperties": False                
                },

            }
        
        }
        with st.container(border=True, height=800):
            st.markdown("###### Response Format")
            st.write(RESPONSE_FORMAT)

    with col3:
        st.caption("Parameters:")
        col1, col2 = st.columns(2)
        with col1:
            st.write("MODEL_NAME:")
            st.write("MAX_TOKENS:")

        with col2:
            st.markdown(f'##### {MODEL_NAME}')
            st.markdown(f'##### {MAX_TOKENS}')

        USER_MESSAGE = {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": USER_TEXT
                }
            ]
        }


        MESSAGES = [{"role": "system", "content": SYSTEM_MESSAGE}, USER_MESSAGE]   
        st.caption("Messages")
        st.write(MESSAGES)

         


    st.markdown('<hr>', unsafe_allow_html=True)
    col1, col2= st.columns(2)
    with  col1:
        st.markdown("###### With Response Format")
        st.code(
            '''
                    from openai import OpenAI

                client = OpenAI(api_key=OPENAI_API_KEY)

                response = client.chat.completions.create(
                    model=MODEL_NAME,
                    messages=MESSAGES,
                    max_tokens=MAX_TOKENS,
                    response_format=RESPONSE_FORMAT
                )
        '''
        )    

    with col2:
        st.markdown("###### Without Response Format")
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

    st.markdown('<hr>', unsafe_allow_html=True)        

    if st.button("Submit"):

        client = OpenAI(api_key=OPENAI_API_KEY)


        cols = st.columns(2)

        with cols[0]:

            st.subheader("AI Response with Json Schema:")
            with st.spinner('Generating response...'):
                response = client.chat.completions.create(
                    model=MODEL_NAME,
                    messages=MESSAGES,
                    max_tokens=MAX_TOKENS,
                    response_format=RESPONSE_FORMAT
                )

            response_dict = response.to_dict() 
            response_json = json.dumps(response_dict, indent=2)
            st.json(response_json)
            response_text = response.choices[0].message.content
            json_obj = json.loads(response_text)

        with cols[1]:


            st.subheader("AI Response without Json Schema:")
            with st.spinner('Generating response...'):

                response = client.chat.completions.create(
                    model=MODEL_NAME,
                    messages=MESSAGES,
                    max_tokens=MAX_TOKENS,
                )

            response_dict = response.to_dict() 
            response_json = json.dumps(response_dict, indent=2)
            st.json(response_json)
            response_text = response.choices[0].message.content


        st.markdown('<hr>', unsafe_allow_html=True)

        cols = st.columns(2)

        with cols[0]:
                with st.container(border=True):
                    with st.chat_message("assistant"):
                        st.write(json_obj)

        with cols[1]:                        
                with st.container(border=True):
                    with st.chat_message("assistant"):
                        st.write(response_text)

##### Voice Narration
'''
In this tutorial, we will learn about the structured output response in the OpenAI API. The response format parameter allows you to specify a JSON schema to structure the response. The schema should be a valid JSON object. The response will be structured according to the schema provided.

Let's see how to use the response format parameter in the OpenAI API. We will provide a system message and a user message, and set the max tokens to 200. 
In this example, the system message is "You are a helpful assistant" and the user message is "Tell me about the movie 'Titanic'". We will also provide a response format in the form of a JSON schema. The schema will define the structure of the response.


In the response format, we have defined a JSON schema for a movie trivia response. The schema specifies the properties of the response, such as the title, storyline, cast, year, and genre of the movie. The schema also specifies that the title, storyline, cast, year, and genre are required properties, and that no additional properties are allowed.

Note the strict parameter in the schema. If strict is set to true, the response must adhere strictly to the schema. If strict is set to false, the response can contain additional properties not defined in the schema. The additionalProperties parameter must be set to false if strict is set to true.

Here is the values of the parameters we have set.

Now, lets look at the code to make the API call with and without the response format parameter.
First code block shows how to make the API call with the response format parameter. The response will be structured according to the schema provided in the response format.
Second code block shows how to make the API call without the response format parameter. The response will not be structured according to any schema.

Lets click on the submit button to see the response from the AI.

In the response, you will see the structured response according to the JSON schema provided in the response format. The response will contain the title, storyline, cast, year, and genre of the movie 'Titanic'. You will also see the unstructured response without the JSON schema.

Here is the structured & unstructured response from the AI.

It's cool, right? You can use the structured output parameter to get responses in a structured format according to your requirements.

Note that this is already available GPT-4o-mini default model. 
If we change the model to gpt-4o, we see that the code will not work as the structured output is not available in the default gpt-4o model. OpenAI has mentioned that they will give 3 weeks notice making it available in the default model.

For now, we can use the gpt-4o-2024-08-06 model to get the structured output.
'''
