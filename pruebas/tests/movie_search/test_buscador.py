import pytest
import os
from playwright.sync_api import expect
from pages.buscador_page import BuscadorPage
from pages.detalle_page import DetallePage
from data.peliculas import MOVIES


@pytest.mark.authenticated
@pytest.mark.parametrize("busqueda, titulo, id_imdb", MOVIES)
def test_abrir_detalle(page, base_url, busqueda, titulo, id_imdb):
    buscador = BuscadorPage(page, id_imdb)
    buscador.ir_al_home(base_url)

    page.click("[class*='menu-button-container']")
    page.wait_for_selector("[class*='email-label']")
    page.evaluate("const el = document.querySelector(\"[class*='email-label']\"); el.style.outline = '3px solid red'; el.style.backgroundColor = 'yellow'; el.style.color = 'black';")
    page.wait_for_timeout(500)
    page.screenshot(path=f"screenshots/email_popup_{busqueda}.png")
    expect(page.locator("[class*='email-label']")).to_have_text(os.getenv("STREMIO_EMAIL"))

    buscador.buscar(busqueda)
    buscador.abrir_resultado()
    detalle = DetallePage(page, titulo)
    expect(detalle.get_titulo()).to_be_visible()
    expect(detalle.get_titulo()).to_have_attribute("title", titulo)