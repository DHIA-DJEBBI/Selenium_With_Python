from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from page_objects.base_page import BasePage

class LoginPage(BasePage):
    # Private variables for encapsulation
    __url = "https://practicetestautomation.com/practice-test-login/"
    __username_Field = (By.ID, "username")
    __password_locator = (By.NAME, "password")
    __Submit_btn = (By.XPATH, "//*[@id='submit']")
    __error_message = (By.ID, "error")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self._driver = driver

    def open(self):
        """Opens the login page"""
        super()._open_url(self.__url)

    def execute_login(self, username: str, password: str):
        """Fills in the login form and submits"""
        super()._type(self.__username_Field, username, time=5)
        super()._type(self.__password_locator, password, time=5)
        super()._click(self.__Submit_btn , time=5)

    def get_error_message(self)-> str :
        return super()._get_text(self.__error_message, 3)

