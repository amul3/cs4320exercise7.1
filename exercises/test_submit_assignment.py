import pytest
import System
import Student
import json

#PASS
#Tests if the submit_assignment function updates the correct assignment, submission, submission date, and in the correct course
def test_submitassignment(grading_system):
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
        assert(data[stuname]['courses'][course][assignment]['submission_date'] == subdate)
        assert(data[stuname]['courses'][course][assignment]['submission'] == submission)


@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem

