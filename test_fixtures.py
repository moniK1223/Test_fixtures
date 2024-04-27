# def outer(func):
#     def wrapper(*args, **kwargs):
#         print('hello world')
#         func(*args, **kwargs)
#     return wrapper
#
# @outer
# def test_spam():
#     print('spam executing')
#
# @outer
# def test_sample():
#     print('sample executing')
#
#
# ## collected 2 items
# ## test_fixtures.py::test_spam     hello world         spam executing          PASSED
# ## test_fixtures.py::test_sample   hello world         sample executing        PASSED


#--------------------------------------------------------------------------------
'''
fixtures : It is a built-in decorator used to perform setup and teardown operations
•	Pytest fixture is a callable (normally a function or a generator) decorated with inbuilt
        pytest decorator @fixture.
•	Fixtures are accessed by test functions by passing the name of the fixture to test functions
        as argument.
•	Fixtures are used to run a piece of code repeatedly before and/or after every
        test method/class/module/session based on the defined scope.

'''
import time
import pytest

# @pytest.fixture()
# def greet():
#     print('Good afternoon')
#
# def test_login(greet):
#     print('login executing')
#
# def test_logout(greet):
#     print('logout executing')
#
# ## collected 2 items
# ## test_fixtures.py::test_login    Good afternoon          login executing      PASSED
# ## test_fixtures.py::test_logout   Good afternoon          logout executing     PASSED
#
# #------------------------------------------------------------------
# ## NOTE : test_functions/methods will take fixtures as parameters
#
# #------------------------------------------------------------------
#
# @pytest.fixture()
# def greet():
#     print('Good afternoon')
#
# def test_login(greet):
#     print('login executing')
#
# def test_signup():
#     print('signup executing')
#
# def test_logout(greet):
#     print('logout executing')
#
# ## collected 3 items
# ## test_fixtures.py::test_login Good afternoon         login executing         PASSED
# ## test_fixtures.py::test_signup                       signup executing        PASSED
# ## test_fixtures.py::test_logout Good afternoon        logout executing        PASSED
#
# #-----------------------------------------------------------------
#
# @pytest.fixture()
# def greet():
#     print('Good afternoon')
#
# def test_login(greet):
#     print('login executing')
#
# def test_signup(greet):
#     print('signup executing')
#
# def test_logout(greet):
#     print('logout executing')
#
# ## collected 3 items
# ## test_fixtures.py::test_login Good afternoon         login executing         PASSED
# ## test_fixtures.py::test_signup Good afternoon        signup executing        PASSED
# ## test_fixtures.py::test_logout Good afternoon        logout executing        PASSED
#
# #----------------------------------------------------------------------
# @pytest.fixture(autouse=True)
# def greet():
#     print('Good afternoon')
#
# def test_login():
#     print('login executing')
#
# def test_signup():
#     print('signup executing')
#
# def test_logout():
#     print('logout executing')
#
# ## collected 3 items
# ## test_fixtures.py::test_login Good afternoon         login executing         PASSED
# ## test_fixtures.py::test_signup Good afternoon        signup executing        PASSED
# ## test_fixtures.py::test_logout Good afternoon        logout executing        PASSED
#
# #--------------------------------------------------------------------------
# ## NOTE : fixture has a parameter called autouse.
# ## when we give autouse=True, the fixture will be applied for all the test functions present in that module
#
# #------------------------------------------------------------------------------
# @pytest.fixture()
# def greet():
#     print('Good afternoon')
#
#
# class TestGmail:
#
#     def test_login(self, greet):
#         print('login executing')
#
#     def test_signup(self, greet):
#         print('signup executing')
#
#     def test_logout(self, greet):
#         print('logout executing')
#
# ## collected 3 items
# ## test_fixtures.py::test_login Good afternoon         login executing         PASSED
# ## test_fixtures.py::test_signup Good afternoon        signup executing        PASSED
# ## test_fixtures.py::test_logout Good afternoon        logout executing        PASSED
#
# #-----------------------------------------------------------------
# @pytest.fixture(autouse=True)
# def greet():
#     print('Good afternoon')
#
# class TestGmail:
#
#     def test_login(self):
#         print('login executing')
#
#     def test_signup(self):
#         print('signup executing')
#
#     def test_logout(self):
#         print('logout executing')
# #
# # ## collected 3 items
# # ## test_fixtures.py::test_login Good afternoon         login executing         PASSED
# # ## test_fixtures.py::test_signup Good afternoon        signup executing        PASSED
# # ## test_fixtures.py::test_logout Good afternoon        logout executing        PASSED
#
# #-----------------------------------------------------------------------------------
#
# @pytest.fixture(autouse=True)
# def greet():
#     print('Good afternoon')     ## setup
#     yield
#     print('Good evening')       ## teardown
#
# def test_login():
#     print('login executing')
#
# def test_signup():
#     print('signup executing')
#
# def test_logout():
#     print('logout executing')
#
# ## collected 3 items
# ## test_fixtures.py::test_login Good afternoon         login executing     PASSEDGood evening
# ## test_fixtures.py::test_signup Good afternoon        signup executing    PASSEDGood evening
# ## test_fixtures.py::test_logout Good afternoon        logout executing    PASSEDGood evening

#--------------------------------------------------------------

# @pytest.fixture(autouse=True)
# def greet():
#     print('Good afternoon')
#
# class TestGmail:
#
#     def test_login(self):
#         print('login executing')
#
#     def test_signup(self):
#         print('signup executing')
#
# class TestSample:
#
#     def test_reg(self):
#         print('registration executing')
#
#     def test_logout(self):
#         print('logout executing')

## collected 4 items
## test_fixtures.py::TestGmail::test_login Good afternoon          login executing         PASSED
## test_fixtures.py::TestGmail::test_signup Good afternoon         signup executing        PASSED
## test_fixtures.py::TestSample::test_reg Good afternoon           registration executing  PASSED
## test_fixtures.py::TestSample::test_logout Good afternoon        logout executing        PASSED

#------------------------------------------------------------------
# @pytest.fixture(scope='class', autouse=True)
# def greet():
#     print('Good afternoon')
#     yield
#     print('Good evening')
#
# class TestGmail:
#
#     def test_login(self):
#         print('login executing')
#
#     def test_signup(self):
#         print('signup executing')
#
# class TestSample:
#
#     def test_reg(self):
#         print('registration executing')
#
#     def test_logout(self):
#         print('logout executing')


## collected 4 items
## test_fixtures.py::TestGmail::test_login Good afternoon      login executing         PASSED
## test_fixtures.py::TestGmail::test_signup                    signup executing        PASSEDGood evening
##
## test_fixtures.py::TestSample::test_reg Good afternoon       registration executing  PASSED
## test_fixtures.py::TestSample::test_logout                   logout executing        PASSEDGood evening


#-----------------------------------------------------------------------------------
## NOTE : By default, the value of scope is function, thats why the fixture will be applied for
## each function/methods when we use autouse=True
## If we want to execute the fixture on a class level, then we change the value of scope to class
## When we give scope="class", the fixture will be applied once before the execution of the class.


#-------------------------------------------------------------------------------------------
from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

@pytest.fixture(scope='class')
def _drivers():
    driver = webdriver.Chrome(options=opts)
    driver.get('https://demowebshop.tricentis.com/')
    time.sleep(2)
    yield driver
    driver.close()

## _drivers --> driver = webdriver.Chrome(options=opts)

class TestDemoRegister:

    def test_click_register(self, _drivers):        ## _drivers --> driver=webdriver.Chrome(options=opts)
        _drivers.find_element('xpath', '//a[text()="Register"]').click()
        time.sleep(2)

    def test_gender_btn(self, _drivers):            ## _drivers --> driver
        _drivers.find_element('xpath', '//input[@id="gender-female"]').click()

    def test_firstname(self, _drivers):
        _drivers.find_element('xpath', '//input[@id="FirstName"]').send_keys('Megha')

    def test_lastname(self, _drivers):
        _drivers.find_element('xpath', '//input[@id="LastName"]').send_keys('SriShankar')

    def test_register_email(self, _drivers):
        _drivers.find_element('xpath', '//input[@id="Email"]').send_keys('meghashankar@gmail.com')

    def test_register_pwd(self, _drivers):
        _drivers.find_element('xpath', '//input[@id="Password"]').send_keys('megha@12345')

    def test_confirm_pwd(self, _drivers):
        _drivers.find_element('xpath', '//input[@id="ConfirmPassword"]').send_keys('megha@12345')

    time.sleep(3)


class TestDemoLogin:

    def test_click_login(self, _drivers):
        _drivers.find_element('xpath', '//a[text()="Log in"]').click()
        time.sleep(1)

    def test_login_email(self, _drivers):
        _drivers.find_element('xpath', '//input[@id="Email"]').send_keys('meghashankar@gmail.com')

    def test_login_pwd(self, _drivers):
        _drivers.find_element('xpath', '//input[@id="Password"]').send_keys('megha@12345')


#------------------------------------------

# @pytest.fixture(autouse=True)
# def greet():
#     print('Good afternoon')     ## setup
#     yield
#     print('Good evening')       ## teardown
#
# def test_login():
#     print('login executing')
#
# def test_logout():
#     print('logout executing')
#










































































