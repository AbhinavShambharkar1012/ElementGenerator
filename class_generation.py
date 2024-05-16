from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
from io import StringIO
import streamlit as st
import os

#from dotenv import load_dotenv

from langchain import OpenAI
from langchain.chains import LLMChain
from langchain_core.prompts import PromptTemplate
from langchain_community.document_loaders import TextLoader

from io import StringIO
import streamlit as st
#from dotenv import load_dotenv
import time
import base64

load_dotenv()
def myfuncclass(query):
    #prompt_template = "Here are the details to generate SysOperation framework classes for our project:  Sample Files: - Attached are the sample files for the three classes: a. Data Contract Class: {contract} b. Service Class: {service} c. Controller Class: {controller} Looking forward to the generated classes. Thanks .Dont make up things on your own."

    prompt_template = "You are an Microsoft D365 Finance and operations Developer with the given input {query} you have to create three classes as contract, service and controller. The class name should end with contract service and controller follwing naming conventions. Dont make up things on your own. The programming language used here is X++. If you need any more information ask again.Return a dict with key as class name and values as class code."# Output instructions : Create one dict that should be as key as file name and value as class content"
    prompt = PromptTemplate(
        input_variables=["query"], 
        template=prompt_template
    ) 

    llm= ChatOpenAI(temperature=0,
                model_name='gpt-3.5-turbo',api_key = "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") 
    
    answer = llm.invoke(prompt.format(query=query))
    return answer.content

#query = "Create sysoperation framework with naming convention AASBatchJob and parameters as transferId with EDT TransfID"
#print(myfunc(query=query))

def get_class_name(mydata):
    prompt_template = "With the provided data {data1} answer {query}. Dont make up things on your own."

    prompt = PromptTemplate(
        input_variables=["data1","query"], 
        template=prompt_template
    )

    llm= ChatOpenAI(temperature=0,
                model_name='gpt-3.5-turbo',api_key = "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") 
    query = "Return just three class names with .xpp extension"
    answer = llm.invoke(prompt.format(data1=mydata,query=query))
    return answer.content
