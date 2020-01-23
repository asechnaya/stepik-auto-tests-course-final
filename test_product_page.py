import pytest
import time
from pages.main_page import MainPage
from pages.product_page import ProductPage


# @pytest.mark.parametrize('promo_offer', ["0", "1", "2", "3", "4", "5", "6",
#                                          pytest.param("7", marks=pytest.mark.xfail),
#                                          "8", "9"])
# def test_guest_can_add_product_to_basket(browser, promo_offer):
#     browser.delete_all_cookies()
#     link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
# # def test_guest_can_go_to_login_page(browser):
# #     link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"  #  -- с этой ссылкой работает все ок
#     # link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
#     page = MainPage(browser, link)
#     page.open()
#     basketpage = PageObject(browser, browser.current_url)
#     basketpage.should_be_basket_page()
#     basketpage.click_the_basket_button()
#     basketpage.should_be_alert()
#     page.solve_quiz_and_get_code()
#     basketpage.should_be_add_to_cart_text()
#
#

@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    # Открываем страницу товара
    browser.delete_all_cookies()
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = MainPage(browser, link)
    page.open()
    # Добавляем товар в корзину
    basketpage = ProductPage(browser, browser.current_url)
    basketpage.should_be_basket_page()
    basketpage.click_the_basket_button()
    basketpage.should_be_alert()
    page.solve_quiz_and_get_code()
    # basketpage.should_be_add_to_cart_text()
    # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    basketpage.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    # Открываем страницу товара
    browser.delete_all_cookies()
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = MainPage(browser, link)
    page.open()
    basketpage = ProductPage(browser, browser.current_url)
    basketpage.should_be_basket_page()
    # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    basketpage.should_not_be_success_message()


@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
    # Открываем страницу товара
    browser.delete_all_cookies()
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = MainPage(browser, link)
    page.open()
    # Добавляем товар в корзину
    basketpage = ProductPage(browser, browser.current_url)
    basketpage.should_be_basket_page()
    basketpage.click_the_basket_button()
    basketpage.should_be_alert()
    page.solve_quiz_and_get_code()
    basketpage.should_be_add_to_cart_text()
    # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    time.sleep(1)
    basketpage.should_be_disappeared_success_message()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
    page.go_to_login_page()
    page.should_be_login_link()