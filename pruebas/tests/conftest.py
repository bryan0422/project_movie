import pytest
import os
from pages.login_page import LoginPage


@pytest.fixture(scope="session")
def auth_file(tmp_path_factory, browser):
    context = browser.new_context(viewport={"width": 1300, "height": 800})
    page = context.new_page()
    page.set_default_timeout(60000)

    login = LoginPage(page)
    login.login(os.getenv("STREMIO_EMAIL"), os.getenv("STREMIO_PASSWORD"))
    page.wait_for_selector("div[class*='search-input']", timeout=120000)

    path = tmp_path_factory.mktemp("auth") / "auth.json"
    context.storage_state(path=str(path))

    context.close()
    return path
