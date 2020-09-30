import string
import time
import random
import pytest
from pageObjects.AddCustomerPage import AddCustomerPage
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig


class Test_003_Add_Customer:
    baseurl = ReadConfig.get_application_url()
    email = ReadConfig.get_email()
    password = ReadConfig.get_password()

    # def test_verify_add_customer_page(self, setup):
    #     self.driver = setup
    #     self.driver.get(self.baseurl)
    #     self.driver.maximize_window()
    #
    #     # login to application
    #     self.lp = LoginPage(self.driver)
    #     self.lp.set_email(self.email)
    #     self.lp.set_password(self.password)
    #     self.lp.click_login()
    #     time.sleep(5)
    #
    #     # Verify add new customer page
    #     self.addCustomer = AddCustomerPage(self.driver)
    #     self.addCustomer.click_on_customers_menu()
    #     self.addCustomer.click_on_customers_submenu()
    #     self.addCustomer.click_on_add_new()
    #     assert self.addCustomer.verify_add_customer_page()
    #
    #     self.driver.close()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_add_customer(self, setup):
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()

        # login to application
        self.lp = LoginPage(self.driver)
        self.lp.set_email(self.email)
        self.lp.set_password(self.password)
        self.lp.click_login()
        time.sleep(5)

        # add new customer
        self.addCustomer = AddCustomerPage(self.driver)
        self.addCustomer.click_on_customers_menu()
        self.addCustomer.click_on_customers_submenu()
        self.addCustomer.click_on_add_new()

        self.full_name = random_generator()
        self.email = self.full_name + "@gmail.com"
        print(self.full_name, self.email)
        self.addCustomer.set_email(self.email)
        self.addCustomer.set_password("hello123")
        self.addCustomer.set_first_name(self.full_name[:5])
        self.addCustomer.set_last_name(self.full_name[5:])
        self.addCustomer.select_gender("male")
        self.addCustomer.set_dob("9/9/1990")
        self.addCustomer.set_company_name("AutomationQA")
        self.addCustomer.select_customer_roles("Administrators")
        self.addCustomer.select_manager_of_vendor("Vendor 1")
        self.addCustomer.set_admin_comment("Adding a new customer using automation script")

        self.addCustomer.click_save()

        if self.addCustomer.verify_alert():
            self.success_msg = self.driver.find_element_by_xpath("//div[contains(@class, 'alert-success')]").text.strip()
            if "The new customer has been added successfully" in self.success_msg:
                assert True
            else:
                self.driver.save_screenshot(".\\Screenshots\\" + "test_add_customer.png")
                assert False
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_add_customer.png")
            assert False

        self.driver.close()


def random_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))
