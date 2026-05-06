# This module contains operations related to sets.
from data_processing import display_students

def unique_majors(student_list):
    """
    Return a set of unique student majors using set comprehension.
    Extract the major field from each student record.
    """
    
    unique={student[2] for student in student_list}
    

    return print(list(unique))
