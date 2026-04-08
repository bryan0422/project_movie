import pytest
from playwright.sync_api import expect
from pages.buscador_page import BuscadorPage
from pages.detalle_page import DetallePage
from data.peliculas import MOVIES


@pytest.mark.parametrize("busqueda, titulo, id_imdb", MOVIES)
def test_buscar_producto(page, base_url, busqueda, titulo, id_imdb):
    buscador = BuscadorPage(page, id_imdb)
    buscador.buscar_producto(busqueda, base_url)
    expect(buscador.resultados()).to_be_visible()
    expect(buscador.resultados()).to_have_attribute("title", titulo)
    
@pytest.mark.parametrize("busqueda, titulo, id_imdb", MOVIES)
def test_abrir_detalle(page, base_url, busqueda, titulo, id_imdb):
    buscador = BuscadorPage(page, id_imdb)
    buscador.buscar_producto(busqueda, base_url)
    buscador.abrir_resultado()

    detalle = DetallePage(page,titulo)
    expect(detalle.get_titulo()).to_be_visible()
    expect(detalle.get_titulo()).to_have_attribute("title", titulo)