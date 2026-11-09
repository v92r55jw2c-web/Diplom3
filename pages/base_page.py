from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_page(self, url):
        self.driver.get(url)

    def get_current_url(self):
        return self.driver.current_url

    def find_element_with_wait(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def get_element_text(self, locator):
        return self.find_element_with_wait(locator).text

    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    def click_element(self, element):
        self.driver.execute_script("arguments[0].click();", element)

    def click_element_with_wait(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()


    def is_url_opened(self, url):
        try:
            self.wait.until(EC.url_to_be(url))
            return True
        except TimeoutException:
            return False

    def send_keys_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    def select_option_by_text(self, locator, text):
        self.click_element_with_wait((locator[0], locator[1].format(text)))

    def switch_to_new_window(self, original_window):
        for window in self.driver.window_handles:
            if window != original_window:
                self.driver.switch_to.window(window)
                break

    def get_current_window(self):
        return self.driver.current_window_handle

    def wait_for_new_window(self, windows_count):
        self.wait.until(
            lambda d: len(d.window_handles) == windows_count)

    def wait_for_element_invisibility(self, locator):
        return self.wait.until(EC.invisibility_of_element_located(locator))