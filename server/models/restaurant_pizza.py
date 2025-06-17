from server.app import db
from sqlalchemy_serializer import SerializerMixin

class RestaurantPizza(db.Model,SerializerMixin):
    __tablename__ = 'restaurant_pizzas'
    serialize_rules=('pizza','restaurant',)

    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer)

    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'))
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizzas.id'))


    restaurant = db.relationship("Restaurant", back_populates="restaurant_pizzas")
    pizza = db.relationship("Pizza", back_populates="restaurant_pizzas")