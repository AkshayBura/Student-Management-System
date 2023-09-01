class SubjMarks:
    def __init__(self, Eng, Maths, Sci):
        self.Eng = Eng
        self.Maths = Maths
        self.Sci = Sci
        print(f"\nMarks in the subjects: English - {self.Eng} , Maths - {self.Maths} , Science - {self.Sci}", end='\n')

# class ColgMarks(SubjMarks):
#     def __init__(self, Eng, Maths, Sci, it):
#         super().__init__(Eng, Maths, Sci)
#         self.it = it

class SMS:
    def __init__(self, roll:int, name:str, div: str, marks: SubjMarks):
        self.roll = roll
        self.name = name
        self.div = div
        self.sub = marks
        print ("\nRoll No:",roll, ", Name:",name, ", STD:",div)
        
    

marks = SubjMarks(80, 90, 85)
student = SMS(1, "Varun", "10b", marks)
marks2 = SubjMarks(79, 94, 89)
student = SMS(2, "Akshay", "10a", marks2)

print(student)

# pyodbc
import pyodbc

conn = pyodbc.connect(
        r'DRIVER={ODBC Driver 17 for SQL Server};'
        r'SERVER=DESKTOP-76DAP13\MSSQLSERVER01;'
        # 'Integrated Security = True;'
        r'Trusted_Connection=Yes;'
        r'Connection Timeout=30;'
        r'DATABASE=StudentDB;'
)

# conn_str = (
#     r'DRIVER={ODBC Driver 17 for SQL Server};'
#     r'SERVER=DESKTOP-76DAP13\MSSQLSERVER01;'
#     r'DATABASE=StudenDB;'
#     r'Trusted_Connection=yes;'
#     r'Connection Timeout=30;'
# )

# conn = pyodbc.connect(conn_str)
print(student.sub)

# cursor = conn.cursor()
# #query = f"CREATE TABLE Student (RollNo int,Name TEXT,STD varchar(32),SubjectMarks int);"
# # query = f"SELECT * from Persons;"
# query = f"INSERT INTO student VALUES({student.roll},'{student.name}','{student.div}')"
# print(query)
# cursor.execute(query)
# cursor.commit()
# cursor.close()

