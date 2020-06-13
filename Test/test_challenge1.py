'''

'''
import pytest
from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.common.keys import Keys



@pytest.fixture
#special functions that do teardowns
def driver():
    #before each test
    _driver = webdriver.Chrome() #give the driver to the test

    #after each test
    yield _driver.quit()



def test_google_search(driver):
    driver = webdriver.Chrome() #can be deleted bc of line 12
    driver.get('https://google.com')
    search_field = driver.find_element_by_css_selector(by.css_selector, "[name='q']")
    search_field.send_keys("puppies", Keys.Enter)
    #check/assertion
    assert 'puppies' in driver.title
    driver.quit()



def test_google_search_pylenium(py):
    py.visit('https://google.com')
    py.get("[name='q']").type('puppies', Keys.ENTER)
    assert py.should().contain_title('puppies')
