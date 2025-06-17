from server.app import db
from sqlalchemy_serializer import SerializerMixin


class Pizza(db.Model,SerializerMixin):
    __tablename__='pizzas'
    serialize_rules=('-restaurant_pizzas',)

    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String)
    ingredients=db.Column(db.String)

    restaurant_pizzas= db.relationship("RestaurantPizza", back_populates="pizza")
