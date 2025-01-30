# Open browser
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
#from Webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome()
# Navigate to the WebPage
driver.get("https://practicetestautomation.com/practice-test-login/")
time.sleep(2)
userName_Locator  = driver.find_element(By.ID , "username")
userName_Locator.send_keys("student")
password_locator = driver.find_element(By.NAME, "password")
password_locator.send_keys("Password123")
Submit_Button_Locator = driver.find_element(By.XPATH, "//*[@id='submit']")
Submit_Button_Locator.click()
currentURL = driver.current_url
assert  currentURL =="https://practicetestautomation.com/logged-in-successfully/"

#print(currentURL)

text_locator = driver.find_element(By.TAG_NAME, "h1")
print(text_locator.text)
Logout_Btn = driver.find_element(By.LINK_TEXT, "Log out")
assert Logout_Btn.is_displayed()

print(Logout_Btn.text)




"""
Type username student into Username field
Type password Password123 into Password field
Push Submit button
Verify new page URL contains practicetestautomation.com/logged-in-successfully/
Verify new page contains expected text ('Congratulations' or 'successfully logged in')
Verify button Log out is displayed on the new page
"""








