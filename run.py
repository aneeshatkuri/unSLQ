import os
import sqlite3
import pandas as pd
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()


genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(question,prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt[0],question])
    return response.text

def read_sql_query(sql,db):
    conn = sqlite3.connect(db)
    curr= conn.cursor()
    curr.execute(sql)
    cursor = conn.execute('select * from STUDENT')
    rows = cursor.fetchall()
    cols = [description[0] for description in cursor.description]
    conn.commit()
    conn.close()

prompt=[
    """
    You are an expert in converting English questions to SQL query!
    The SQL database has the name STUDENT and has the following columns - NAME, CLASS, 
    SECTION \n\nFor example,\nExample 1 - How many entries of records are present?, 
    the SQL command will be something like this SELECT COUNT(*) FROM STUDENT ;
    \nExample 2 - Tell me all the students studying in Data Science class?, 
    the SQL command will be something like this SELECT * FROM STUDENT 
    where CLASS="Data Science"; 
    also the sql code should not have ``` in beginning or end and sql word in output

    """
]

## Streamlit App

st.set_page_config(page_title="LLManager")
st.header("uSLQ - unStructured Language Queries")

question=st.text_input("Input: ",key="input")

submit=st.button("Execute / Display")

def get_records():
    conn = sqlite3.connect("student.db")
    cursor = conn.execute('select * from STUDENT')
    rows = cursor.fetchall()
    cols = [description[0] for description in cursor.description]
    df = pd.DataFrame(rows,columns = cols)
    return df



# if submit is clicked
if submit:
    if question == "":
        question = "display table"
    response=get_gemini_response(question,prompt)
    df = read_sql_query(response,"student.db")
    st.subheader("Your Table")

    st.table(get_records())
    
    
   

