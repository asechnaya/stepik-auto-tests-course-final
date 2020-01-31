from .base_page import BasePage
from .locators import MainPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage(BasePage):
    def should_be_basket_button(self):
        assert self.is_element_present(*MainPageLocators.BASKET_BUTTON), "Basket link is not presented"

    def should_be_language_link(self):
        assert self.is_element_present(*MainPageLocators.BASKET_BUTTON), "Basket link is not presented"

    def basket_should_be_amount(self):
        assert self.is_element_present(*MainPageLocators.BASKET_AMOUNT), "No text with amount"

    def basket_should_be_equal_zero(self):
        basket_amount = WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located(MainPageLocators.BASKET_AMOUNT)).text
        print(basket_amount)
        assert 'Basket total: £0.00' in basket_amount, "Basket is not empty"


