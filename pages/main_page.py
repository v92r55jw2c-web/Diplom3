from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.common.action_chains import ActionChains


class MainPage(BasePage):

    def click_constructor(self):
        self.click_element_with_wait(MainPageLocators.CONSTRUCTOR_BUTTON)

    def click_order_feed(self):
        self.click_element_with_wait(MainPageLocators.ORDER_FEED_BUTTON)

    def click_ingredient(self):
        self.click_element_with_wait(MainPageLocators.BUN_INGREDIENT)

    def close_ingredient_modal(self):
        self.click_element_with_wait(MainPageLocators.CLOSE_MODAL_BUTTON)

    def is_ingredient_modal_closed(self):
        return self.wait_for_element_invisibility(MainPageLocators.INGREDIENT_MODAL_TITLE)

    def is_ingredient_modal_opened(self):
        return self.find_element_with_wait(MainPageLocators.INGREDIENT_MODAL_TITLE).is_displayed()


    def get_ingredient_modal_name(self):
        return self.find_element_with_wait(MainPageLocators.INGREDIENT_MODAL_NAME).text


    def drag_ingredient_to_constructor(self):
        ingredient = self.find_element_with_wait(MainPageLocators.BUN_INGREDIENT)

        constructor = self.find_element_with_wait(MainPageLocators.CONSTRUCTOR_AREA)

        ActionChains(self.driver).drag_and_drop(ingredient, constructor).perform()


    def is_bun_added(self):
        return self.find_element_with_wait(MainPageLocators.ADDED_BUN_TOP).is_displayed()

    def is_constructor_displayed(self):
        return self.find_element_with_wait(MainPageLocators.CONSTRUCTOR_AREA).is_displayed()