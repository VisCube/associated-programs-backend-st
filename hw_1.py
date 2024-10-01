import requests

BASE_URL = "https://fakestoreapi.com/"

# 1. Вывести продукты, цена которых <20
response = requests.get(f"{BASE_URL}/products")
products = filter(lambda product: product["price"] < 20, response.json())
print(*products, sep="\n", end="\n\n")

# 2. Вывести все категории
response = requests.get(f"{BASE_URL}/products/categories")
print(*response.json(), sep="\n", end="\n\n")

# 3. Вывести все продукты с категорией "jewelery"
response = requests.get(f"{BASE_URL}/products/category/jewelery")
print(*response.json(), sep="\n", end="\n\n")

# 4. Вывести всех пользователей
response = requests.get(f"{BASE_URL}/users")
print(*response.json(), sep="\n", end="\n\n")

# 5. Добавить пользователя со своим именем.
response = requests.post(f"{BASE_URL}/users", data=dict(name=dict(firstname="Mark", lastname="Zhitomirsky")))
print(response.json())

