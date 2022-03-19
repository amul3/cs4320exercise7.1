import pytest
import System
import Professor
import json

#Tests if the drop_student function drops a student from the correct course
def test_dropstudent(grading_system):
    staffname = 'calyam'
    staffpassword = '#yeet'
    course =  'databases'
    student = 'akend3'
    if(grading_system.check_password(staffname,staffpassword) == True):
        grading_system.login(staffname,staffpassword)
        grading_system.usr.drop_student(student,course)
        f = open('Data/users.json')
        data = json.load(f)
        assert(data[student]['role'] == 'student')
        assert(course not in data[student]['courses'])
        

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
