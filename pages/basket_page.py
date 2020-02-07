from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from pages.base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_url(self):
        assert '/basket/' in self.browser.current_url, 'Login url is not found'

    def basket_should_be_empty(self):
        basket_is_empty = WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located(BasketPageLocators.BASKET_EMPTY)).text
        assert basket_is_empty == 'Your basket is empty. Continue shopping'
