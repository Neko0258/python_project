import requests, json
from pprint import pprint

def Response(response):
    print("HTTP Status Code: " + str(response.status_code))
    print(response.headers)
    results = response.json()
    pprint(results)

BASE = "http://172.21.0.2:5000/"

def Login():
    username = input("Username: ")
    password = input("Password: ")
    response = requests.get(BASE + "login", {"username": username, "password": password})
    Response(response)

def Register():
    username = input("Username: ")
    password = input("Password: ")
    email = input("Email: ")
    response = requests.post(BASE + "register", json={"username": username, "password": password, "email": email})
    Response(response)

def VerifyEmail():
    email = input("Email: ")
    response = requests.get(BASE + "verifyemail", {"email": email})
    Response(response)

def AddProduct():
    name_product = input("Name Product: ")
    price = int(input("Price: "))
    quantity = int(input("Quantity: "))
    description = input("Description: ")
    response = requests.post(BASE + "product", json={"name_product": name_product, "price": price,"quantity": quantity, "description": description})
    Response(response)

def ShowQuantity():
    response = requests.get(BASE + "product/quantity")
    Response(response)

def UpdateProduct():
    name_product = input("Name Product: ")
    price = int(input("Price: "))
    quantity = int(input("Quantity: "))
    description = input("Description: ")
    id = input("ID Product: ")    
    response = requests.put(BASE + "product/update/" + str(id), json={"name_product": name_product, "price": price,"quantity": quantity, "description": description})
    Response(response)

def DeleteProduct():
    id = input("ID Product: ")  
    response = requests.delete(BASE + "product/delete/" + str(id))
    Response(response)

def OrderProduct():
    id = input("ID Product: ")
    quantity = int(input("Quantity: "))
    response = requests.put(BASE + "order/" + str(id), json={"quantity": quantity})
    Response(response)

def Exit():
    print("Good bye!")

while(True):
    print("""
        ------------------------------------------------
        1. Login
        2. Register
        3. Verify Email
        4. Add Product
        5. Show Quantity Of Product
        6. Update Product
        7. Delete Product
        8. Order Product
        0. Exit
        -------------------------------------------------
    """)
    choose = int(input("Choose: "))
    if choose == 1:
        Login()
    elif choose == 2:
        Register()
    elif choose == 3:
        VerifyEmail()
    elif choose == 4:
        AddProduct()
    elif choose == 5:
        ShowQuantity()
    elif choose == 6:
        UpdateProduct()
    elif choose == 7:
        DeleteProduct()
    elif choose == 8:
        OrderProduct()
    elif choose == 0:
        Exit()
        break