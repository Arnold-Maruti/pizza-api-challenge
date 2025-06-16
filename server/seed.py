from server.app import create_app, db
from server.models.pizza import Pizza
from server.models.restaurant import Restaurant
from server.models.restaurant_pizza import RestaurantPizza

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()

    
    pepperoni = Pizza(name="Pepperoni", ingredients="Dough, Tomato Sauce, Cheese, Pepperoni")
    margherita = Pizza(name="Margherita", ingredients="Dough, Tomato Sauce, Mozzarella, Basil")
    emma = Pizza(name="Emma", ingredients="Dough, Tomato Sauce, Cheese")

    
    luigis = Restaurant(name="Luigi's Pizza", address="123 Pasta Lane")
    kikis = Restaurant(name="Kiki's Pizza", address="456 Mozzarella Blvd")

    
    rp1 = RestaurantPizza(price=12, pizza=pepperoni, restaurant=luigis)
    rp2 = RestaurantPizza(price=10, pizza=margherita, restaurant=kikis)
    rp3 = RestaurantPizza(price=8, pizza=emma, restaurant=kikis)

    
    db.session.add_all([pepperoni, margherita, emma, luigis, kikis, rp1, rp2, rp3])
    db.session.commit()