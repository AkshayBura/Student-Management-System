import streamlit as st
# from email_validator import validate_email
import requests

st.title('Student Management System')

st.write('###')

preff = st.selectbox('Which operation would you like to perform ?', ('Get Details', 'Add Details', 'Update Details', 'Delete Details'))

st.write('###')

if preff == 'Get Details':
    roll = st.number_input('Enter Roll No', 1, 100)

elif preff == 'Add Details':
    roll = st.number_input('Enter Roll No', 1, 100)
    name = st.text_input('Enter Name', placeholder='Student\'s Name')
    email = st.text_input('Enter Email', placeholder='abc@gmail.com')
    engmarks = st.number_input('Enter Eng Marks', 1, 100)
    mathsmarks = st.number_input('Enter Maths Marks', 1, 100)
    scimarks = st.number_input('Enter Sci Marks', 1, 100)

elif preff == 'Update Details':
    roll = st.number_input('Enter Roll No', 1, 100)
    name = st.text_input('Enter Name', placeholder='Student\'s Name')
    email = st.text_input('Enter Email', placeholder='abc@gmail.com')
    engmarks = st.number_input('Enter Eng Marks', 1, 100)
    mathsmarks = st.number_input('Enter Maths Marks', 1, 100)
    scimarks = st.number_input('Enter Sci Marks', 1, 100)

elif preff == 'Delete Details':
    roll = st.number_input('Enter Roll No', 1, 100)


st.write('###')
if st.button('Get Details'):
    data = {'Roll_no' : roll}
    res = requests.get('http://127.0.0.1:8000/students', params = data)

    if res.status_code == 200:
        res_data = res.json()  
        st.write("API Response:")
        st.write(res_data)  
    else:
        st.error(f"Error: Unable to fetch data from the API (Status Code: {res.status_code})")

elif st.button('Add Details'):
    data = {'RollNo' : roll, 'Email' : email, 'Name' : name, 'EngMarks' : engmarks, 'MathsMarks' : mathsmarks, 'SciMarks' : scimarks}
    # header = {'Content-Type': 'application/json'}
    res = requests.post('http://127.0.0.1:8000/add-details', params = data)

    if res.status_code == 200:
        resp_data = res.json()  
        st.write("API Response:")
        st.write(resp_data)  
    else:
        st.error(f"Error: Unable to send data to the API (Status Code: {res.status_code})")

