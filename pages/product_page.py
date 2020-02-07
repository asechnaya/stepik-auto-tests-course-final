from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from .base_page import BasePage
from .locators import BasketPageLocators, ProductPageLocators


class ProductPage(BasePage):
    def click_add_to_the_basket_button(self):
        basket_link = self.browser.find_element(*BasketPageLocators.BASKET_LINK)
        basket_link.click()

    def should_be_basket_page(self):
        assert '/basket/' in self.browser.current_url, 'Basket url is not found'

    def should_be_promo_url(self):
        assert '?promo' in self.browser.current_url, 'Promo url is not found'

    def should_be_basket_link(self):
        assert WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located(BasketPageLocators.BASKET_LINK)), 'Couldn\'t find the basket button'

    def should_be_alert(self):
        assert self.browser.switch_to.alert, 'There is no alert'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_add_to_cart_text(self):
        coders_at_work = WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located(BasketPageLocators.CODERS_AT_WORK_TEXT)).text
        basket_qualifies = WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located(BasketPageLocators.BASKET_QUALIFIES_TEXT)).text
        basket_total = WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located(BasketPageLocators.BASKET_TOTAL_TEXT)).text
        assert coders_at_work == 'Coders at Work has been added to your basket.', self.browser.current_url
        assert basket_qualifies == 'Your basket now qualifies for the Deferred benefit offer offer.', \
            self.browser.current_url
        assert 'Your basket total is now £19.99' in basket_total, self.browser.current_url


