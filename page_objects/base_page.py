from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver: WebDriver):
        self._driver = driver

    def _find(self, locator: tuple) -> WebElement:
        return self._driver.find_element(*locator)

    def _type(self, locator: tuple, text: str, time: int = 10):
        self.wait_until_element_is_visible(locator, time)
        self._find(locator).send_keys(text)

    def _click(self, locator: tuple, time: int = 5):
        self.wait_until_element_is_visible(locator, time)
        self._find(locator).click()

    def wait_until_element_is_visible(self, locator: tuple, time: int = 10):
        WebDriverWait(self._driver, time).until(EC.visibility_of_element_located(locator))

    @property
    def current_url(self) -> str:
        return self._driver.current_url

    def _is_element_displayed(self, locator: tuple) -> bool:
        try:
            return self._find(locator).is_displayed()
        except NoSuchElementException:
            return False

    def _open_url(self, url: str):
        self._driver.get(url)

    def _get_text(self, locator: tuple, time: int = 5) -> str:
        self.wait_until_element_is_visible(locator, time)
        return self._find(locator).text

    def _clear(self, locator: tuple, time: int = 5):
        self.wait_until_element_is_visible(locator, time)
        self._find(locator).clear()
