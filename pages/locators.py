from selenium.webdriver.common.by import By



class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_ink")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_URL = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    PRODUCT_NAME_MESSAGE = (By.CSS_SELECTOR, ".fade.in:nth-child(1) strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".col-sm-6.product_main > h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".col-sm-6.product_main > p")
    BASKET_PRODUCT_PRICE = (By.CSS_SELECTOR, ".fade.in:nth-child(3) strong")

    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".fade.in:nth-child(1)")
