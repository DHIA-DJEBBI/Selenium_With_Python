import pytest
from page_objects.exeptions_Page import ExpectedPage


class TestExceptions:

    @pytest.mark.exception
    def test_login_access(self, driver):
        """Test case to verify that a new row can be added and displayed successfully."""
        exception_page = ExpectedPage(driver)
        exception_page.open()
        exception_page.add_second_row()
        assert exception_page.is_row2_displayed(), "Row 2 is not displayed"

    @pytest.mark.exception
    @pytest.mark.debug
    def test_element_not_interactable_exception(self, driver):
        """Test case to verify that a user can enter a value in row2 and save it successfully."""
        exception_page = ExpectedPage(driver)
        exception_page.open()
        exception_page.add_second_row()
        exception_page.add_second_food("sushi")
        assert exception_page.get_confirmation_method() == "Row 2 was saved", "Confirmation message is incorrect"

    @pytest.mark.exception
    def test_invalid_element_state_exception(self, driver):
        """Test case to verify that a text field can be cleared and edited."""
        exception_page = ExpectedPage(driver)
        exception_page.open()
        exception_page.add_second_row()

        # Modify the first row text
        exception_page.edit_first_row_text("Dhia DJEBBI")

        # Verify the entered text
        assert exception_page.get_first_row_text() == "Dhia DJEBBI", "Text in row1 was not updated correctly"

    @pytest.mark.exception
    def test_state_element_reference_exception(self, driver):
        """Test case to verify that the instructions element disappears after clicking the 'Add' button."""
        exception_page = ExpectedPage(driver)
        exception_page.open()

        # Capture reference to instructions before clicking Add
        assert exception_page.is_instructions_visible(), "Instructions should be visible before clicking add"

        # Click add button
        exception_page.add_second_row()


        # Verify instructions disappear
        assert not exception_page.is_instructions_visible(), "The instruction element is still displayed after clicking add"



