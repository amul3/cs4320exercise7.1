import pytest
import System
import json

#Tests if the correct user is created for program
def test_login(grading_system):
    username = 'akend3'
    password =  '123454321'
    if(grading_system.check_password(username,password) == True):
        grading_system.login(username,password)
        f = open('Data/users.json')
        data = json.load(f)
        assert(grading_system.usr.name == username)
        assert(data[username]['courses'] == grading_system.usr.courses)
        assert(data[username]['password'] == grading_system.usr.password)


@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
