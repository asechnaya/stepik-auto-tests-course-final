from .base_page import BasePage
from .locators import BasketPageLocators
import time

class PageObject(BasePage):
    # Описать в нем метод для добавления в корзину.
    def click_the_basket_button(self):
        basket_link = self.browser.find_element(*BasketPageLocators.BASKET_LINK)
        basket_link.click()

    def should_be_basket_page(self):
        self.should_be_promo_url()
        self.should_be_basket_link()

    def should_be_promo_url(self):
        assert '?promo=newYear' in self.browser.current_url, "Login url is not found"
        # реализуйте проверку на корректный url адрес

    def should_be_basket_link(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_LINK), "Couldn't find the basket button"

    def should_be_alert(self):
        assert self.browser.switch_to.alert, "There is no alert"


