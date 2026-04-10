import pytest 
from playwright.sync_api import expect
from pages.login_page import LoginPage
from data.user import USER_VALID


def test_login_exitoso(page):
    login = LoginPage(page)
    login.login(USER_VALID["email"], USER_VALID["password"])
    expect(login.success()).to_be_visible()