import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from config import settings
from pages.base_page import BasePage


class SearchPage(BasePage):

    SEARCH_BOX = '//input[@data-a-target="tw-input" or @type="search"]'

    # Live preview URLs contain live_user_<channel>
    LIVE_IMAGE = '//img[contains(@src, "previews-ttv/live_user_")]'

    CHANNELS_TAB = '//a[contains(@href, "type=channels")]'

    def type_keyword(self, keyword):

        # Type into the search box and press Enter
        box = WebDriverWait(self.driver, settings.WAIT_SECONDS).until(
            EC.visibility_of_element_located((By.XPATH, self.SEARCH_BOX))
        )
        box.click()
        box.send_keys(Keys.CONTROL, "a")
        box.send_keys(keyword, Keys.ENTER)
        self.wait_for_live_results()

    def scroll_down(self, times=1):

        # Scroll down; pause so content can load
        for i in range(times):
            self.driver.execute_script("window.scrollBy(0, 800);")
            time.sleep(settings.SCROLL_PAUSE)

    def click_first_live(self):

        # Click a live card that is on screen after scrolling
        card = self.find_first_live_card()

        try:
            card.click()
        except Exception:
            # Normal click failed, so click with JavaScript
            self.driver.execute_script("arguments[0].click();", card)

    def wait_for_live_results(self):

        # Wait for live imagge; if none, open the channel tab
        try:
            WebDriverWait(self.driver, 8).until(
                EC.presence_of_element_located((By.XPATH, self.LIVE_IMAGE))
            )
            return
        except TimeoutException:
            pass

        try:
            tab = WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable((By.XPATH, self.CHANNELS_TAB))
            )
            tab.click()
            time.sleep(2)
        except TimeoutException:
            pass

        WebDriverWait(self.driver, settings.WAIT_SECONDS).until(
            EC.visibility_of_element_located((By.XPATH, self.LIVE_IMAGE))
        )

    def find_first_live_card(self):
        # Prefer a live card that is currently on screen
        images = self.driver.find_elements(By.XPATH, self.LIVE_IMAGE)
        for image in images:
            on_screen = self.driver.execute_script(
                """
                const box = arguments[0].getBoundingClientRect();
                return box.bottom > 80 && box.top < window.innerHeight;
                """,
                image,
            )
            if not on_screen:
                continue
            card = self.driver.execute_script(
                "return arguments[0].closest('button, a');",
                image,
            )
            if card:
                return card

        raise TimeoutError("No live streamer card found")
