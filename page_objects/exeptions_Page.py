from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class ExpectedPage(BasePage):
    __url = "https://practicetestautomation.com/practice-test-exceptions/"

    __add_btn = (By.ID, "add_btn")
    __row_2_input_element = (By.XPATH, "//*[@id='row2']/input")
    __row2_edit_BTN = (By.XPATH, "//*[@id='edit_btn']") # //*[@id="save_btn"]
    __row_1_input_element = (By.XPATH, "//*[@id='row1']/input")
    __row1_Save_Btn = (By.XPATH, "//button[@id='save_btn']")
    __Id_confirmation = (By.ID, "confirmation")
    __instructions = (By.ID, "instructions")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super()._open_url(self.__url)

    def add_second_row(self):
        super()._click(self.__add_btn)
        super().wait_until_element_is_visible(self.__row_2_input_element)


    def is_row2_displayed(self) -> bool:
        return super()._is_element_displayed(self.__row_2_input_element)

    def add_second_food(self, food: str):
        print("Typing food in row2 input field...")
        super()._type(self.__row_2_input_element, food)

        print("Waiting for 'Edit' button to be clickable...")
        super().wait_until_element_is_visible(self.__row2_edit_BTN, 5)

        print("Clicking 'Edit' button...")
        super()._click(self.__row2_edit_BTN)

        print("Waiting for confirmation message to appear...")
        super().wait_until_element_is_visible(self.__Id_confirmation)

    def get_confirmation_method(self) -> str:
        return super()._get_text(self.__Id_confirmation)

    def edit_first_row_text(self, text: str):
        super()._click(self.__row1_Save_Btn)
        super()._clear(self.__row_1_input_element)
        super()._type(self.__row_1_input_element, text)

    def get_first_row_text(self) -> str:
        return super()._get_text(self.__row_1_input_element)

    def is_instructions_visible(self) -> bool:
        return super()._is_element_displayed(self.__instructions)
