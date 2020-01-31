from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LANGUAGE = (By.XPATH, "xpath=//select[@name='language']")
    BASKET_BUTTON = (By.XPATH, '//*[@id="default"]/header/div[1]/div/div[2]/span/a')
    BASKET_AMOUNT = (By.CSS_SELECTOR, ".basket-mini")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REG_FORM = (By.CSS_SELECTOR, "#register_form")


class BasketPageLocators:
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-add-to-basket")
    CODERS_AT_WORK_TEXT = (By.XPATH, '/html/body/div[2]/div/div[1]/div[1]/div')
    BASKET_QUALIFIES_TEXT = (By.XPATH, '/html/body/div[2]/div/div[1]/div[2]/div')
    BASKET_TOTAL_TEXT = (By.XPATH, '/html/body/div[2]/div/div[1]/div[3]/div')
    BASKET_EMPTY = (By.CSS_SELECTOR, '#content_inner > p')
    GO_BTN = (By.CSS_SELECTOR, '#language_selector > button')
    LANGUAGE_ACCEPT = (By.XPATH, '//*[@id="language_selector"]/button')


class ProductPageLocators:
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alertinner')


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
