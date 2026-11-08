from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class LoginPage(BasePage):
    def enter_email(self, email):
        self.send_keys_to_element(MainPageLocators.EMAIL_INPUT, email)

    def enter_password(self, password):
        self.send_keys_to_element(MainPageLocators.PASSWORD_INPUT, password)

    def click_login_button(self):
        self.click_element_with_wait(MainPageLocators.LOGIN_BUTTON)

    def is_order_button_displayed(self):
        return self.find_element_with_wait(MainPageLocators.ORDER_BUTTON).is_displayed()