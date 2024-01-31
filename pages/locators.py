from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_ink")
    BASKET_LINK = (By.XPATH, '//a[contains(@href, "basket")]')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_URL = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_INPUT = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD1_INPUT = (By.CSS_SELECTOR, "#id_registration-password1")
    PASSWORD2_INPUT = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_BUTTON = (By.XPATH, '//button[@name="registration_submit"]')


class ProductPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    PRODUCT_NAME_MESSAGE = (By.CSS_SELECTOR, ".fade.in:nth-child(1) strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".col-sm-6.product_main > h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".col-sm-6.product_main > p")
    BASKET_PRODUCT_PRICE = (By.CSS_SELECTOR, ".fade.in:nth-child(3) strong")

    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".fade.in:nth-child(1)")


class BasketPageLocators():
    BASKET_PRODUCTS = (By.CSS_SELECTOR, "#basket_formset")
    BASKET_IS_EMPTY_TEXT = (By.XPATH, '//p[text()="Ваша корзина пуста"]')