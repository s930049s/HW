from datetime import datetime
from pathlib import Path
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from config import settings
from pages.base_page import BasePage


class StreamerPage(BasePage):
    
    # Video player, or at least the main content area
    PLAYER = '//*[@data-a-target="video-player"] | //video | //main'

    def wait_until_ready(self):
        # Age-gate / login often appears on the streamer page, sometimes after the player loads
        self.close_popups()
        WebDriverWait(self.driver, settings.WAIT_SECONDS).until(
            EC.presence_of_element_located((By.XPATH, self.PLAYER))
        )
        self.close_popups()

    def save_screenshot(self, folder):
        # Save the current screen as a PNG
        folder = Path(folder)
        folder.mkdir(parents=True, exist_ok=True)
        time_text = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_path = folder / ("streamer_" + time_text + ".png")
        self.driver.save_screenshot(str(file_path))
        return file_path
