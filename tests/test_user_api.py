import pytest
from helpers import generate_user_data, register_user, login_user, delete_user, get_ingredient_ids, create_order, get_valid_ingredient_ids


def test_register_user():
    user_data = generate_user_data()

    response = register_user(user_data)

    assert response.status_code == 200
    assert response.json()["success"] is True

    token = response.json()["accessToken"]
    delete_user(token)


def test_login_user():
    user_data = generate_user_data()

    register_response = register_user(user_data)
    assert register_response.status_code == 200

    login_response = login_user(user_data)

    assert login_response.status_code == 200
    assert login_response.json()["success"] is True

    token = register_response.json()["accessToken"]
    delete_user(token)


def test_create_order():
    user_data = generate_user_data()

    register_response = register_user(user_data)
    token = register_response.json()["accessToken"]

    ingredient_ids = get_valid_ingredient_ids()

    order_response = create_order(ingredient_ids, token)

    assert order_response.status_code == 200
    assert order_response.json()["success"] is True

    delete_user(token)