from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_product_page(self):
        self.should_be_add_to_basket_form()
        self.should_be_add_to_basket_button()

    def should_be_add_to_basket_form(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_FORM), \
            "add to basket form is not presented"

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), \
            "add to basket button is not presented"

    def click_add_to_basket_button(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_button.click()

    def get_product_real_name(self):
        product_real_name = self.browser.find_element(*ProductPageLocators.PRODUCT_REAL_NAME_ELEM).text
        return product_real_name

    def get_product_real_cost(self):
        product_real_cost = self.browser.find_element(*ProductPageLocators.PRODUCT_REAL_COST_ELEM).text
        return product_real_cost

    def get_product_basket_name(self):
        name = self.browser.find_element(*ProductPageLocators.PRODUCT_BASKET_NAME_ELEM).text
        return name

    def get_product_basket_cost(self):
        cost = self.browser.find_element(*ProductPageLocators.PRODUCT_BASKET_COST_ELEM).text
        return cost

    def should_be_equal_real_to_basket_names(self):
        real = self.get_product_real_name()
        basket = self.get_product_basket_name()
        assert real == basket,\
            f"Real product name: {real}, should be equal to basket name: {basket}. But it's not!"

    def should_be_equal_real_to_basket_costs(self):
        real = self.get_product_real_cost()
        basket = self.get_product_basket_cost()
        assert real == basket, \
            f"Real product cost: {real}, should be equal to basket cost: {basket}. But it's not!"

    #def should_be_working_url(self):
