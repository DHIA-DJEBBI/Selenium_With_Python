import time
#from selenium import webdriver
#from selenium.webdriver.chromium.service import ChromiumService
from selenium.webdriver.common.by import By
import pytest
from page_objects.login_page import LoginPage


class TestNegativeScenarios:

    @pytest.mark.login
    @pytest.mark.negative
    @pytest.mark.parametrize("userName, password , Expected_error_msg",
                             [("Dhia", "Password123", "Your username is invalid!"),
                              ("student", "worlllldddd", "Your password is invalid!")])
    def test_negative_login(self, driver, userName, password, Expected_error_msg):
        """Test invalid login attempts and verify error messages."""

        login_page = LoginPage(driver)  # FIXED INSTANCE NAMING
        login_page.open()
        login_page.execute_login(userName, password)

        error_message = login_page.get_error_message()  # FIXED METHOD CALL
        assert error_message == Expected_error_msg, f"Expected '{Expected_error_msg}', but got '{error_message}' instead."

        # Navigate to the WebPage
        #driver.get("https://practicetestautomation.com/practice-test-login/")
        #time.sleep(2)
        #userName_Locator = driver.find_element(By.ID, "username")
        #userName_Locator.send_keys(userName)
        #password_locator = driver.find_element(By.NAME, "password")
        #password_locator.send_keys(password)
        #Submit_Button_Locator = driver.find_element(By.XPATH, "//*[@id='submit']")
        #Submit_Button_Locator.click()
        #time.sleep(2)


        #username_Error = driver.find_element(By.ID, "error")
        #time.sleep(3)
        #assert username_Error.is_displayed(), "the error message is not displayed but it should"



        #Error_msg_Text = username_Error.text
        #assert Error_msg_Text == Expected_error_msg, "error message is not expected"


    def test_negative_username(self, driver):
        # driver = webdriver.Chrome()

        # Navigate to the WebPage
        driver.get("https://practicetestautomation.com/practice-test-login/")
        time.sleep(2)
        userName_Locator = driver.find_element(By.ID, "username")
        userName_Locator.send_keys("Dhia")
        password_locator = driver.find_element(By.NAME, "password")
        password_locator.send_keys("Password123")
        Submit_Button_Locator = driver.find_element(By.XPATH, "//*[@id='submit']")
        Submit_Button_Locator.click()
        time.sleep(2)
        username_Error = driver.find_element(By.ID, "error")
        assert username_Error.is_displayed(), "the error message is not displayed but it should"

        Error_msg_Text = username_Error.text

        assert Error_msg_Text == "Your username is invalid!", "error message is not expected"






