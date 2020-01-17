from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.product_page import PageObject


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = MainPage(browser, link)
    page.open()
    basketpage = PageObject(browser, browser.current_url)
    basketpage.should_be_basket_page()
    basketpage.click_the_basket_button()
    basketpage.should_be_alert()
    page.solve_quiz_and_get_code()