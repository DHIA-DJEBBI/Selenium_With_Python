import pytest
from page_objects.logged_in_successfully import LoggedInSuccessfullyPage
from page_objects.login_page import LoginPage


class TestPositiveScenarios:

    @pytest.mark.login
    def test_positive_login(self, driver):
        """Tests a valid login scenario."""

        login_page = LoginPage(driver)

        # Open login page
        login_page.open()  # Fixed instance method call

        # Execute login
        login_page.execute_login("student", "Password123")  # Fixed instance method call

        # Validate that the login was successful
        logged_in_page = LoggedInSuccessfullyPage(driver)

        assert logged_in_page.header == "Logged In Successfully", "Header is incorrect"
        assert logged_in_page.is_logout_btn_displayed(), "Logout button should be visible"







        #driver = webdriver.Chrome()

        # Navigate to the WebPage

        # """ driver.get("https://practicetestautomation.com/practice-test-login/")
        #time.sleep(2)


       # userName_Locator  = driver.find_element(By.ID , "username")
        #userName_Locator.send_keys("student")
        #password_locator = driver.find_element(By.NAME, "password")
        #password_locator.send_keys("Password123")
        #Submit_Button_Locator = driver.find_element(By.XPATH, "//*[@id='submit']")
       # Submit_Button_Locator.click()
        #currentURL = driver.current_url
        #assert  currentURL =="https://practicetestautomation.com/logged-in-successfully/"

        #print(currentURL)
        #text_locator = driver.find_element(By.TAG_NAME, "h1")
        #print(text_locator.text)
        #Logout_Btn = driver.find_element(By.LINK_TEXT, "Log out")
        #assert Logout_Btn.is_displayed()

        #print(Logout_Btn.text) """



