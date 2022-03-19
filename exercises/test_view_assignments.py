import pytest
import System
import Student
import json

#FAIL
#Tests if the view_assignments function returns the correct assignments for the correct course
def test_viewassignments(grading_system):
    stuname = 'yted91'
    stupassword = 'imoutofpasswordnames'
    course = 'software_engineering'
    if(grading_system.check_password(stuname,stupassword) == True):
        grading_system.login(stuname,stupassword)
        f = open('Data/users.json')
        data = json.load(f)
        h = open('Data/courses.json')
        classes = json.load(h)
        funcassign = grading_system.usr.view_assignments(course)
        courseassign = classes[course]['assignments']
        assignarr = []
        for assign in courseassign:
            dd = courseassign[assign]['due_date']
            assignarr.append([assign, dd])
        assert(assignarr == funcassign)


@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem

