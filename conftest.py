import pytest
from src.core.PlaywrightManager import PlaywrightManager

def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome", help="Browser Type Selection")
    parser.addoption("--url", action="store", default="https://www.saucedemo.com/", help="Base Page URL")


@pytest.fixture(scope="function")
def page(request):
    browser_name = request.config.getoption("--browser_name")
    url = request.config.getoption("--url")
    manager = PlaywrightManager(browser_name)
    manager.page.goto(url)
    yield manager.page
    manager.close()