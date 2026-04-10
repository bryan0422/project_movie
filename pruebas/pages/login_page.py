from pages.base_page import BasePage

class LoginPage(BasePage):
    url = "https://web.stremio.com/#/intro?form=login"
    email = "//input[@placeholder='E-mail']"
    password = "//input[@placeholder='Password']"
    boton_login = "//*[contains(text(), 'Log in')]"
    msg = "div[class*='search-input']"
    
    def login(self, email, password):
        self.navegar(self.url)
        self.fill(self.email, email)
        self.fill(self.password, password)
        self.click(self.boton_login)
    def success(self):
        return self.find(self.msg)    
