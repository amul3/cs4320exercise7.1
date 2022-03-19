import pytest
import Staff
import System
import json

#Tests if the change_grade function changes the correct grade for the correct user
def test_changegrade(grading_system):
    staffname = 'goggins'
    staffpassword = 'augurrox'
    user = 'akend3'
    course =  'databases'
    assignment = 'assignment2'
    grade = '20'
    if(grading_system.check_password(staffname,staffpassword) == True):
        grading_system.login(staffname,staffpassword)
        f = open('Data/users.json')
        data = json.load(f)
        grading_system.usr.change_grade(user,course,assignment,grade)
        f = open('Data/users.json')
        data = json.load(f)
        assert(data[user]['courses'][course][assignment][grade] == grade)


@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem

