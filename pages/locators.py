from selenium.webdriver.common.by import By



class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REG_FORM = (By.CSS_SELECTOR, "#register_form")


class BasketPageLocators:
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-add-to-basket")
    CODERS_AT_WORK_TEXT = (By.XPATH, '/html/body/div[2]/div/div[1]/div[1]/div')
    BASKET_QUALIFIES_TEXT = (By.XPATH, '/html/body/div[2]/div/div[1]/div[2]/div')
    BASKET_TOTAL_TEXT = (By.XPATH, '/html/body/div[2]/div/div[1]/div[3]/div')


class ProductPageLocators:
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alertinner')


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
