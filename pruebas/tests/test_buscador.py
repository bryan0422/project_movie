from playwright.sync_api import expect
from pages.buscador_page import BuscadorPage
from pages.detalle_page import DetallePage
from data.peliculas import BUSQUEDA, TITULO

def test_buscar_producto(page, base_url):
    buscador = BuscadorPage(page)
    buscador.buscar_producto(BUSQUEDA, base_url)
    expect(buscador.resultados()).to_be_visible()
    expect(buscador.resultados()).to_have_attribute("title", TITULO)

def test_abrir_detalle(page, base_url):
    buscador = BuscadorPage(page)
    buscador.buscar_producto(BUSQUEDA, base_url)
    buscador.abrir_resultado()

    detalle = DetallePage(page)
    expect(detalle.get_titulo()).to_be_visible()
    expect(detalle.get_titulo()).to_have_attribute("title", "nada")