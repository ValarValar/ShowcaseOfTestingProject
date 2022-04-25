from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    ADD_TO_BASKET_FORM = (By.CSS_SELECTOR, "#add_to_basket_form")
    PRODUCT_REAL_NAME_ELEM = (By.CSS_SELECTOR, ".product_main > h1")
    PRODUCT_REAL_COST_ELEM = (By.CSS_SELECTOR, ".product_main > p.price_color")
    PRODUCT_BASKET_NAME_ELEM = (By.CSS_SELECTOR, "#messages :first-child .alertinner > strong")
    PRODUCT_BASKET_COST_ELEM = (By.CSS_SELECTOR, "#messages .alert-info strong")