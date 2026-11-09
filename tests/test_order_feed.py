import allure
from pages.order_feed_page import OrderFeedPage
from data import ORDER_FEED_URL
from helpers import get_valid_ingredient_ids, create_order

class TestOrders:

    @allure.title("Получение данных из ленты заказов")
    def test_get_order_feed_data(self, driver):

        order_feed = OrderFeedPage(driver)
        order_feed.open_page(ORDER_FEED_URL)

        assert order_feed.get_total_orders_count() > 0
        assert order_feed.get_today_orders_count() > 0
        assert isinstance(order_feed.get_orders_in_progress(), list)


    @allure.title("Созданный заказ отображается в разделе «В работе»")
    def test_created_order_appears_in_progress(self, driver, user):
        _, token = user

        ingredient_ids = get_valid_ingredient_ids()
        order_response = create_order(ingredient_ids, token)

        assert order_response.status_code == 200
        assert order_response.json()["success"] is True

        order_number = str(order_response.json()["order"]["number"])

        order_feed = OrderFeedPage(driver)
        order_feed.open_page(ORDER_FEED_URL)

        assert any(int(number) == int(order_number)
        for number in order_feed.get_order_numbers_in_progress())


    @allure.title("Счётчик выполненных заказов за всё время увеличивается")
    def test_total_orders_count_increases(self, driver, user):
        _, token = user

        order_feed = OrderFeedPage(driver)
        order_feed.open_page(ORDER_FEED_URL)

        total_before = order_feed.get_total_orders_count()

        ingredient_ids = get_valid_ingredient_ids()
        order_response = create_order(ingredient_ids, token)

        assert order_response.status_code == 200
        assert order_response.json()["success"] is True

        order_feed.refresh_page()
        order_feed.wait_for_total_orders_count(total_before)

        total_after = order_feed.get_total_orders_count()

        assert total_after > total_before


    @allure.title("Счётчик выполненных заказов за сегодня увеличивается")
    def test_today_orders_count_increases(self, driver, user):
        _, token = user

        order_feed = OrderFeedPage(driver)
        order_feed.open_page(ORDER_FEED_URL)

        today_before = order_feed.get_today_orders_count()

        ingredient_ids = get_valid_ingredient_ids()
        order_response = create_order(ingredient_ids, token)

        assert order_response.status_code == 200
        assert order_response.json()["success"] is True

        order_feed.refresh_page()
        order_feed.wait_for_today_orders_count(today_before)

        today_after = order_feed.get_today_orders_count()

        assert today_after > today_before