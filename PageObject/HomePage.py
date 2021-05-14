from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Utilities.BaseClass import BaseClass


class HomePage(BaseClass):

    def __init__(self, driver):
        self.driver = driver

    Date = "//table[contains(@id,'GridView1')]//tr[$$1]//td[2]/span"
    Generic_City = "//a[contains(text(),'$$1')]"
    ViewNotice = "//table[contains(@id,'GridView1')]//tr[$$1]//td[5]/a"
    TotalRows = "//table[contains(@id,'GridView1')]//tr//td[2]/span"

    def getTotalRowCount(self):
        return self.driver.find_elements_by_xpath(HomePage.TotalRows)

    def getCity(self, cityname):
        fianlpath = self.Get_Parameterized_Xpath(HomePage.Generic_City, cityname)
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.presence_of_element_located((By.XPATH, fianlpath)))
        return fianlpath

    def getDate(self, counter):
        fianlpath = self.Get_Parameterized_Xpath(HomePage.Date, counter)
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.presence_of_element_located((By.XPATH, fianlpath)))
        return fianlpath

    def getNotice(self, counter):
        fianlpath = self.Get_Parameterized_Xpath(HomePage.ViewNotice, counter)
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.presence_of_element_located((By.XPATH, fianlpath)))
        return fianlpath
