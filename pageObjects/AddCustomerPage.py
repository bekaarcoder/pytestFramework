from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from pageObjects.BasePage import BasePage


class AddCustomerPage(BasePage):
    customer_menu_xpath = (By.XPATH, "//div[@class='sidebar']//a[@href='#']//span[text()='Customers']")
    customer_submenu_xpath = (By.XPATH, "//a[@href='/Admin/Customer/List']//span[text()='Customers']")
    add_new_button_xpath = (By.XPATH, "//a[@href='/Admin/Customer/Create']")
    new_customer_page_title = (By.XPATH, "//h1[contains(text(), 'Add a new customer')]");
    email_field_id = (By.ID, "Email")
    password_field_id = (By.ID, "Password")
    first_name_field_id = (By.ID, "FirstName")
    last_name_field_id = (By.ID, "LastName")
    gender_role_male_id = (By.ID, "Gender_Male")
    gender_role_female_id = (By.ID, "Gender_Female")
    dob_field_id = (By.ID, "DateOfBirth")
    company_field_id = (By.ID, "Company")
    tax_checkbox_id = (By.ID, "IsTaxExempt")
    customer_roles_select_xpath = (By.XPATH, "(//div[@class='k-multiselect-wrap k-floatwrap'])[2]")
    manager_vendor_select_xpath = (By.XPATH, "//select[@name='VendorId']")
    admin_comment_field_id = (By.ID, "AdminComment")
    save_button_xpath = (By.XPATH, "//button[@name='save']")
    success_alert_xpath = (By.XPATH, "//div[contains(@class, 'alert-success')]")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_on_customers_menu(self):
        self.do_click(self.customer_menu_xpath)

    def click_on_customers_submenu(self):
        self.do_click(self.customer_submenu_xpath)

    def click_on_add_new(self):
        self.do_click(self.add_new_button_xpath)

    def verify_add_customer_page(self):
        return self.is_visible(self.new_customer_page_title)

    def set_email(self, email):
        self.do_send_keys(self.email_field_id, email)

    def set_password(self, password):
        self.do_send_keys(self.password_field_id, password)

    def set_first_name(self, first_name):
        self.do_send_keys(self.first_name_field_id, first_name)

    def set_last_name(self, last_name):
        self.do_send_keys(self.last_name_field_id, last_name)

    def select_gender(self, gender):
        if gender == "male":
            self.do_click(self.gender_role_male_id)
        elif gender == "female":
            self.do_click(self.gender_role_female_id)
        else:
            self.do_click(self.gender_role_male_id)

    def set_dob(self, dob):
        self.do_send_keys(self.dob_field_id, dob)

    def set_company_name(self, company_name):
        self.do_send_keys(self.company_field_id, company_name)

    def select_customer_roles(self, role):
        self.do_click(self.customer_roles_select_xpath)
        role_xpath = (By.XPATH, "//ul[@id='SelectedCustomerRoleIds_listbox']//li[contains(text(), '"+role+"')]")
        self.do_click(role_xpath)

    def select_manager_of_vendor(self, manager):
        self.select_option(self.manager_vendor_select_xpath, manager)

    def set_admin_comment(self, comment):
        self.do_send_keys(self.admin_comment_field_id, comment)

    def click_save(self):
        self.do_click(self.save_button_xpath)

    def verify_alert(self):
        return self.is_visible(self.success_alert_xpath)
