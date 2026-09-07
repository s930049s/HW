from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from config import settings


def create_driver(headless=False):
    # Open Chrome with mobile emulation
    options = Options()
    options.add_experimental_option(
        "mobileEmulation", {"deviceName": settings.PHONE}
    )
    options.add_argument("--disable-notifications")
    options.add_argument(
        f"--window-size={settings.PHONE_WIDTH},{settings.PHONE_HEIGHT}"
    )

    if headless:
        # Run without a visible window
        options.add_argument("--headless=new")

    driver = webdriver.Chrome(options=options)
    driver.set_window_size(settings.PHONE_WIDTH, settings.PHONE_HEIGHT)
    driver.set_page_load_timeout(settings.PAGE_LOAD_SECONDS)
    return driver
