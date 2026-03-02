class CommonActions:
    def __init__(self, page):
        self.page = page

    def click(self, locator):
        self.page.wait_for_selector(locator)
        self.page.click(locator)

    def send_keys(self, locator, value):
        self.page.wait_for_selector(locator)
        self.page.fill(locator, value)

    def get_text(self, locator):
        self.page.wait_for_selector(locator)
        return self.page.text_content(locator)

    def is_visible(self, locator):
        return self.page.is_visible(locator)