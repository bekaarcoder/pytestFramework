import time
import pytest
from pageObjects.AddCustomerPage import AddCustomerPage
from pageObjects.LoginPage import LoginPage
from pageObjects.SearchCustomerPage import SearchCustomerPage
from utilities.readProperties import ReadConfig


class Test_004_Search_Customer:
    baseurl = ReadConfig.get_application_url()
    email = ReadConfig.get_email()
    password = ReadConfig.get_password()

    @pytest.mark.regression
    def test_search_customer_by_email(self, setup):
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()

        # login to application
        self.lp = LoginPage(self.driver)
        self.lp.set_email(self.email)
        self.lp.set_password(self.password)
        self.lp.click_login()
        time.sleep(5)

        # search customer
        self.addCustomer = AddCustomerPage(self.driver)
        self.addCustomer.click_on_customers_menu()
        self.addCustomer.click_on_customers_submenu()

        self.searchCustomer = SearchCustomerPage(self.driver)
        self.searchCustomer.set_email("victoria_victoria@nopCommerce.com")
        self.searchCustomer.click_search_button()

        if self.searchCustomer.verify_email_result("victoria_victoria@nopCommerce.com"):
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_search_customer_by_email.png")
            assert False

        self.driver.close()
