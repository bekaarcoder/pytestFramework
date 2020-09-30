import time

import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities import excelUtils
from utilities.Logger import LogGen


class Test_002_Login_DDT:
    baseurl = ReadConfig.get_application_url()
    path = ".//TestData//LoginData.xlsx"
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_login_ddt(self, setup):
        self.logger.info("**********Test_002_Login_DDT***********")
        self.logger.info("**********Verify Login Test DDT***********")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.lp = LoginPage(self.driver)
        list_status = []

        self.rows = excelUtils.get_row_count(self.path, "login_data")
        print("Number of rows:", self.rows)

        for r in range(2, self.rows+1):
            self.email = excelUtils.read_data(self.path, "login_data", r, 1)
            self.password = excelUtils.read_data(self.path, "login_data", r, 2)
            self.expected = excelUtils.read_data(self.path, "login_data", r, 3)
            print(self.email, self.password, self.expected)

            self.lp.set_email(self.email)
            self.lp.set_password(self.password)
            self.lp.click_login()
            time.sleep(5)

            actual_title = self.driver.title
            if actual_title == "Dashboard / nopCommerce administration":
                if self.expected == "Pass":
                    self.lp.click_logout()
                    list_status.append("Pass")
                    self.logger.info("**********Test " + str(r-1) + " Passed***********")
                elif self.expected == "Fail":
                    self.lp.click_logout()
                    list_status.append("Fail")
                    self.logger.error("**********Test " + str(r - 1) + " Failed***********")
            elif actual_title != "Dashboard / nopCommerce administration":
                if self.expected == "Pass":
                    self.lp.click_logout()
                    list_status.append("Fail")
                    self.logger.error("**********Test " + str(r - 1) + " Failed***********")
                elif self.expected == "Fail":
                    list_status.append("Pass")
                    self.logger.info("**********Test " + str(r - 1) + " Passed***********")

        if "Fail" not in list_status:
            assert True
            self.driver.close()
            self.logger.info("**********Test Finished***********")
        else:
            assert False
            self.driver.close()
            self.logger.info("**********Test Finished***********")
