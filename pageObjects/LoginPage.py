from selenium import webdriver


class LoginPage:
    email_field_id = "Email"
    password_field_id = "Password"
    login_btn_xpath = "//input[@value='Log in']"
    logout_link_xpath = "//a[text()='Logout']"

    def __init__(self, driver):
        self.driver = driver

    def set_email(self, email):
        self.driver.find_element_by_id(self.email_field_id).clear()
        self.driver.find_element_by_id(self.email_field_id).send_keys(email)

    def set_password(self, password):
        self.driver.find_element_by_id(self.password_field_id).clear()
        self.driver.find_element_by_id(self.password_field_id).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_xpath(self.login_btn_xpath).click()

    def click_logout(self):
        self.driver.find_element_by_xpath(self.logout_link_xpath).click()