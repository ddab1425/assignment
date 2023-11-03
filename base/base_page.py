import logging
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

logging.basicConfig(level=logging.INFO)

class BasePage:

    def __init__(self, driver):
        self.wait = None
        self.driver = driver
        self.explicit_wait_timeout = 60
        self.set_explicit_wait_timeout(self.explicit_wait_timeout)

    def set_explicit_wait_timeout(self, timeout: int):
        self.wait = WebDriverWait(self.driver, timeout)

    def get_page(self, url: str):
        logging.info("Open URL -> %s", url)
        self.driver.get(url)

    def get_title(self):
        return self.driver.title

    def quit_driver(self):
        logging.info("Quit driver")
        self.driver.quit()

    def find_element(self, locator: tuple):
        logging.debug("Find Element: %s", locator)
        _element = self.wait.until(ec.visibility_of_element_located(locator))
        return _element
    
    def find_elements(self, locator: tuple):
        logging.debug("Find Element: %s", locator)
        _element = self.wait.until(ec.visibility_of_all_elements_located(locator))
        return _element

    def refresh(self):
        self.driver.refresh()

    def save_screenshot(self, filename):
        self.driver.save_screenshot(filename)