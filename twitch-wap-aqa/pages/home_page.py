from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from config import settings
from pages.base_page import BasePage


class HomePage(BasePage):

    # Search button
    SEARCH_BUTTON = '//*[@data-a-target="search-icon-button"] | //a[@href="/search"]'

    def open(self):

        # Open Twitch home
        self.driver.get(settings.BASE_URL)
        self.close_popups()

    def go_to_search(self):

        # Click search; if the button is missing, go to /search
        try:
            button = WebDriverWait(self.driver, timeout=5).until(
                EC.element_to_be_clickable((By.XPATH, self.SEARCH_BUTTON))
            )
            button.click()

        except TimeoutException:
            self.driver.get(settings.BASE_URL.rstrip("/") + "/search")
