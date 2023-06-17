import pytest
import time
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObjects.LoginPage import Login
from utilities.Readconfigfile import ReadValue
from utilities.Logger import LogGen

class Test_Login_Params:
    Url= ReadValue.getUrl()
    log = LogGen.loggen()

    def test_login_params_002(self, setup,getDataForLogin):
        self.log.info(" Opening Browser ")
        self.driver = setup
        self.driver.get(self.Url)
        time.sleep(1)
        self.log.info(" Going to Url")
        self.lp = Login(self.driver)
        self.lp.Enter_UserName(getDataForLogin[0])
        self.log.info("Enter_UserName"+ getDataForLogin[0])
        self.lp.Enter_Password(getDataForLogin[1])
        self.log.info("Enter_Password" + getDataForLogin[1])
        self.lp.Click_Login()
        self.log.info("Click on login Button" )
        self.driver.save_screenshot("C:\\Users\HP\\OneDrive\\Desktop\\letskodeit\\Screenshots\\test_login_params_002_loginpage.png")
        time.sleep(2)
        login_status=[]
        if self.lp.login_status() == True:
            if getDataForLogin[2]== "Pass":
                login_status.append("Pass")
                time.sleep(1)
                self.driver.save_screenshot("C:\\Users\HP\\OneDrive\\Desktop\\letskodeit\\Screenshots\\test_login_params_002_Pass.png")
                self.lp.Click_Menu_Button()
                self.log.info(" Click on menu button ")
                time.sleep(1)
                self.lp.Click_logout_Button()
                self.log.info(" Click on Logout button ")
            elif getDataForLogin[2] == "Fail":
                login_status.append("Fail")
                time.sleep(1)
                self.driver.save_screenshot("C:\\Users\HP\\OneDrive\\Desktop\\letskodeit\\Screenshots\\test_login_params_002_Pass.png")
                self.lp.Click_Menu_Button()
                self.log.info(" Click on menu button ")
                time.sleep(1)
                self.lp.Click_logout_Button()
                self.log.info(" Click on Logout button ")
        else:
            if getDataForLogin[2] == "Fail":
                login_status.append("Pass")
                self.driver.save_screenshot("C:\\Users\HP\\OneDrive\\Desktop\\letskodeit\\Screenshots\\test_login_params_002_Fail.png")
            elif getDataForLogin[2] == "Pass":
                login_status.append("Fail")
                self.driver.save_screenshot("C:\\Users\HP\\OneDrive\\Desktop\\letskodeit\\Screenshots\\test_login_params_002_Fail.png")
        print(login_status)

        if "Fail" not in login_status:
            self.log.info(" test_login_params_002 is Passed ")
            assert True
        else:
            self.log.info(" test_login_params_002 is Failed ")
            assert False
        self.driver.close()
        self.log.info(" test_login_params_002 is completed ")
        self.driver.quit()

        # #   pytest -v -rA -s -n=4  testCases/test_login_param.py --browser chrome --html=Report/report.html