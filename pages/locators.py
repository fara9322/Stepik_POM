from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
class ProductPageLocators():
    ADD_BUTTON = (By.XPATH, "//button[@class='btn btn-lg btn-primary btn-add-to-basket']")
    ADDED_PRODUCT = (By.CSS_SELECTOR, "div.alertinner strong")
    PRODUCT_NAME = (By.TAG_NAME, "h1")
    PRODUCT_PRICE = (By.XPATH, "//p[@class='price_color']")
    CART_PRICE = (By.XPATH, "//div[@class='alertinner ']/p/strong")
class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "login_link_inc")

