import pytest
import System
import Staff
import json

#Tests if the check_grades function returns the correct grades for the correct student for the correct course only if the user is a staff member for that course
def test_dropstudent2(grading_system):
    staffname = 'calyam'
    staffpassword = '#yeet'
    course =  'databases'
    student = 'akend3'
    if(grading_system.check_password(staffname,staffpassword) == True):
        grading_system.login(staffname,staffpassword)
        f = open('Data/users.json')
        data = json.load(f)
        funcgrades = grading_system.usr.check_grades(student,course)
        courseassign = data[student]['courses'][course]
        gradesarr = []
        for assign in courseassign:
            gr = courseassign[assign]['grade']
            gradesarr.append([assign, gr])
        assert(gradesarr == funcgrades)
        assert(course in data[staffname]['courses'])



@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
