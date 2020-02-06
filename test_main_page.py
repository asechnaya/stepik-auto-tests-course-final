from pages.basket_page import BasketPage
from pages.main_page import MainPage
from pages.login_page import LoginPage
import pytest


@pytest.mark.login_guest
class TestLoginFromMainPage:
    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com"
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        browser.delete_all_cookies()
        link = "http://selenium1py.pythonanywhere.com"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()



def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    # Гость открывает главную страницу
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = MainPage(browser, link)
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
