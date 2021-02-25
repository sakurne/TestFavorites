class Application:
    def __init__(self, selenium=None):
        self.browser = selenium
        self.current_page = None

    def open_page(self, url):
        self.browser.get(url)
