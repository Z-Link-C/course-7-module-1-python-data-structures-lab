from student_data import students
from data_generator import student_generator
from filters import filter_students_by_major
from set_operations import unique_majors
class Main():
    while True:
        uInput=input("""please choose what you want to do:
    1. Student filter based on inputted major
    2. """)
        if uInput=='1':
            filter=input("please input a major: ")        
            filter_students_by_major(student_list=students, major=filter)
        elif uInput=='2':
            filter=input("please input a major: ")        
            student_generator(student_list=students, major=filter )
        elif uInput=='3':
            unique_majors(student_list=students)
        else: 
            break