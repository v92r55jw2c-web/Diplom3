from selenium.webdriver.support import expected_conditions as EC
import allure
from selenium.webdriver.support.ui import WebDriverWait
from pages.order_feed_page import OrderFeedPage
from data import ORDER_FEED_URL
from helpers import generate_user_data, register_user, delete_user, get_valid_ingredient_ids, create_order, create_test_order

class TestOrders:

    @allure.title("Получение данных из ленты заказов")
    def test_get_order_feed_data(self, driver):
        order_feed = OrderFeedPage(driver)
        order_feed.open_page(ORDER_FEED_URL)

        assert order_feed.get_total_orders_count() > 0
        assert order_feed.get_today_orders_count() > 0
        assert isinstance(order_feed.get_orders_in_progress(), list)


    @allure.title("Созданный заказ отображается в разделе «В работе»")
    def test_created_order_appears_in_progress(self, driver):
        user_data = generate_user_data()

        register_response = register_user(user_data)
        token = register_response.json()["accessToken"]

        ingredient_ids = get_valid_ingredient_ids()
        order_response = create_order(ingredient_ids, token)

        assert order_response.status_code == 200
        assert order_response.json()["success"] is True

        order_number = str(order_response.json()["order"]["number"])

        order_feed = OrderFeedPage(driver)
        order_feed.open_page(ORDER_FEED_URL)

        assert any(int(number) == int(order_number)
        for number in order_feed.get_order_numbers_in_progress())

        delete_user(token)


@allure.title("Счётчик выполненных заказов за всё время увеличивается")
def test_total_orders_count_increases(driver):
    order_feed = OrderFeedPage(driver)
    order_feed.open_page(ORDER_FEED_URL)

    total_before = order_feed.get_total_orders_count()

    order_response = create_test_order()

    assert order_response.status_code == 200
    assert order_response.json()["success"] is True

    driver.refresh()

    WebDriverWait(driver, 15).until(
        lambda d: order_feed.get_total_orders_count() > total_before
    )

    total_after = order_feed.get_total_orders_count()

    assert total_after > total_before


@allure.title("Счётчик выполненных заказов за сегодня увеличивается")
def test_today_orders_count_increases(driver):
    order_feed = OrderFeedPage(driver)
    order_feed.open_page(ORDER_FEED_URL)

    today_before = order_feed.get_today_orders_count()

    order_response = create_test_order()

    assert order_response.status_code == 200
    assert order_response.json()["success"] is True

    driver.refresh()

    WebDriverWait(driver, 15).until(
        lambda d: order_feed.get_today_orders_count() > today_before
    )

    today_after = order_feed.get_today_orders_count()

    assert today_after > today_before

