import pytest
import System
import Staff
import json

#FAIL
#Tests if the create_assignment function only creates an assignment for a course if the user is a staff member for that course
def test_createassignment2(grading_system):
    staffname = 'calyam'
    staffpassword = '#yeet'
    course =  'databases'
    assignmentname = 'pineapple'
    duedate = '1/9/22'
    grade = '20'
    if(grading_system.check_password(staffname,staffpassword) == True):
        grading_system.login(staffname,staffpassword)
        grading_system.usr.create_assignment(assignmentname,duedate,course)
        f = open('Data/users.json')
        data = json.load(f)
        h = open('Data/courses.json')
        classes = json.load(h)
        assert(course in data[staffname]['courses'])
        

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
