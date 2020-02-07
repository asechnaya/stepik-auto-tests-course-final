from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert '/login/' in self.browser.current_url, 'Login url is not found'
        # реализуйте проверку на корректный url адрес

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'Login form is not presented'

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REG_FORM), 'Register form is not presented'

    def register_new_user(self, email, password):
        email_input = self.browser.find_element(*LoginPageLocators.EMAIL_REG)
        pass1 = self.browser.find_element(*LoginPageLocators.PASS_REG)
        pass2 = self.browser.find_element(*LoginPageLocators.CONFIRM_PASS_REG)
        email_input.send_keys(email)
        pass1.send_keys(password)
        pass2.send_keys(password)
        submit = self.browser.find_element(*LoginPageLocators.REG_BTN)
        submit.click()

    def user_should_see_register_success_message(self):
        # реализуйте проверку, что сообщение об успехе
        thanks_for_registering = WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located(LoginPageLocators.SUCCESS_MESSAGE)).text
        assert thanks_for_registering == 'Thanks for registering!', \
            "Success message is not presented, but should be"

