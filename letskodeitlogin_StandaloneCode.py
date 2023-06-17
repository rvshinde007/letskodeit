import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# 1 opening browser
driver = webdriver.Chrome()
# 2 going to url
driver.get("https://www.letskodeit.com/login")
driver.maximize_window()
# Enter UserName
WebDriverWait(driver,10).until(expected_conditions.presence_of_element_located((By.ID, "email")))
driver.find_element(By.ID, "email").send_keys("rvshinde007@gmail.com")
# Enter Password
driver.find_element(By.NAME, "password").send_keys("007@Ravishinde")
# Click on login button
driver.find_element(By.XPATH, "//button[@id='login']").click()
time.sleep(2)
# # Click on menu button
driver.find_element(By.XPATH, "//button[@id='dropdownMenu1']//a[@class='dynamic-link']").click()
# # Click on logout button
driver.find_element(By.XPATH, "//a[normalize-space()='Logout']").click()

driver.close()
driver.quit()







