from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
from io import StringIO
import streamlit as st
import os

from dotenv import load_dotenv

from langchain import OpenAI
from langchain.chains import LLMChain
from langchain_core.prompts import PromptTemplate
from langchain_community.document_loaders import TextLoader

from io import StringIO
import streamlit as st
from dotenv import load_dotenv
import time
import base64

load_dotenv()
def myfunc(query):
    loader = TextLoader(
            "/Users/ashambharkar/Desktop/Table creation/StudTable.xml",
            encoding = 'UTF-8'
        )
    document = loader.load()
    data = str(document[0])
    print(data)

    loader = TextLoader(
            "/Users/ashambharkar/Desktop/GenAI FnO/Project - GPT- Table - Extension - EDT Creation/StudTbl.AbhinavTestModel.xml",
            encoding = 'UTF-8'
        )
    document1 = loader.load()
    TblExtensionData = str(document1[0])

    loader = TextLoader(
            "/Users/ashambharkar/Desktop/GenAI FnO/Project - GPT- Table - Extension - EDT Creation/MyEDT.xml",
            encoding = 'UTF-8'
        )
    document2 = loader.load()
    EDTXML  = str(document2[0])

    prompt_template = "With the provided data {data1} {data2} answer create a similar file with {query} Remove \t and \n from output and give output in correct xml format with correct opening and closing tags.Dont make up things on your own."

    
    prompt = PromptTemplate(
        input_variables=["data1","data2","query"], 
        template=prompt_template
    )

    print(prompt)

    llm= ChatOpenAI(temperature=0,
                model_name='gpt-3.5-turbo') 
    #llm = LLMChain(llm=model,prompt=prompt)
    #query = "Create a similar file with table name as familydata with similar to StudTbl with fields  empid , empName , empfamilyname and create one fieldgroup with name myfieldgroup."
    #query = "Create an extension of table familydata with field as myfield2"
    answer = llm.invoke(prompt.format(data1=data,data2 = TblExtensionData,data3 = EDTXML,query=query))
    return answer.content


def get_file_name(mydata):
    prompt_template = "With the provided data {data1} answer {query}. Dont make up things on your own."

    prompt = PromptTemplate(
        input_variables=["data1","query"], 
        template=prompt_template
    )

    llm= ChatOpenAI(temperature=0,
                model_name='gpt-3.5-turbo') 
    query = "Return just File name under name tag with .xml extension"
    answer = llm.invoke(prompt.format(data1=mydata,query=query))
    return answer.content



    
    

