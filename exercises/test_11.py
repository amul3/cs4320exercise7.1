import pytest
import System
import Student
import json

#FAIL
#Tests if the submit_assignment function correctly sets the ontime boolean
def test_submitassignment2(grading_system):
    stuname = 'akend3'
    stupassword = '123454321'
    course =  'databases'
    assignment = 'assignment2'
    submission = 'pineapple'
    subdate = '2/8/20'
    if(grading_system.check_password(stuname,stupassword) == True):
        grading_system.login(stuname,stupassword)
        grading_system.usr.submit_assignment(course,assignment,submission,subdate)
        f = open('Data/users.json')
        data = json.load(f)
        h = open('Data/courses.json')
        classes = json.load(h)
        if(data[stuname]['courses'][course][assignment]['ontime'] == True):
            assert(data[stuname]['courses'][course][assignment]['submission_date'] <= classes[course]['assignments'][assignment]['due_date'])
        else:
            assert(data[stuname]['courses'][course][assignment]['submission_date'] > classes[course]['assignments'][assignment]['due_date'])


@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem

