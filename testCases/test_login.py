import pytest
import time
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObjects.LoginPage import Login
from utilities.Readconfigfile import ReadValue
from utilities.Logger import LogGen


class Test_Url_Login:
    username = ReadValue.getUsername()
    password = ReadValue.getPassword()
    Url= ReadValue.getUrl()
    log = LogGen.loggen()

    def test_Url_001(self, setup,):
        # self.log.debug("debug")
        # self.log.info("info")
        # self.log.warning("warning")
        # self.log.error("error")
        # self.log.critical("debug")
        self.log.info(" Opening Browser ")
        self.driver = setup
        self.driver.get(self.Url)
        time.sleep(1)
        self.log.info(" Going to Url")
        self.lp = Login(self.driver)
        self.lp.Enter_UserName(self.username)
        self.log.info("Enter_UserName"+ self.username)
        self.lp.Enter_Password(self.password)
        self.log.info("Enter_Password" + self.password)
        self.lp.Click_Login()
        self.log.info("Click on login Button" )
        self.driver.save_screenshot("C:\\Users\HP\\OneDrive\\Desktop\\letskodeit\\Screenshots\\test_Url_001_loginpage.png")
        time.sleep(2)
        if self.lp.login_status() == True:
            self.log.info(" test_Url_001 is Passed ")
            time.sleep(1)
            self.driver.save_screenshot("C:\\Users\HP\\OneDrive\\Desktop\\letskodeit\\Screenshots\\test_Url_001_Pass.png")
            self.lp.Click_Menu_Button()
            self.log.info(" Click on menu button ")
            time.sleep(1)
            self.lp.Click_logout_Button()
            self.log.info(" Click on Logout button ")
            assert True
        else:
            self.log.info(" test_Url_001 is Failed ")
            self.driver.save_screenshot("C:\\Users\HP\\OneDrive\\Desktop\\letskodeit\\Screenshots\\test_Url_001_Fail.png")
            assert False
        self.driver.close()
        self.log.info(" test_Url_001 is completed ")
        self.driver.quit()

## pytest -v -s -rA --html=Report/MyReport.html -n=2

# =========================================================================================================================


# import pytest
# import time
# from selenium.common import NoSuchElementException
# from selenium.webdriver.chrome import webdriver
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
#
# class Test_Url_Login:
#     def test_Url_001(self):
#         chrome_options = webdriver.ChromeOptions()
#         chrome_options.add_argument("headless")
#         driver = webdriver.Chrome(options=chrome_options)
#         # driver = webdriver.Chrome()
#         driver.get("https://www.letskodeit.com/login")
#         driver.find_element(By.ID, "email").send_keys("rvshinde007@gmail.com")
#         driver.find_element(By.NAME, "password").send_keys("007@Ravishinde")
#         driver.find_element(By.XPATH, "//button[@id='login']").click()
#         driver.maximize_window()
#         time.sleep(3)
#
#         try:
#             driver.find_element(By.XPATH, "//button[@id='dropdownMenu1']//a[@class='dynamic-link']")
#             login = True
#         except NoSuchElementException:
#             login = False
#             pass
#         time.sleep(6)
#         if login == True:
#             driver.find_element(By.XPATH, "//button[@id='dropdownMenu1']//a[@class='dynamic-link']").click()
#             driver.find_element(By.XPATH, "//a[normalize-space()='Logout']").click()
#             assert True
#         else:
#             assert False
