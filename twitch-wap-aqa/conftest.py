import os
from pathlib import Path

import pytest

from utils.driver_factory import create_driver

# Folder for screenshots
SCREENSHOT_DIR = Path("screenshots").resolve()


# @pytest.fixture tells pytest: if a test has a parameter with this name, prepare it.
# This is not class inheritance. It is setup before the test and cleanup after.
@pytest.fixture
def driver():
    # Start of test: open the browser
    hide_window = os.getenv("HEADLESS", "false").lower() in ("1", "true", "yes")
    browser = create_driver(headless=hide_window)
    yield browser  # give the browser to the test; continue after the test ends
    # End of test: close the browser
    browser.quit()


@pytest.fixture
def screenshot_dir():
    # Create the folder if it does not exist
    SCREENSHOT_DIR.mkdir(parents=True, exist_ok=True)
    return SCREENSHOT_DIR
