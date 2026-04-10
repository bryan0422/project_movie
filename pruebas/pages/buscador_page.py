from pages.base_page import BasePage

class BuscadorPage(BasePage):
    search_container = "div[class*='search-input']"
    buscador = 'input[placeholder="Search or paste link"]'
    
    def __init__(self, page, id_imdb):
        super().__init__(page)
        self.resultado = f"#{id_imdb}"

    def ir_al_home(self, base_url):
        self.navegar(f"{base_url}/#/")

    def buscar(self, producto):
        self.click(self.search_container)
        self.fill(self.buscador, producto)
        self.press(self.buscador, "Enter")

    def buscar_producto(self, producto, base_url):
        self.ir_al_home(base_url)
        self.buscar(producto)
        

    def resultados(self):
        return self.find(self.resultado)

    def abrir_resultado(self):
        self.click(self.resultado)