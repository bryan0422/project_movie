from playwright.sync_api import Page
class BasePage:
    def __init__(self, page: Page):
        self.page = page
        
    def find(self, selector):
        return self.page.locator(selector)    
    
    def navegar(self, url):
        self.page.goto(url)
        self.page.wait_for_load_state("networkidle")
        