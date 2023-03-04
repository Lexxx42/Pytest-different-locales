''' Tests for purchase order. '''

import time
from selenium.webdriver.common.by import By

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_guest_should_be_able_to_add_product_to_basket(browser):
    ''' Test checking that button Add to basket is on the page. '''
    browser.get(link)
    time.sleep(30)
    browser.find_element(By.CSS_SELECTOR, '.btn-add-to-basket')
