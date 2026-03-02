from playwright.sync_api import sync_playwright
from pytest_playwright.pytest_playwright import browser_name


class PlaywrightManager:
    def __init__(self, browser_name):
        self.playwright = sync_playwright().start()
        if browser_name == "chrome":
            self.browser = self.playwright.chromium.launch(headless=False)
        elif browser_name == "firefox":
            self.browser = self.playwright.firefox.launch(headless=False)
        self.context = self.browser.new_context()
        # Start tracing before creating / navigating a page.
        self.context.tracing.start(screenshots=True, snapshots=True, sources=True)
        self.page = self.context.new_page()

    def close(self):
        # Stop tracing and export it into a zip archive.
        self.context.tracing.stop(path="src/testResults/traceFiles/trace.zip")
        self.context.close()
        self.browser.close()
        self.playwright.stop()