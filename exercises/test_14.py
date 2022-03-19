import pytest
import Staff
import System
import json

#Tests if the change_grade function only changes a grade for a student from a course if the user is a staff member for that course
def test_changegrade2(grading_system):
    staffname = 'calyam'
    staffpassword = '#yeet'
    user = 'akend3'
    course =  'databases'
    assignment = 'assignment2'
    grade = '20'
    if(grading_system.check_password(staffname,staffpassword) == True):
        grading_system.login(staffname,staffpassword)
        f = open('Data/users.json')
        data = json.load(f)
        grading_system.usr.change_grade(user,course,assignment,grade)
        assert(course in data[staffname]['courses'])


@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
