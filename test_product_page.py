import pytest
import time
from pages.main_page import MainPage
from pages.product_page import PageObject


@pytest.mark.parametrize('promo_offer', ["0","1", "3", "4", "5", "6", "7", "8", "9"])
def test_guest_can_add_product_to_basket(browser, promo_offer):
    browser.delete_all_cookies()
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
# def test_guest_can_go_to_login_page(browser):
    # link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear" -- с этой ссылкой работает все ок
    # link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
    url = link
    print(url)
    page = MainPage(browser, url)
    page.open()
    basketpage = PageObject(browser, browser.current_url)
    basketpage.should_be_basket_page()
    basketpage.click_the_basket_button()
    basketpage.should_be_alert()
    page.solve_quiz_and_get_code()
    # basketpage.should_be_alert()