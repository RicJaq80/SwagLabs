from selenium import webdriver
import pytest

@pytest.fixture()
def MethodSetup():
    print("\nStart Test Case")
    yield
    print("\nFinish Test Case")

@pytest.fixture(scope="class")
def ClassSetup(request, browser):
    print("\nStart Class Module")
    baseUrl = "https://www.saucedemo.com/"
    if browser == "chrome":
        print("Running on Chrome")
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(2)
        driver.get(baseUrl)

    if request.cls is not None:
        request.cls.driver = driver
    
    yield driver
    driver.quit()
    print("Finish Class Module")

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture(scope="module")
def browser(request):
    return request.config.getoption("--browser")
