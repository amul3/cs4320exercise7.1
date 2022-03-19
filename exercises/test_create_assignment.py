import pytest
import System
import Staff
import json

#Tests if the create_assignment function creates an assignment with the correct due date in the correct course
def test_createassignment(grading_system):
    staffname = 'goggins'
    staffpassword = 'augurrox'
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
        assert(classes[course]['assignments'][assignmentname]['due_date'] == duedate)
        

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem

