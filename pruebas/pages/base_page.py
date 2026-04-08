from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def find(self, selector):
        return self.page.locator(selector)

    def click(self, selector):
        self.find(selector).click()

    def fill(self, selector, texto):
        self.find(selector).fill(texto)

    def press(self, selector, tecla):
        self.find(selector).press(tecla)

    def navegar(self, url):
        self.page.goto(url)
        self.page.wait_for_load_state("domcontentloaded")
