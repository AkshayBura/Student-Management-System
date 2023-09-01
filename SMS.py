stud_det = {}

def add_details(roll, name, div):
    stud_det[roll] = {'name' : name, 'div' : div}
    print("\nStudent Details has been added successfully... ")
    print(stud_det)
    
def del_details(roll):
    if roll in stud_det:
        del(stud_det[roll])
        print(f"\nSuccessfully deleted details of roll no. {roll}")
        print(stud_det)
    else:
        print("\nRoll No. which you entered is not present.")

def upd_details(roll, name, div):
    if roll in stud_det:
        stud_det[roll] = {'name' : name, 'div' : div}
        print("\nSudent Details have been updated successfully")
        print(stud_det)
    else:
        add_details(roll, name, div)

add_details(1, 'Akshay', '9a')
add_details(2, 'Abhay', '9c')

del_details(3)
del_details(1)

upd_details(1, 'Akshay', '9b')
upd_details(2, 'Varun', '9c')
