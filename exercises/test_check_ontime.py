import pytest
import System
import Student
import json

#Tests if the check_ontime function returns the correct boolean
def test_checkontime(grading_system):
    stuname = 'yted91'
    stupassword = 'imoutofpasswordnames'
    course = 'software_engineering'
    assignment = 'assignment2'
    if(grading_system.check_password(stuname,stupassword) == True):
        grading_system.login(stuname,stupassword)
        f = open('Data/users.json')
        data = json.load(f)
        h = open('Data/courses.json')
        classes = json.load(h)
        subdate = data[stuname]['courses'][course][assignment]['submission_date']
        duedate = classes[course]['assignments'][assignment]['due_date']
        b1 = grading_system.usr.check_ontime(subdate,duedate)
        b2 = data[stuname]['courses'][course][assignment]['ontime']
        assert(b1 == b2)


@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem

