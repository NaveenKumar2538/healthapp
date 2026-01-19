import os
import pandas as pd 
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI


# Lets get the api key form the environment

gemini_api_key = os.getenv('Google-API-Key3')

# Lets configure the model

model = ChatGoogleGenerativeAI(
    model = 'gemini-2.5-flash-lite',
    api_key = gemini_api_key)


# Design the UI of application
st.title("[healthyfyme:] :blue[your personal AI assistant]")
st.markdown('''
This application will assist you to get better and customized 
Health advice. You can ask your health related issues and get 
the personalized guidance''' )

st.write('''
Follow These Steps:
* Enter your details in sidebar
* Rate your activity and fitness on the scale of 0-5.
* Submit your details.
* Ask your question on the main page.
* Click generate and relax.''')

# Design the sidebar for all the-user parametres
st.sidebar.header(':red[ENTER YOUR DETAILS]')
name = st.sidebar.text_input('Enter your name')
gender = st.sidebar.selectbox('Select your gender',['Male','Female'])
age = st.sidebar.text_input('Enter your age')
weight = st.sidebar.text_input('Enter your weight in kgs')
height = st.sidebar.text_input('Enter your height in cms')
bmi = pd.to_numeric(weight)/((pd.to_numeric(height)/100)**2)
active = st.sidebar.slider('Rate your activity(0-5)',0,5,step=1)
fitness = st.sidebar.slider('Rate your fitness(0-5)',0,5,step=1)
if st.sidebar.button('Submit'):
    st.sidebar.write(f"{name}, your BMI is {bmi} kg/m^2")


# Lets use the gemini model to generate the report
user_input = st.text_input('Ask me your question')
prompt = '''
<Role> You are an expert in health and wellness and has 10+ years experience in guideing people.
<Goal> Generate the customized report addressing the problem the user has asked. Here is the question that user has asked: {user_input}:
<Context> Here are the details that the user has provided. 
name ={name}
age={age}
gender={gender}
height={height}
weight={weight}
gender={gender}
bmi={bmi}
activity rating(0-5)={active}
fitness rating(0-5)={fitness}


<Format> Following should be outline of the report , in the sequence as provided.
* Start with the 2-3 line of comment on the details that user has provided
* Explain what the real problem could be on the basis of input the user has provided.
* Suggest the possible reasons for the problem.
* What are the possible solutions.
* Mention the doctor from which specialization can be visited if required.
* Mention any change in the diet which is required.
* In last create a final summary of all things that as been discussed in the report.

<Instructions>
* Use bullet points where ever possible.
* Create tables to represent any data where ever posible.
* Strictly do not advice any medicine.'''


if st.button('Generate'):
    response = model.invoke(prompt)
    st.write(response.content)


