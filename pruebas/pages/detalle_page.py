from pages.base_page import BasePage

class DetallePage(BasePage):
    def __init__(self, page, titulo):
        super().__init__(page)
        self.titulo = f"img.logo-X3hTV[title='{titulo}']"

    def get_titulo(self):
        return self.find(self.titulo)