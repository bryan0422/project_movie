from pages.base_page import BasePage
from data.peliculas import TITULO

class DetallePage(BasePage):
    titulo = f"img.logo-X3hTV[title='{TITULO}']"

    def get_titulo(self):
        return self.find(self.titulo)