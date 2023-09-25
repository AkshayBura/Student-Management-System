import streamlit as st
import re
import pandas as pd
import requests

def main():
    st.title('Student Management System')

    st.write('###')

    preff = st.selectbox('Which operation would you like to perform ?', ('Show all Details', 'Get Details', 'Add Details', 'Update Details', 'Delete Details'), key='sb1')

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

    elif preff == 'Show all Details':

        res = requests.get('http://127.0.0.1:8000/allstudents')
        
        marks_ranges = ('Show All','Marks > 90', '90 >= Marks > 75', '75 >= Marks > 35', 'Marks <= 35')
        

        if res.status_code == 200:
            res_data = res.json()  
            st.write('###')
            st.write("API Response:")
            column_order = ["RollNo", "Name", "Email", "EngMarks", "MathsMarks", "SciMarks"]
            df = pd.DataFrame(res_data)[column_order]
            # st.dataframe(df)
            
            selected_marks_range = st.selectbox('Select English Marks Range', marks_ranges, key='1')
            if selected_marks_range:
                if selected_marks_range == 'Marks > 90':
                    filtered_df = df[df['EngMarks'] > 90]
                elif selected_marks_range == '90 >= Marks > 75':
                    filtered_df = df[(df['EngMarks'] <= 90) & (df['EngMarks'] > 75)]
                elif selected_marks_range == '75 >= Marks > 35':
                    filtered_df = df[(df['EngMarks'] <= 75) & (df['EngMarks'] > 35)]
                elif selected_marks_range == 'Marks <= 35':
                    filtered_df = df[df['EngMarks'] <= 35]
                elif selected_marks_range == 'Show All':
                    filtered_df = df
                st.dataframe(filtered_df)

            st.write('###')
            selected_marks_range = st.selectbox('Select Maths Marks Range', marks_ranges, key='2')
            if selected_marks_range:
                if selected_marks_range == 'Marks > 90':
                    filtered_df = df[df['MathsMarks'] > 90]
                elif selected_marks_range == '90 >= Marks > 75':
                    filtered_df = df[(df['MathsMarks'] <= 90) & (df['MathsMarks'] > 75)]
                elif selected_marks_range == '75 >= Marks > 35':
                    filtered_df = df[(df['MathsMarks'] <= 75) & (df['MathsMarks'] > 35)]
                elif selected_marks_range == 'Marks <= 35':
                    filtered_df = df[df['MathsMarks'] <= 35]
                elif selected_marks_range == 'Show All':
                    filtered_df = df
                st.dataframe(filtered_df)

            st.write('###')
            selected_marks_range = st.selectbox('Select Science Marks Range', marks_ranges, key='3')
            if selected_marks_range:
                if selected_marks_range == 'Marks > 90':
                    filtered_df = df[df['SciMarks'] > 90]
                elif selected_marks_range == '90 >= Marks > 75':
                    filtered_df = df[(df['SciMarks'] <= 90) & (df['SciMarks'] > 75)]
                elif selected_marks_range == '75 >= Marks > 35':
                    filtered_df = df[(df['SciMarks'] <= 75) & (df['SciMarks'] > 35)]
                elif selected_marks_range == 'Marks <= 35':
                    filtered_df = df[df['SciMarks'] <= 35]
                elif selected_marks_range == 'Show All':
                    filtered_df = df
                st.dataframe(filtered_df)

        else:
            st.error(f"Error: Unable to fetch data from the API (Status Code: {res.status_code})")


    st.write('###')

    if preff != 'Show all Details':
        Button = st.button(f'{preff}')
        if Button:
            if preff == 'Get Details':
                data = {'Roll_no' : roll}
                res = requests.get('http://127.0.0.1:8000/students', params = data)

                if res.status_code == 200:
                    res_data = res.json()  
                    st.write('###')
                    st.write("API Response:")
                    st.write(res_data)  
                elif res.status_code == 404:
                    resp = res.json()
                    st.write('###')
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
                        st.write('###')
                        st.write("API Response:")
                        st.write(resp_data)  
                    elif res.status_code == 400:
                        resp = res.json()
                        st.write('###')
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
                        st.write('###') 
                        st.write("API Response:")
                        st.write(resp_data)  
                    elif res.status_code == 404:
                        resp = res.json()
                        st.write('###')
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
                    st.write('###')
                    st.write("API Response:")
                    st.success(res_data)  
                elif res.status_code == 404:
                    resp = res.json()
                    st.write('###')
                    st.write("API Response:")
                    st.error(resp['detail'])
                else:
                    st.error(f"Error: Unable to fetch data from the API (Status Code: {res.status_code})")

if __name__ == "__main__":
    main()