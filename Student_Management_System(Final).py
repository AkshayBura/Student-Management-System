class SubjMarks:
    def __init__(self, Eng, Maths, Sci):
        self.Eng = Eng
        self.Maths = Maths
        self.Sci = Sci
        
        print(f"\nName : {student.name}, STD : {student.div} \nMarks in the subjects: English - {self.Eng} , Maths - {self.Maths} , Science - {self.Sci}")

def Marks_Input():
    while True:
        Eng = input("\nEnter Student's English marks : ")
        if Eng.isdigit() and int(Eng) <= 100:
            break
        else:
            print("-----Marks should consist of only numbers and it should be under 100-----")

    while True:
        Maths = input("Enter Student's Maths marks : ")
        if Maths.isdigit() and int(Maths) <= 100:
            break
        else:
            print("-----Marks should consist of only numbers and it should be under 100-----")

    while True:
        Sci = input("Enter Student's Science marks : ")
        if Sci.isdigit() and int(Sci) <= 100:
            break
        else:
            print("-----Marks should consist of only numbers and it should be under 100-----")

    return Eng, Maths, Sci


# class ColgMarks(SubjMarks):
#     def __init__(self, Eng, Maths, Sci, it):
#         super().__init__(Eng, Maths, Sci)
#         self.it = it

class SMS:
    def __init__(self, name: str, div: str):
    # def __init__(self, roll:int, name:str, div: str, marks: SubjMarks):
        # self.roll = int(input("\nEnter your Roll No : "))
        self.name = name
        self.div = div



def Details_Input():
    while True:
        name = str(input("\nEnter Student's Name : "))
        if name.isalpha():
            break
        else:
            print("-----Name should consist of only alphabets-----")

    while True:    
        div = str(input("Enter Student's Std : "))
        if div.isalnum():
            break
        else:
            print("-----Std should consist of number and alphabet only-----")

    return name , div

# marks = SubjMarks(80, 90, 85)
# student = SMS(1, "Varun", "10b", marks)
# marks2 = SubjMarks(79, 94, 89)
# student2 = SMS(2, "Akshay", "10a", marks2)

# print(student)

# # pyodbc
import pyodbc

conn = pyodbc.connect(
        r'DRIVER={ODBC Driver 17 for SQL Server};'
        r'SERVER=DESKTOP-2CMID66\SQLEXPRESS;'
        # 'Integrated Security = True;'
        r'Trusted_Connection=Yes;'
        r'Connection Timeout=30;'
        r'DATABASE=StudentDB;'
)


#query = f"CREATE TABLE Student (RollNo int, Name TEXT, STD varchar);"
#query = f"CREATE TABLE SubjectsMarks (ENG int, MATHS int, SCI int)"
#query = f"ALTER TABLE Student drop column SubjectMarks"
#query = f"INSERT INTO student VALUES({student.roll},'{student.name}','{student.div}',{marks2.Eng},{marks2.Maths},{marks2.Sci})"
# print(query)


flag = True

while flag:

    User_Input = input("\nWhat operation would you like to do? (Create/Add/Update/Del/View/Store/Truncate): ")
    cursor = conn.cursor()
    if User_Input.upper() == "ADD":
        student_name, student_div = Details_Input()
        student = SMS(student_name, student_div)
        
        Eng_marks, Maths_marks, Sci_marks = Marks_Input()
        marks = SubjMarks(Eng_marks, Maths_marks, Sci_marks)      
        
        query = f"INSERT INTO Student VALUES('{student.name}','{student.div}',{marks.Eng},{marks.Maths},{marks.Sci})"
        cursor.execute(query)
        cursor.commit()
        cursor.close()

    elif User_Input.upper() == "UPDATE":
        inp = int(input("Enter the roll no whose details you want to update: "))
        student_name, student_div = Details_Input()
        student = SMS(student_name, student_div)
        
        Eng_marks, Maths_marks, Sci_marks = Marks_Input()
        marks = SubjMarks(Eng_marks, Maths_marks, Sci_marks)   

        query = f"UPDATE Student SET Name = '{student.name}' , STD = '{student.div}' , Eng = {marks.Eng} , Maths = {marks.Maths} , Sci = {marks.Sci} WHERE RollNo = {inp}"
        cursor.execute(query)
        cursor.commit()
        cursor.close()

    elif User_Input.upper() == "DEL":
        inp = int(input("Enter the roll no whose details you want to delete: "))
        query = f"DELETE FROM Student WHERE RollNo = {inp}"
        cursor.execute(query)
        cursor.commit()
        cursor.close()

    elif User_Input.upper() == "TRUNCATE":
        query = f"TRUNCATE TABLE Student"
        cursor.execute(query)
        cursor.commit()
        cursor.close()

    elif User_Input.upper() == "CREATE":
        query = f"CREATE TABLE Student (RollNo int IDENTITY(1,1), Name TEXT, STD varchar(20), ENG int, MATHS int, SCI int, PRIMARY KEY (RollNo))"
        cursor.execute(query)
        cursor.commit()
        cursor.close()

    elif User_Input.upper() == "STORE":
        data1 = cursor.execute("SELECT (SELECT RollNo AS Roll, Name AS Name, STD AS STD, Eng, Maths, Sci FROM Student FOR JSON PATH) AS jsonData")
        data1 = data1.fetchall()
        print(data1)    
        cursor.commit()
        cursor.close()

    elif User_Input.upper() == "VIEW":
        print("RollNo | Name | STD | ENG | MATHS | SCI")
        print("")
        data = cursor.execute("SELECT * FROM Student")
        data = data.fetchall()
        for row in data:
            for column in row:
                print(column, end=' | ')
            print('\n')
        cursor.commit()
        cursor.close()
        
    while True:    
        new = input("\nDo you want to perform more such operations? (Yes/No): ")
        if new.upper() == "NO":
            flag = False
            break
        elif new.upper() == "YES":
            break
        else:
            print("Enter yes or no only")
            continue