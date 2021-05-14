from datetime import datetime, timedelta, date

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

from Utilities.BaseClass import BaseClass


class Keywords(BaseClass):

    def GenericWait(self, driver, locator):
        """ Explicit Wait Keyword for All the elements"""
        wait = WebDriverWait(driver, 20)
        wait.until(EC.presence_of_element_located((By.XPATH,locator)))

    def Click_Element(self, driver, locator):
        """ generic Keyword Created to Click on the element
        Driver will be input along with elements
        """
        wait = WebDriverWait(driver, 20)
        wait.until(EC.presence_of_element_located((By.XPATH,locator)))
        wait.until(EC.element_to_be_clickable((By.XPATH,locator)))
        driver.find_element_by_xpath(locator).click()

    def Get_Text(self, driver, locator):
        wait = WebDriverWait(driver, 20)
        wait.until(EC.presence_of_element_located((By.XPATH,locator)))
        return driver.find_element_by_xpath(locator).text

    def Get_Element_Attribute(self, driver, locator, Attribute):
        wait = WebDriverWait(driver, 20)
        wait.until(EC.presence_of_element_located((By.XPATH, locator)))
        return driver.find_element_by_xpath(locator).get_attribute(Attribute)


    def is_date_valid(self, dateonui):
        dateonui = dateonui.split()
        dateonui = dateonui[0]
        splitteddateonui = dateonui.split("/")
        month = splitteddateonui[0]
        datee = splitteddateonui[1]
        year = splitteddateonui[2]

        finaldateonui = month + '-' + datee + '-' + year

        date_dt3 = datetime.strptime(finaldateonui, '%m-%d-%Y')
        date_dt3 = datetime.date(date_dt3)

        todaysdate = date.today()
        maxAcceptabledate = todaysdate + timedelta(days=7)

        if date_dt3 <= maxAcceptabledate:
            return True
        else:
            return False
