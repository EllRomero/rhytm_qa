import pytest


def pytest_addoption(parser):
    parser.addoption(
        '--drivers',
        help='опция указывает какой браузер будет использован',
        default='chrome',
        choices=('chrome', 'firefox', 'edge')
    ),
    parser.addoption(
        '--headless',
        help='опция браузера в фоновом режиме',
        default=False,
    )


@pytest.fixture
def drivers(request):
    '''Функция выбора браузера.'''

    return request.config.getoption("--drivers")


@pytest.fixture
def headless(request):
    '''Функция браузер в фоновом режиме'''

    return request.config.getoption('--headless')
