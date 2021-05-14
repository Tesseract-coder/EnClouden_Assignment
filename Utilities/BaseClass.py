import inspect
import logging
import pytest


@pytest.mark.usefixtures("setup")
class BaseClass:

    def Get_Parameterized_Xpath(self, mainpath, *argument):
        """
        This Keyword Returns Final Xpath with Parameterized value
        Where $$1, $$2 .... will get replace by Parameters
        :param mainpath: This is Generic Xpath which contains $$1, $$2 ..
        :param argument: List of Parameters
        :return: Final Xpath
        """
        dollars = ['$$1', '$$2', '$$3', '$$4', '$$5']
        for i in range(len(argument)):
            mainpath = mainpath.replace(dollars[i], argument[i])
        return mainpath
