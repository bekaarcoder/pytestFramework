from selenium.webdriver.common.by import By

from pageObjects.BasePage import BasePage


class SearchCustomerPage(BasePage):
    email_field_id = (By.ID, "SearchEmail")
    first_name_field_id = (By.ID, "SearchFirstName")
    search_button_id = (By.ID, "search-customers")
    email_result_xpath = (By.XPATH, "//div[@class='dataTables_scrollBody']//table//tbody/tr//td[2]")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def set_email(self, email):
        self.do_send_keys(self.email_field_id, email)

    def set_first_name(self, first_name):
        self.do_send_keys(self.first_name_field_id, first_name)

    def click_search_button(self):
        self.do_click(self.search_button_id)

    def verify_email_result(self, email):
        if self.is_visible(self.email_result_xpath):
            if self.driver.find_element(*self.email_result_xpath).text == email:
                return True
            else:
                return False
        else:
            return False
