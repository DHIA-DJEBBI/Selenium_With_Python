from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver  # Use Chrome WebDriver or remote WebDriver

from page_objects.base_page import BasePage


# Assuming BasePage is in a separate file

class LoggedInSuccessfullyPage(BasePage):
    _url = "https://practicetestautomation.com/logged-in-successfully/"

    __header_locator = (By.TAG_NAME, "h1")
    __logout_btn_locator = (By.LINK_TEXT, "Log out")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)  # Initialize the parent class

    @property
    def expected_url(self) -> str:
        """Returns the expected URL of the page."""
        return self._url

    @property
    def header(self) -> str:
        """Gets the header text of the page."""
        return self._get_text(self.__header_locator)

    def is_logout_btn_displayed(self) -> bool:
        """Checks if the logout button is displayed."""
        return self._is_logout_btn_displayed(self.__logout_btn_locator)
