import math
from typing import Union

from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

from pages.locators import (
    BasePageLocators,
    ProductPageLocators,
    MainPageLocators,
    BasketPageLocators,
)


class BasePage:
    def __init__(self, browser: Union[webdriver.Chrome, webdriver.Firefox], url: str, timeout: int = 10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
        except NoAlertPresentException:
            print("No second alert presented")
        else:
            alert_text = alert.text
            print(f"{alert_text}")
            alert.accept()

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until_not(
                EC.presence_of_element_located((how, what))
            )
        except TimeoutException:
            return False
        return True

    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def go_to_basket(self):
        link = self.browser.find_element(*MainPageLocators.BASKET_BUTTON)
        link.click()

    def should_be_brenglish_language(self):
        select = Select(self.browser.find_element(*BasketPageLocators.LANGUAGE))
        select.select_by_visible_text('British English')
        go_button = self.browser.find_element(*BasketPageLocators.LANGUAGE_ACCEPT)
        go_button.click()

    def basket_should_have_amount(self):
        assert self.is_element_present(*MainPageLocators.BASKET_AMOUNT), "No text with amount"

    def basket_should_be_equal_zero(self):
        basket_amount = WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located(MainPageLocators.BASKET_AMOUNT)).text
        assert 'Basket total: £0.00' in basket_amount, "Basket is not empty"

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                     " probably unauthorised user"

