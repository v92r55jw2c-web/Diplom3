from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
import allure


class LoginPage(BasePage):

    @allure.step("Ввести email")
    def enter_email(self, email):
        self.send_keys_to_element(MainPageLocators.EMAIL_INPUT, email)


    @allure.step("Ввести пароль")
    def enter_password(self, password):
        self.send_keys_to_element(MainPageLocators.PASSWORD_INPUT, password)


    @allure.step("Нажать на кнопку Войти")
    def click_login_button(self):
        self.wait_for_element_invisibility(MainPageLocators.LOADING_MODAL)
        self.click_element_with_wait(MainPageLocators.LOGIN_BUTTON)


    @allure.step("Проверить, что кнопка заказа активна")
    def is_order_button_displayed(self):
        return self.find_element_with_wait(MainPageLocators.ORDER_BUTTON).is_displayed()