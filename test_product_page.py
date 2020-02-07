import time

import pytest

from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.product_page import ProductPage


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        # открыть страницу регистрации
        link = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
        register_page = LoginPage(browser, link)
        register_page.open()
        # зарегистрировать нового пользователя
        email = f'{time.time()}@fakemail.org'
        password = str(time.time())
        register_page.register_new_user(email, password)
        register_page.user_should_see_register_success_message()
        # проверить, что пользователь залогинен
        register_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        page = ProductPage(browser, link)
        page.open()
        # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear"
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.click_add_to_the_basket_button()
        product_page.should_be_alert()
        product_page.solve_quiz_and_get_code()
        product_page.should_be_add_to_cart_text()
        product_page.basket_should_have_amount()


def test_guest_cant_see_success_message(browser):
    # Открываем страницу товара
    browser.delete_all_cookies()
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    page.open()
    # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    page.should_not_be_success_message()


@pytest.mark.need_review
@pytest.mark.parametrize(
    'promo_offer', [
        "0", "1", "2", "3", "4", "5", "6",
        pytest.param("7", marks=pytest.mark.xfail),
        "8", "9"
    ]
)
def test_guest_can_add_product_to_basket(browser, promo_offer):
    browser.delete_all_cookies()
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
    page = MainPage(browser, link)
    page.open()
    product_page = ProductPage(browser, browser.current_url)
    product_page.click_add_to_the_basket_button()
    product_page.should_be_alert()
    product_page.solve_quiz_and_get_code()
    product_page.should_be_add_to_cart_text() 


@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    # Открываем страницу товара
    browser.delete_all_cookies()
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = MainPage(browser, link)
    page.open()
    # Добавляем товар в корзину
    basket_page = ProductPage(browser, browser.current_url)
    basket_page.should_be_basket_page()
    basket_page.click_add_to_the_basket_button()
    basket_page.should_be_alert()
    basket_page.solve_quiz_and_get_code()
    # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    basket_page.should_not_be_success_message()


@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
    # Открываем страницу товара
    browser.delete_all_cookies()
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = MainPage(browser, link)
    page.open()
    # Добавляем товар в корзину
    basket_page = ProductPage(browser, browser.current_url)
    basket_page.should_be_basket_page()
    basket_page.click_add_to_the_basket_button()
    basket_page.should_be_alert()
    basket_page.solve_quiz_and_get_code()
    basket_page.should_be_add_to_cart_text()
    # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    time.sleep(1)
    basket_page.should_be_disappeared_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    browser.delete_all_cookies()
    link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    browser.delete_all_cookies()
    link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
    login_page.should_be_login_url()
    login_page.should_be_login_form()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    # Гость открывает главную страницу
    link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
    page = ProductPage(browser, link)
    page.open()
    # Меняем язык на Британский Английский
    page.should_be_brenglish_language()
    page.should_be_basket_link()
    # Ожидаем, что в корзине нет товаров    ||  Your basket is empty
    page.basket_should_have_amount()
    page.basket_should_be_equal_zero()
    # Переходит в корзину по кнопке в шапке сайта
    page.go_to_basket()
    basket_page = BasketPage(browser, link)
    basket_page.should_be_basket_url()
    # Ожидаем, что есть текст о том что корзина пуста
    basket_page.basket_should_be_empty()

