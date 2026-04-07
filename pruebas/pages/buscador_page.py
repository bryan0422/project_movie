from pages.base_page import BasePage
from data.peliculas import ID_IMDB, TITULO


class BuscadorPage(BasePage):
    search_container = "div[class*='search-input']"
    buscador = 'input[placeholder="Search or paste link"]'
    resultado = f"#{ID_IMDB}"

    def buscar_producto(self, producto, base_url):
        self.navegar(f"{base_url}/#/")
        self.find(self.search_container).click()
        self.find(self.buscador).fill(producto)
        self.find(self.buscador).press("Enter")
        self.page.wait_for_load_state("networkidle")

    def resultados(self):
        return self.find(self.resultado)

    def abrir_resultado(self):
        self.find(self.resultado).click()