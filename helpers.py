import requests
from data import REGISTER_URL, LOGIN_API_URL, DELETE_USER_API_URL, BASE_URL, CREATE_ORDER_URL
from faker import Faker

fake = Faker()

def generate_user_data():
    return {
        "email": fake.email(),
        "password": fake.password(),
        "name": fake.name()
    }


def register_user(user_data):
    return requests.post(REGISTER_URL, json=user_data)

def login_user(user_data):
    return requests.post(LOGIN_API_URL, json=user_data)

def delete_user(token):
    return requests.delete(DELETE_USER_API_URL, headers={"Authorization": token})

def get_ingredients():
    response = requests.get(BASE_URL + "api/ingredients")
    return response.json()["data"]

def get_ingredient_ids():
    ingredients = get_ingredients()
    return [ingredient["_id"] for ingredient in ingredients]

def create_order(ingredient_ids, token):
    return requests.post(CREATE_ORDER_URL, json={"ingredients": ingredient_ids}, headers={"Authorization": token})


def get_valid_ingredient_ids():
    ingredients = get_ingredients()

    bun = next(item for item in ingredients if item["type"] == "bun")
    main = next(item for item in ingredients if item["type"] == "main")
    sauce = next(item for item in ingredients if item["type"] == "sauce")

    return [bun["_id"], main["_id"], sauce["_id"]]


def create_test_order():
    user_data = generate_user_data()

    register_response = register_user(user_data)
    token = register_response.json()["accessToken"]

    ingredient_ids = get_valid_ingredient_ids()
    order_response = create_order(ingredient_ids, token)

    return order_response