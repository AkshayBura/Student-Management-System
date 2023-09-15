import streamlit as st
import re
# from email_validator import validate_email
import requests

def main():
    st.title('Student Management System')

    st.write('###')

    preff = st.selectbox('Which operation would you like to perform ?', ('Get Details', 'Add Details', 'Update Details', 'Delete Details'))

    st.write('###')

    def is_valid_email(email):
        pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        return bool(re.match(pattern, email))

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
    if st.button(f'{preff}'):
        if preff == 'Get Details':
            data = {'Roll_no' : roll}
            res = requests.get('http://127.0.0.1:8000/students', params = data)

            if res.status_code == 200:
                res_data = res.json()  
                st.write("API Response:")
                st.write(res_data)  
            elif res.status_code == 404:
                resp = res.json()
                st.write("API Response:")
                st.error(resp['detail'])
            else:
                st.error(f"Error: Unable to fetch data from the API (Status Code: {res.status_code})")

        elif preff == 'Add Details':
            if is_valid_email(email):
                data = {'RollNo' : roll, 'Email' : email, 'Name' : name, 'EngMarks' : engmarks, 'MathsMarks' : mathsmarks, 'SciMarks' : scimarks}
                res = requests.post('http://127.0.0.1:8000/add-details', params = data)

                if res.status_code == 200:
                    resp_data = res.json()  
                    st.write("API Response:")
                    st.write(resp_data)  
                elif res.status_code == 400:
                    resp = res.json()
                    st.write("API Response:")
                    st.error(resp['detail'])
                else:
                    st.error(f"Error: Unable to send data to the API (Status Code: {res.status_code})")
            else :
                st.error(f"Invalid email address: {email}")

        elif preff == 'Update Details':
            if is_valid_email(email):
                data = {'RollNo' : roll, 'Email' : email, 'Name' : name, 'EngMarks' : engmarks, 'MathsMarks' : mathsmarks, 'SciMarks' : scimarks}
                res = requests.put('http://127.0.0.1:8000/update-details', params = data)

                if res.status_code == 200:
                    resp_data = res.json()  
                    st.write("API Response:")
                    st.write(resp_data)  
                elif res.status_code == 404:
                    resp = res.json()
                    st.write("API Response:")
                    st.error(resp['detail'])
                else:
                    st.error(f"Error: Unable to send data to the API (Status Code: {res.status_code})")
            else :
                st.error(f"Invalid email address: {email}")

        elif preff == 'Delete Details':
            data = {'Roll_No' : roll}
            res = requests.delete('http://127.0.0.1:8000/delete-details', params = data)
            
            if res.status_code == 200:
                res_data = res.json()  
                st.write("API Response:")
                st.success(res_data)  
            elif res.status_code == 404:
                resp = res.json()
                st.write("API Response:")
                st.error(resp['detail'])
            else:
                st.error(f"Error: Unable to fetch data from the API (Status Code: {res.status_code})")

if __name__ == "__main__":
    main()