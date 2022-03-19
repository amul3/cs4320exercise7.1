import pytest
import System
import json

#Tests if the check_password function returns the correct boolean
def test_checkpassword(grading_system):
    username = 'goggins'
    password =  'augurrox'
    if(grading_system.check_password(username,password) == True):
        f = open('Data/users.json')
        data = json.load(f)
        assert(data[username]['password'] == password)
    else:
        f = open('Data/users.json')
        data = json.load(f)
        if(username in data):
            assert(data[username]['password'] != password)
        


@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem

