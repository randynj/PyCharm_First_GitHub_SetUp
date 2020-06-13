from selenium import webdriver


def test_google_search(driver):
    driver = webdriver.Chrome() #can be deleted bc of line 12
    driver.get('https://google.com')
    search_field = driver.find_element_by_css_selector(by.css_selector, "[name='q']")
    search_field.send_keys("puppies", Keys.Enter)
    #check/assertion
    assert 'puppies' in driver.title
    driver.quit()
