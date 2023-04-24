from selenium.webdriver.common.by import By
from pom.base.base_page import BasePage
from pom.pages.admin.admin_header import AdminHeader


class Nationalities(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    NATIONALITIES_GENERAL_BUTTON = (By.XPATH, "//a[text()='Nationalities']")
    ADD_BUTTON = (By.CSS_SELECTOR, "button[class='oxd-button oxd-button--medium oxd-button--secondary']")
    NATIONALITY_INPUT = (By.CSS_SELECTOR, "div[class='oxd-form-row'] div div:nth-child(2) input")
    SUBMIT_NATIONALITY_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    RECORDS_FOUND = (By.CSS_SELECTOR, "span[class='oxd-text oxd-text--span']")
    DELETE_EDIT_BUTTONS = (By.CSS_SELECTOR, "button[class='oxd-icon-button oxd-table-cell-action-space']")
    NATIONALITY_LIST = (By.CSS_SELECTOR, "div[class ^= 'oxd-table-row']")
    PAGINATION_BUTTONS = (By.CSS_SELECTOR,
                          "button[class='oxd-pagination-page-item oxd-pagination-page-item--previous-next']")
    PAGINATION_BUTTON_1 = (By.XPATH, "//button[text()='1']")
    NATIONALITY_UPDATED_SUCCESS = (By.CSS_SELECTOR, "div[id='oxd-toaster_1']")
    CANCEL_DELETION = (By.CSS_SELECTOR, "div[class='orangehrm-modal-footer'] button")
    APPROVE_DELETION = (By.CSS_SELECTOR, "div[class='orangehrm-modal-footer'] button:nth-child(2)")
    DELETION_SUCCESS_MESSAGE = (By.XPATH, "//p[text()='Successfully Deleted']")
    CHECKBOXES = (By.CSS_SELECTOR, "input[type='checkbox']")
    CHECKBOX_CLICKS = (By.CSS_SELECTOR, "i[class^='oxd-icon bi-check'")


    def init_admin_page_nationalities(self):
        admin_header = AdminHeader(self.driver)
        admin_header.go_to('Nationalities')

    def add_nationality(self, new_nationality: str):
        add_button = self.wait.wait_for_element_to_be_clickable(self.ADD_BUTTON)
        record_found_text = self.wait.wait_for_element(self.RECORDS_FOUND).text
        self.initial_record_number = int(record_found_text[1:4])
        add_button.click()
        input_field = self.wait.wait_for_element_to_be_clickable(self.NATIONALITY_INPUT)
        input_field.click()
        self.clear_field(input_field)
        input_field.send_keys(new_nationality)
        self.find_element_by(self.SUBMIT_NATIONALITY_BUTTON).click()

    def is_record_number_updated(self):
        record_found_text = self.wait.wait_for_element(self.RECORDS_FOUND).text
        updated_record_number = int(record_found_text[1:4])
        return updated_record_number == self.initial_record_number+1


    def edit_nationality_name(self, nationality: str, new_nationality_name: str):
        """

        :param nationality: The nationality that needs to be edited.
        :param new_nationality_name: The new name for editing the existing nationality.
        :return: 'No such nationality', if wrong name has been passed.
        """
        self.wait.wait_for_element_to_be_clickable(self.NATIONALITIES_GENERAL_BUTTON).click()
        edit_button = None
        first_page = True
        nationality_found = False
        while not nationality_found:
            list_of_nationality_elements = self.wait.wait_for_elements(self.NATIONALITY_LIST)
            list_of_edit_buttons = self.find_list_of_elements(self.DELETE_EDIT_BUTTONS)[1::2]
            list_of_nationalities = [nation.text for nation in list_of_nationality_elements]
            for nation in list_of_nationalities:
                if nation == nationality:
                    index = list_of_nationalities.index(nationality)
                    edit_button = list_of_edit_buttons[index-1]
                    nationality_found = True
                    break
            if not nationality_found:
                right_pagination = self.find_list_of_elements(self.PAGINATION_BUTTONS)
                if first_page:
                    right_pagination[-1].click()
                    first_page = False
                elif len(right_pagination) > 1:
                    right_pagination[-1].click()
                else:
                    print("No such nationality.")
                    return
        self.driver.execute_script("arguments[0].scrollIntoView();", edit_button)
        self.driver.execute_script("window.scrollBy(0, -150)")
        self.get_actions().scroll_to_element(edit_button)
        edit_button.click()
        input_field = self.wait.wait_for_element_to_be_clickable(self.NATIONALITY_INPUT)
        input_field.click()
        self.clear_field(input_field)
        input_field.send_keys(new_nationality_name)
        self.find_element_by(self.SUBMIT_NATIONALITY_BUTTON).click()

    def is_edit_nationality_success_message_displayed(self):
        message = self.wait.wait_for_element_to_be_visible(self.NATIONALITY_UPDATED_SUCCESS)
        return message.is_displayed()

    def is_nationality_present(self, nationality: str):
        """

        :param nationality: The nationality that needs to be checked whether is edited or not.
        :return: Returns True if the edited nationality is found in the nationality lists throughout all pages.
        """
        self.wait.wait_for_element_to_be_clickable(self.NATIONALITIES_GENERAL_BUTTON).click()
        first_page = True
        while True:
            list_of_nationality_elements = self.wait.wait_for_elements(self.NATIONALITY_LIST)
            for nation in list_of_nationality_elements:
                if nation.text == nationality:
                    return nation.text == nationality
            right_pagination = self.find_list_of_elements(self.PAGINATION_BUTTONS)
            if first_page:
                right_pagination[-1].click()
                first_page = False
            elif len(right_pagination) > 1:
                right_pagination[-1].click()
            else:
                print("No such edited nationality.")
                return False

    def delete_nationality(self, nationality_name: str):
        """

        :param nationality_name: The nationality that needs to be deleted.
        :return:
        """
        self.wait.wait_for_element_to_be_clickable(self.NATIONALITIES_GENERAL_BUTTON).click()
        delete_button = None
        first_page = True
        nationality_found = False
        while not nationality_found:
            list_of_nationality_elements = self.wait.wait_for_elements(self.NATIONALITY_LIST)
            list_of_delete_buttons = self.find_list_of_elements(self.DELETE_EDIT_BUTTONS)[0::2]
            list_of_nationalities = [nation.text for nation in list_of_nationality_elements]
            for nation in list_of_nationalities:
                if nation == nationality_name:
                    index = list_of_nationalities.index(nationality_name)
                    delete_button = list_of_delete_buttons[index - 1]
                    nationality_found = True
                    break
            if not nationality_found:
                right_pagination = self.find_list_of_elements(self.PAGINATION_BUTTONS)
                if first_page:
                    right_pagination[-1].click()
                    first_page = False
                elif len(right_pagination) > 1:
                    right_pagination[-1].click()
                else:
                    print("No such nationality.")
                    return
        self.driver.execute_script("arguments[0].scrollIntoView();", delete_button)
        self.driver.execute_script("window.scrollBy(0, -150)")
        self.get_actions().scroll_to_element(delete_button)
        delete_button.click()
        self.wait.wait_for_element_to_be_clickable(self.CANCEL_DELETION).click()
        delete_button.click()
        self.wait.wait_for_element_to_be_clickable(self.APPROVE_DELETION).click()

    def is_delete_nationality_success_message_displayed(self):
        message = self.wait.wait_for_element_to_be_visible(self.DELETION_SUCCESS_MESSAGE)
        return message.is_displayed()

    def select_checkboxes(self, nationality_name: str):
        """

        :param nationality_name: The nationality that needs to be checked.
        :return:
        """
        self.wait.wait_for_element_to_be_clickable(self.NATIONALITIES_GENERAL_BUTTON).click()
        checkboxes = self.wait.wait_for_elements(self.CHECKBOXES)
        checkbox_clicks = self.find_list_of_elements(self.CHECKBOX_CLICKS)
        # below verifies that all the checkboxes are not selected
        for checkbox in checkboxes:
            if checkbox.is_selected():
                index = checkboxes.index(checkbox)
                checkbox_clicks[index].click()
        first_page = True
        nationality_found = False
        while not nationality_found:
            list_of_nationality_elements = self.wait.wait_for_elements(self.NATIONALITY_LIST)
            list_of_nationalities = [nation.text for nation in list_of_nationality_elements]
            checkbox_clicks = self.find_list_of_elements(self.CHECKBOX_CLICKS)
            for nation in list_of_nationalities:
                if nation == nationality_name:
                    index = list_of_nationalities.index(nationality_name)
                    self.driver.execute_script("arguments[0].scrollIntoView();", checkbox_clicks[index])
                    self.driver.execute_script("window.scrollBy(0, -150)")
                    checkbox_clicks[index].click()
                    nationality_found = True
                    break
            if not nationality_found:
                right_pagination = self.find_list_of_elements(self.PAGINATION_BUTTONS)
                if first_page:
                    right_pagination[-1].click()
                    first_page = False
                elif len(right_pagination) > 1:
                    right_pagination[-1].click()
                else:
                    print("No such nationality.")
                    return

    def is_nationality_selected(self, nationality_name: str):
        """

        :param nationality_name: The nationality that needs to be checked whether selected or not.
        :return:
        """
        checkboxes = self.wait.wait_for_elements(self.CHECKBOXES)
        list_of_nationality_elements = self.wait.wait_for_elements(self.NATIONALITY_LIST)
        list_of_nationalities = [nation.text for nation in list_of_nationality_elements]
        for nation in list_of_nationalities:
            if nation == nationality_name:
                index = list_of_nationalities.index(nationality_name)
                return checkboxes[index].is_selected()
