import allure
from pages.login_page import LoginPage
from data import LOGIN_PAGE_URL


class TestLogin:

    @allure.title("Успешная авторизация пользователя")
    def test_login_user(self, driver, user):
        user_data, _ = user

        login_page = LoginPage(driver)
        login_page.open_page(LOGIN_PAGE_URL)
        login_page.enter_email(user_data["email"])
        login_page.enter_password(user_data["password"])
        login_page.click_login_button()

        assert login_page.is_order_button_displayed()