import pytest
import System
import Professor
import json

#FAIL
#Tests if the add_student function adds a student to the correct course
def test_addstudent(grading_system):
    staffname = 'goggins'
    staffpassword = 'augurrox'
    course =  'software_engineering'
    student = 'akend3'
    if(grading_system.check_password(staffname,staffpassword) == True):
        grading_system.login(staffname,staffpassword)
        grading_system.usr.add_student(student,course)
        f = open('Data/users.json')
        data = json.load(f)
        assert(data[student]['role'] == 'student')
        #assert(course in data[staffname]['courses'])
        assert(course in data[student]['courses'])
        

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem

