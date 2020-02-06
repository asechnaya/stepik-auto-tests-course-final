from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):
    def should_be_basket_button(self):
        assert self.is_element_present(*MainPageLocators.BASKET_BUTTON), "Basket link is not presented"

    def should_be_language_link(self):
        assert self.is_element_present(*MainPageLocators.BASKET_BUTTON), "Basket link is not presented"


