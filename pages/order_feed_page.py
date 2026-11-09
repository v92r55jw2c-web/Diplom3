from pages.base_page import BasePage
from locators.order_feed_locators import OrderFeedLocators
import allure


class OrderFeedPage(BasePage):

    @allure.step("Получить общее количество выполненных заказов")
    def get_total_orders_count(self):
        return int(self.get_element_text(OrderFeedLocators.TOTAL_ORDERS_COUNT))


    @allure.step("Получить количество выполненных заказов за сегодня")
    def get_today_orders_count(self):
        return int(self.get_element_text(OrderFeedLocators.TODAY_ORDERS_COUNT))


    @allure.step("Получить список заказов в работе")
    def get_orders_in_progress(self):
        return self.driver.find_elements(*OrderFeedLocators.ORDER_NUMBERS_IN_PROGRESS)


    @allure.step("Получить номера заказов в работе")
    def get_order_numbers_in_progress(self):
        orders = self.get_orders_in_progress()
        return [order.text for order in orders]


    @allure.step("Обновить страницу ленты заказов")
    def refresh_page(self):
        self.driver.refresh()


    @allure.step("Дождаться обновления общего количества заказов")
    def wait_for_total_orders_count(self, expected_count):
        self.wait.until(lambda driver: self.get_total_orders_count() > expected_count)


    @allure.step("Дождаться увеличения количества заказов за сегодня")
    def wait_for_today_orders_count(self, expected_count):
        self.wait.until(lambda _: self.get_today_orders_count() > expected_count)