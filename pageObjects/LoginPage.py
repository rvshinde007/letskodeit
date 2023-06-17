from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Login:
    Text_username_ID = (By.ID, "email")
    Text_Password_Name = (By.NAME, "password")
    Click_Login_Xpath = (By.XPATH, "//button[@id='login']")
    Click_menu_Xpath = (By.XPATH, "//button[@id='dropdownMenu1']//a[@class='dynamic-link']")
    Click_Logout_Xpath = (By.XPATH, "//a[normalize-space()='Logout']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def Enter_UserName(self, email):
        self.wait.until(expected_conditions.presence_of_element_located(self.Text_username_ID))
        self.driver.find_element(*Login.Text_username_ID).send_keys(email)

    def Enter_Password(self, password):
        self.driver.find_element(*Login.Text_Password_Name).send_keys(password)

    def Click_Login(self):
        self.driver.find_element(*Login.Click_Login_Xpath).click()

    def login_status(self):
        try:
            self.driver.find_element(*Login.Click_menu_Xpath)
            return True
        except NoSuchElementException:
            return False

    def Click_Menu_Button(self):
        self.wait.until(expected_conditions.presence_of_element_located(self.Click_menu_Xpath))
        self.driver.find_element(*Login.Click_menu_Xpath).click()

    def Click_logout_Button(self):
        self.driver.find_element(*Login.Click_Logout_Xpath).click()
