from flask import Blueprint, jsonify, request
from server.app import db
from models.restaurant_pizza import RestaurantPizza
from models.pizza import Pizza
from models.restaurant import Restaurant

restaurant_pizza_bp = Blueprint('restaurant_pizzas', __name__)

@restaurant_pizza_bp.route('/restaurant_pizzas', methods=['POST'])
def create_restaurant_pizza():
    data = request.get_json()
    try:
        price = int(data['price'])
        pizza_id = int(data['pizza_id'])
        restaurant_id = int(data['restaurant_id'])

        if price < 1 or price > 30:
            return jsonify({"errors": ["Price must be between 1 and 30"]}), 400

        rp = RestaurantPizza(price=price, pizza_id=pizza_id, restaurant_id=restaurant_id)
        db.session.add(rp)
        db.session.commit()

        response = {
            "id": rp.id,
            "price": rp.price,
            "pizza_id": rp.pizza_id,
            "restaurant_id": rp.restaurant_id,
            "pizza": rp.pizza.to_dict(),
            "restaurant": rp.restaurant.to_dict()
        }
        return jsonify(response), 201

    except (KeyError, ValueError):
        return jsonify({"errors": ["Invalid input"]}), 400
