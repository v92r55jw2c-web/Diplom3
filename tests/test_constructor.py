from selenium.webdriver.support import expected_conditions as EC
import allure
from pages.main_page import MainPage
from data import ORDER_FEED_URL, BASE_URL


class TestConstructor:

    @allure.title("Открытие и закрытие окна с деталями ингредиента")
    def test_open_and_close_ingredient_modal(self, driver):
        main_page = MainPage(driver)

        main_page.open_page(BASE_URL)

        main_page.click_ingredient()

        assert main_page.is_ingredient_modal_opened()
        assert main_page.get_ingredient_modal_name() == "Флюоресцентная булка R2-D3"

        main_page.close_ingredient_modal()

        assert main_page.is_ingredient_modal_closed()


    @allure.title("Добавление ингредиента в конструктор")
    def test_drag_ingredient_to_constructor(self, driver):
        main_page = MainPage(driver)

        main_page.open_page(BASE_URL)
        main_page.drag_ingredient_to_constructor()

        assert main_page.is_bun_added()


    @allure.title("Переход в ленту заказов")
    def test_open_order_feed(self, driver):
        main_page = MainPage(driver)

        main_page.open_page(BASE_URL)
        main_page.click_order_feed()

        assert main_page.is_url_opened(ORDER_FEED_URL)



    @allure.title("Переход из ленты заказов в конструктор")
    def test_open_constructor(self, driver):
        main_page = MainPage(driver)

        main_page.open_page(ORDER_FEED_URL)
        main_page.click_constructor()

        assert main_page.is_url_opened(BASE_URL)
        assert main_page.is_constructor_displayed()