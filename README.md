 Pizza API




A RESTful API built with Flask that allows users to manage restaurants, pizzas, and the association between them (restaurant_pizzas).



Setup Instructions

To install dependencies type the following commands into the terminal


  1)pipenv install


  2)pipenv shell


  3)pip install sqlalchemy-serializer



To run the Flask app  type the following commands into the terminal:


  1)export FLASK_APP=app.py

  2)export FLASK_RUN_PORT=4000


  3)flask run



  DATABASE SETUP & SEEDING

  THe database has already been initialised thus there is no reason to run migrations again


  Data has also already been seeded.To seed new data run the following command in the terminal:
        

            python -m seed 



ROUTES SUMMARY 



| Method | Endpoint                | Description                      |
| ------ | ----------------------- | -------------------------------- |
| GET    | `/pizzas`               | Get all pizzas                   |
| GET    | `/restaurants`          | Get all restaurants              |
| GET    | `/restaurants/<int:id>` | Get one restaurant (with pizzas) |
| POST   | `/restaurant_pizzas`    | Create new restaurant-pizza link |
| DELETE | `/restaurants/<int:id>` | Delete a restaurant              |





EXAMPLE OF REQUESTS & RESPONSES
1)GET/pizzas


request=>  GET /pizzas



response

[
  {
    "id": 1,
    "name": "Margherita",
    "ingredients": "cheese, tomato"
  },
  {
    "id": 2,
    "name": "Pepperoni",
    "ingredients": "cheese, tomato, pepperoni"
  }
]


2) GET /restaurants/<id>

request=>  GET /restaurants/1


response 

{
  "id": 1,
  "name": "Pizza Inn",
  "address": "123 Main St",
  "pizzas": [
    {
      "id": 2,
      "name": "Pepperoni",
      "ingredients": "cheese, tomato, pepperoni"
    }
  ]
}


3)POST /restaurant_pizzas

request 


POST /restaurant_pizzas
Content-Type: application/json

{
  "price": 67,
  "pizza_id": 2,
  "restaurant_id": 1
}



response

{
  "id": 1,
  "price": 67,
  "pizza": {
    "id": 2,
    "name": "Pepperoni",
    "ingredients": "cheese, tomato, pepperoni"
  },
  "restaurant": {
    "id": 1,
    "name": "Pizza Inn",
    "address": "123 Main St"
  }
}


3)DELETE /restaurants/<id>

request => DELETE /restaurants/1


response =>{}


Validation Rules


| Field           | Validation                                   |
| --------------- | -------------------------------------------- |
| `price`         | Required, Integer, Between 1 and 30          |
| `pizza_id`      | Required, must reference existing pizza      |
| `restaurant_id` | Required, must reference existing restaurant |


On validation failure, a 400 response will be returned:
{
  "errors": ["Price must be between 1 and 30."]
}




Postman Usage
1)Open Postman and import a new request collection.

2)Set the base URL to http://127.0.0.1:5000/.

3)Add endpoints like:

     > GET /pizzas

     > POST /restaurant_pizzas

     > DELETE /restaurants/:id

For POST requests, select Body → raw → JSON and input:

      {
          "price": 20,
          "pizza_id": 1,
          "restaurant_id": 2
       }


4)Press Send to test


N/B:
   if some commands bring errors in the terminal try running them from the server directory