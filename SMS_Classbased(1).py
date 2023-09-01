class SubjMarks:
    def __init__(self):
        self.Eng = int(input("\nEnter your English Marks : "))

        self.Maths = int(input("Enter your Maths Marks : "))

        self.Sci = int(input("Enter your Science Marks : "))
        
        print(f"\nName : {student.name}, STD : {student.div}, \nMarks in the subjects: English - {self.Eng} , Maths - {self.Maths} , Science - {self.Sci}")


# class ColgMarks(SubjMarks):
#     def __init__(self, Eng, Maths, Sci, it):
#         super().__init__(Eng, Maths, Sci)
#         self.it = it

class SMS:
    def __init__(self, marks=SubjMarks):
    # def __init__(self, roll:int, name:str, div: str, marks: SubjMarks):
        # self.roll = int(input("\nEnter your Roll No : "))
        self.name = str(input("Enter your Name : "))
        assert self.name != "", " Input should not be empty"
        self.div = str(input("Enter your Std : "))
        assert self.div != "", " Input should not be empty"

        self.sub = marks
        # print ("\nName:",self.name, ", STD:",self.div)

    


# marks = SubjMarks(80, 90, 85)
# student = SMS(1, "Varun", "10b", marks)
# marks2 = SubjMarks(79, 94, 89)
# student2 = SMS(2, "Akshay", "10a", marks2)

# print(student)

# # pyodbc
import pyodbc

conn = pyodbc.connect(
        r'DRIVER={ODBC Driver 17 for SQL Server};'
        r'SERVER=DESKTOP-76DAP13\MSSQLSERVER01;'
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



while True:

    User_Input = input("\nWhat operation would you like to do? (Create/Add/Update/Del/View/Store/Truncate): ")
    cursor = conn.cursor()
    if User_Input.upper() == "ADD":
        student = SMS()
        marks = SubjMarks()        
        query = f"INSERT INTO Student VALUES('{student.name}','{student.div}',{marks.Eng},{marks.Maths},{marks.Sci})"
        cursor.execute(query)
        cursor.commit()
        cursor.close()

    elif User_Input.upper() == "UPDATE":
        inp = int(input("Enter the roll no whose details you want to update: "))
        student = SMS()
        marks = SubjMarks()    
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
        query = f"CREATE TABLE Student (RollNo int IDENTITY(1,1), Name TEXT, STD varchar(max), ENG int, MATHS int, SCI int, PRIMARY KEY (RollNo))"
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
        data = cursor.execute("SELECT * FROM Student")
        data = data.fetchall()
        for row in data:
            for column in row:
                print(column, end=' | ')
            print('\n')
        cursor.commit()
        cursor.close()
        
    new = input("\nDo you want to perform more such operations? (Yes/No): ")
    if new.upper() == "NO":
        break
    elif new.upper() == "YES":
        continue