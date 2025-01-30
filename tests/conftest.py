import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

@pytest.fixture()
#@pytest.fixture(params= ["chrome","edge"])
@pytest.mark.login
@pytest.mark.exception
def driver(request):
    browser = request.config.getoption("--browser").lower()  # Normalisation en minuscule
    #browser= request.param
    print(f"Creating {browser.capitalize()} Driver")

    if browser == "chrome":
        service = ChromeService(ChromeDriverManager().install())
        my_driver = webdriver.Chrome(service=service)

    elif browser == "edge":
        service = EdgeService(EdgeChromiumDriverManager().install())
        my_driver = webdriver.Edge(service=service)

    else:
        # Lève une exception pour un navigateur non pris en charge
        raise TypeError("Expected 'chrome' or 'edge', but got something else.")
    my_driver.implicitly_wait(4)
    yield my_driver

    print(f"Closing {browser.capitalize()} Driver")
    my_driver.quit()


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",  # Valeur par défaut en minuscule
        help="Browser to execute tests (chrome or edge)",
        choices=("chrome", "edge"),  # Limite les choix à chrome ou edge
    )
