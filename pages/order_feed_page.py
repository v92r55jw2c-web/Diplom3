from pages.base_page import BasePage
from locators.order_feed_locators import OrderFeedLocators


class OrderFeedPage(BasePage):
    
    def get_total_orders_count(self):
        return int(self.get_element_text(OrderFeedLocators.TOTAL_ORDERS_COUNT))


    def get_today_orders_count(self):
        return int(self.get_element_text(OrderFeedLocators.TODAY_ORDERS_COUNT))


    def get_orders_in_progress(self):
        return self.driver.find_elements(*OrderFeedLocators.ORDER_NUMBERS_IN_PROGRESS)

    def get_order_numbers_in_progress(self):
        orders = self.get_orders_in_progress()
        return [order.text for order in orders]