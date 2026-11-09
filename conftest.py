import pytest
from selenium import webdriver
from helpers import generate_user_data, register_user, delete_user


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):

    if request.param == "chrome":
        driver = webdriver.Chrome()
    elif request.param == "firefox":
        driver = webdriver.Firefox()

    driver.maximize_window()

    yield driver

    driver.quit()


@pytest.fixture
def user():

    user_data = generate_user_data()
    response = register_user(user_data)
    token = response.json()["accessToken"]

    yield user_data, token

    delete_user(token)