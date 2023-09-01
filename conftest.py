import pytest
from selene import browser


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.base_url = 'https://demoqa.com'
    browser.config.driver_name = 'firefox'
    browser.config.window_width = 1200
    browser.config.window_height = 1200
    yield

    browser.quit()
