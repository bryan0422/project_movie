import pytest

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)

@pytest.fixture(autouse=True)
def screenshot_on_failure(page, request):
    yield
    if request.node.rep_call.failed:
        page.screenshot(path=f"screenshots/{request.node.name}.png")


@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args):
    import os
    is_ci = os.getenv("CI", "false") == "true"
    return {
        **browser_type_launch_args,
        "headless": is_ci,
        "slow_mo": 0 if is_ci else 500
    }

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "viewport": {"width": 1300, "height": 800},
    }

@pytest.fixture
def page(page):
    yield page