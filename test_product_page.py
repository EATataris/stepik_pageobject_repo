from .pages.base_page import BasePage
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
import time, pytest

# LINK = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

# list_of_failed_num = [7]
# tested_links = [f"{LINK}?promo=offer{i}" if i not in list_of_failed_num else
#                 pytest.param(f"{LINK}?promo=offer{i}", marks=pytest.mark.xfail(reason="some bug", strict=True))
#                 for i in range(10)]


# @pytest.mark.parametrize('link', LINK)
def test_guest_can_add_product_to_basket(browser):
    # link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    # link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.could_add_to_basket()
    # page.solve_quiz_and_get_code()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()