import pytest


def pytest_addoption(parser):
    parser.addoption("--developer", action="store", default="default_value")


@pytest.fixture
def developer(request):
    return request.config.getoption("--developer")


# run pytest --developer=<number>
