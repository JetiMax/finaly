import pytest
from selenium import webdriver
import time


@pytest.fixture(scope="function")
def driver(request):
    path = str(request.fspath)
    time.sleep(5)
    driver = webdriver.Chrome('C:/Users/slvit/PycharmProjects/pro/chrome/chromedriver.exe')
    #driver = webdriver.chrome(f"{path[:path.find('page_object')]}page_object/chrom/chromedriver.exe")
    driver.maximize_window()
    driver.implictly_wait(5)
    yield driver
