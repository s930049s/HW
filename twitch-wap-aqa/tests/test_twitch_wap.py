import time

from config import settings
from pages.home_page import HomePage
from pages.search_page import SearchPage
from pages.streamer_page import StreamerPage


def test_search_starcraft_and_open_streamer(driver, screenshot_dir):
    # 1. Open Twitch
    home = HomePage(driver)
    home.open()
    time.sleep(2)

    # 2. Click search
    home.go_to_search()
    time.sleep(2)

    # 3. Search StarCraft II
    search = SearchPage(driver)
    search.type_keyword(settings.SEARCH_TEXT)
    time.sleep(2)

    # 4. Scroll down twice
    search.scroll_down(1)
    search.scroll_down(1)
    time.sleep(2)

    # 5. Open a streamer
    search.click_first_live()
    time.sleep(2)

    # 6. Wait for the page, then take a screenshot
    streamer = StreamerPage(driver)
    streamer.wait_until_ready()
    time.sleep(6)
    file_path = streamer.save_screenshot(screenshot_dir)

    # Check the screenshot was saved and we are still on twitch.tv
    assert file_path.exists()
    assert file_path.stat().st_size > 0
    assert "twitch.tv" in driver.current_url
