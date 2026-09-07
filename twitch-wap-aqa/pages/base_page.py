from selenium.webdriver.common.by import By


class BasePage:
    # Popup buttons: cookie, age gate, login
    POPUP_XPATHS = [
        '//*[@data-a-target="consent-banner-accept"]',
        '//*[@data-a-target="modal-close-button"]',
        '//*[@data-a-target="content-classification-gate-overlay-start-watching-button"]',
        '//button[contains(@aria-label, "Close")]',
        '//button[contains(., "Accept")]',
        '//button[contains(., "Start Watching")]',
        '//button[contains(., "I understand")]',
        '//button[contains(., "Not now")]',
    ]

    def __init__(self, driver):
        # Every page uses the same browser
        self.driver = driver

    def close_popups(self):
        # Try each xpath once. find_element returns one button.

        for xpath in self.POPUP_XPATHS:

            try:
                button = self.driver.find_element(By.XPATH, xpath)
                button.click()

            except Exception:
                pass
