import pytest
from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

driver = None

@pytest.fixture()
def setup(request):
    global driver
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

    driver.get("https://sso.eservices.jud.ct.gov/Foreclosures/Public/PendPostbyTownList.aspx")
    driver.implicitly_wait(10)
    request.cls.driver = driver


@pytest.fixture(params=['Milford', 'Trumbull', 'Norwalk', 'Stamford', 'Shelton', 'Fairfield'])
def getData(request):
    return request.param
