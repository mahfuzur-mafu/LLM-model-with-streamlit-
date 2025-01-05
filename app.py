import streamlit as st
from langchain import PromptTemplate,LLMChain
from langchain.llms import OpenAI

st.title("LLM Web App")

#key
st.divider()

st.write("This is a simple web app that uses the LLM to generate text based on the input text.")


prompt = st.text_input("Enter your Prompt")
st.divider()

if st.button("Send"):
    if prompt:

        template = "You ask: {user_prompt}"
        prompt_template = PromptTemplate(template=template, input_variables=["user_prompt"])
        

        llm_chain = LLMChain(llm=llm, prompt=prompt_template)
        

        response = llm_chain.run({"user_prompt": prompt})
        

        st.write(f"Assistant: {response}")
    else:
        st.write("Please enter a prompt.")
