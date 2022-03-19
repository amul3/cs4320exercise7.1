import pytest
import System
import Student
import json

#Tests if the check_grades function returns the correct grades for the correct user for the correct course
def test_checkgrades(grading_system):
    stuname = 'yted91'
    stupassword = 'imoutofpasswordnames'
    course = 'software_engineering'
    if(grading_system.check_password(stuname,stupassword) == True):
        grading_system.login(stuname,stupassword)
        f = open('Data/users.json')
        data = json.load(f)
        funcgrades = grading_system.usr.check_grades(course)
        courseassign = data[stuname]['courses'][course]
        gradesarr = []
        for assign in courseassign:
            gr = courseassign[assign]['grade']
            gradesarr.append([assign, gr])
        assert(gradesarr == funcgrades)


@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem

