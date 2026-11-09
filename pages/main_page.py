from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.common.action_chains import ActionChains
import allure


class MainPage(BasePage):

    @allure.step("Нажать на кнопку Конструктор")
    def click_constructor(self):
        self.click_element_with_wait(MainPageLocators.CONSTRUCTOR_BUTTON)


    @allure.step("Нажать на кнопку Лента заказов")
    def click_order_feed(self):
        self.click_element_with_wait(MainPageLocators.ORDER_FEED_BUTTON)


    @allure.step("Выбрать ингредиент")
    def click_ingredient(self):
        self.click_element_with_wait(MainPageLocators.BUN_INGREDIENT)


    @allure.step("Закрыть модальное окно ингредиента")
    def close_ingredient_modal(self):
        self.click_element_with_wait(MainPageLocators.CLOSE_MODAL_BUTTON)


    @allure.step("Проверить, что модальное окно ингредиента закрыто")
    def is_ingredient_modal_closed(self):
        return self.wait_for_element_invisibility(MainPageLocators.INGREDIENT_MODAL_TITLE)


    @allure.step("Проверить, что модальное окно ингредиента открыто")
    def is_ingredient_modal_opened(self):
        return self.find_element_with_wait(MainPageLocators.INGREDIENT_MODAL_TITLE).is_displayed()


    @allure.step("Получить название ингредиента в модальном окне")
    def get_ingredient_modal_name(self):
        return self.find_element_with_wait(MainPageLocators.INGREDIENT_MODAL_NAME).text


    @allure.step("Перетащить ингредиент в конструктор")
    def drag_ingredient_to_constructor(self):
        ingredient = self.find_element_with_wait(MainPageLocators.BUN_INGREDIENT)

        constructor = self.find_element_with_wait(MainPageLocators.CONSTRUCTOR_AREA)

        ActionChains(self.driver).drag_and_drop(ingredient, constructor).perform()


    @allure.step("Проверить, что булка добавлена в конструктор")
    def is_bun_added(self):
        return self.find_element_with_wait(MainPageLocators.ADDED_BUN_TOP).is_displayed()

    @allure.step("Проверить отображение конструктора")
    def is_constructor_displayed(self):
        return self.find_element_with_wait(MainPageLocators.CONSTRUCTOR_AREA).is_displayed()