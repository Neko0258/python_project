from flask import Blueprint, request, Response, jsonify
from bson import json_util
from bson.objectid import ObjectId
from flask_swagger.errors import handler
from flask_swagger import client

products = Blueprint('products', __name__)


collection = client.collection
product = collection.product


@products.route('/product', methods=['POST'])
def createProduct():
    productName = request.json['name_product']
    productPrice = request.json['price']
    productQuantity = request.json['quantity']
    productDescription = request.json['description']
    check_production_name = product.find_one({'name_product': productName})
    if not check_production_name and productPrice and productQuantity and productDescription:
        product.insert({'name_product': productName, 'price': productPrice, \
             'quantity': productQuantity, 'description': productDescription})
        response = jsonify(message='Create product successful')
        response.status_code = 201
        return response
    else:
        return handler.not_found()


@products.route('/product/quantity', methods=['GET'])
def showQuantityAllProdcut():
    quantity = product.find({})
    response = json_util.dumps(quantity)
    return Response(response, mimetype="application/json")
    
@products.route('/product/update/<id>', methods=['PUT'])
def updateProduct(id):
    checkProductID = product.find_one({"_id": ObjectId(id)})
    productName = request.json["name_product"]
    productPrice = request.json["price"]
    productQuantity = request.json["quantity"]
    productDescription = request.json["description"]
    
    
    if checkProductID:
        product.update_one({'_id': ObjectId(id)}, {'$set': {'name_product': productName,\
             'price': productPrice, 'quantity': productQuantity, 'description': productDescription}})
        response = jsonify(message='User ' + id + ' Update successfully')
        response.status_code = 200
        return response
    else:
        return handler.not_found()

@products.route('/product/delete/<id>', methods=['DELETE'])
def deleteProduct(id):
    checkProductID = product.find_one({"_id": ObjectId(id)})
    if checkProductID:
        product.delete_one({'_id': ObjectId(id)})
        response = jsonify(message='Product ' + id + ' has been deleted!')
        return response
    else:
        return handler.not_found()

@products.route('/order/<id>', methods=['PUT'])
def order(id):
    checkProductID = product.find_one({"_id": ObjectId(id)}) #just for checking data
    #quantityOrder = request.args.get("quantity")
    quantityOrder = request.json["quantity"]
    
    if checkProductID:
        product.update_one({"_id": ObjectId(id)}, {"$inc": {"quantity": -int(quantityOrder)}})
        price = product.find_one({"_id": ObjectId(id)}, {"price"})
        totalCost = price["price"] * int(quantityOrder)
        response = jsonify(message="Total cost = %s" %totalCost)
        return response
    else:
        return handler.not_found()