# This module contains functions to lazily generate student data.
from data_processing import display_students
def student_generator(student_list, major):
    """
    Generate student records filtered by major lazily for memory efficiency
    using a Python generator.
    """
    newList=(student for student in student_list if major in student)
    display_students(newList)
