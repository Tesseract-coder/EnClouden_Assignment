import time
from datetime import datetime, date, timedelta
from selenium import webdriver

from PageObject.HomePage import HomePage
from Utilities.BaseClass import BaseClass
from Utilities.Keywords import Keywords


class TestClass(Keywords):

    def test_CitySale(self, getData):

        driver = self.driver
        HP_obj = HomePage(driver)
        '''
        Implementing Try Except block because some City names are not present on UI
        '''
        try:
            ''' Getting Dynamic City Name'''
            CityElement = HP_obj.getCity(getData)
            self.GenericWait(driver, CityElement)
            self.Click_Element(driver, CityElement)

            ''' Get Total number of Sale record present for specific Town '''
            totalcolumns = HP_obj.getTotalRowCount()
            for i in range(len(totalcolumns)):
                Date_Element = HP_obj.getDate(str(i + 2))
                DateText = self.Get_Text(driver, Date_Element)

                ''' Validating current record date is within 7 days or not '''
                if self.is_date_valid(DateText):

                    ViewNoticeElement = HP_obj.getNotice(str(i + 2))
                    nextURL = self.Get_Element_Attribute(driver, ViewNoticeElement, "href")

                    ''' Opening View Full Notice on new tab '''

                    script = 'window.open("' + nextURL + '", "_blank");'
                    print(script)
                    driver.execute_script(script)
                else:
                    print("For town " + getData + " there is no sale record within 7 days")

        except:
            print("Town with name " + getData + " is not present on Homepage")
