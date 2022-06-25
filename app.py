import json

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

from models import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSON_AS_ASCII'] = False

db = SQLAlchemy(app)


@app.route('/users', methods=['GET', 'POST'])
def users():
    if request.method == 'GET':
        res = []
        for user in User.query.all():
            res.append(user.to_dict())
        return jsonify(res)
    if request.method == 'POST':
        user = json.loads(request.data)
        new_user_obj = User(
            id=user['id'],
            first_name=user['first_name'],
            last_name=user['last_name'],
            age=user['age'],
            email=user['email'],
            role=user['role'],
            phone=user['phone']
        )
        db.session.add(new_user_obj)
        db.session.commit()
        return "Пользователь создан в базе данных"


@app.route('/users/<int:user_id>', methods=['GET', 'PUT', 'DELETE'])
def one_user(user_id):
    if request.method == 'GET':
        user = User.query.get(user_id)
        if user is None:
            return "Не найдено"
        else:
            return jsonify(user.to_dict())
    elif request.method == 'PUT':
        user_data = json.loads(request.data)
        user = db.session.query(User).get(user_id)
        if user is None:
            return "Пользователь не найден"
        user.first_name = user_data['first_name'],
        user.last_name = user_data['last_name'],
        user.age = user_data['age'],
        user.email = user_data['email'],
        user.role = user_data['role'],
        user.phone = user_data['phone']
        return f"Объект с id {user_id} успешно изменен"
    elif request.method == 'DELETE':
        user = User.query.get(user_id)
        if user is None:
            return "Пользователь не найден"
        db.session.delete(user)
        db.session.commit()
        return f"Объект с id {user_id} успешно удалён"


@app.route('/orders', methods=['GET', 'POST'])
def orders():
    if request.method == 'GET':
        res = []
        for order in Order.query.all():
            res.append(order.to_dict())
        return jsonify(res)
    if request.method == 'POST':
        order = json.loads(request.data)
        new_order_obj = Order(
            id=order['id'],
            name=order['name'],
            description=order['description'],
            start_date=order['start_date'],
            end_date=order['end_date'],
            address=order['address'],
            price=order['price'],
            customer_id=order['customer_id'],
            executor_id=order['executor_id']
        )
        db.session.add(new_order_obj)
        db.session.commit()
        return "Заказ создан в базе данных"


@app.route('/orders/<int:order_id>', methods=['GET', 'PUT', 'DELETE'])
def one_order(order_id):
    if request.method == 'GET':
        order = Order.query.get(order_id)
        if order is None:
            return "Заказ не найден"
        else:
            return jsonify(order.to_dict())
    elif request.method == 'PUT':
        order_data = json.loads(request.data)
        order = Order.query.get(order_id)
        if order is None:
            return "Заказ не найден"
        order.name = order_data['name'],
        order.description = order_data['description'],
        order.start_date = order_data['start_date'],
        order.end_date = order_data['end_date'],
        order.address = order_data['address'],
        order.price = order_data['price'],
        order.customer_id = order_data['customer_id'],
        order.executor_id = order_data['executor_id']
        return f"Объект с id {order_id} успешно изменен"
    elif request.method == 'DELETE':
        order = Order.query.get(order_id)
        if order is None:
            return "Заказ не найден"
        db.session.delete(order)
        db.session.commit()
        return f"Объект с id {order_id} успешно удалён"


@app.route('/offers', methods=['GET', 'POST'])
def offers():
    if request.method == 'GET':
        res = []
        for offer in Offer.query.all():
            res.append(offer.to_dict())
        return jsonify(res)
    if request.method == 'POST':
        offer = json.loads(request.data)
        new_offer_obj = Offer(
            id=offer['id'],
            order_id=offer['order_id'],
            executor_id=offer['executor_id']
        )
        db.session.add(new_offer_obj)
        db.session.commit()
        return "Предложение создано в базе данных"


@app.route('/offers/<int:offer_id>', methods=['GET', 'PUT', 'DELETE'])
def one_offer(offer_id):
    if request.method == 'GET':
        offer = Offer.query.get(offer_id)
        if offer is None:
            return "Предложение не найдено"
        else:
            return jsonify(offer.to_dict())
    elif request.method == 'PUT':
        offer_data = json.loads(request.data)
        offer = Offer.query.get(offer_id)
        if offer is None:
            return "Предложение не найдено",
        offer.order_id = offer_data['order_id'],
        offer.executor_id = offer_data['executor_id']
        return f"Объект с id {offer_id} успешно изменен"
    elif request.method == 'DELETE':
        offer = Offer.query.get(offer_id)
        if offer is None:
            return "Предложение не найдено"
        db.session.delete(offer)
        db.session.commit()
        return f"Объект с id {offer_id} успешно удалён"


if __name__ == '__main__':
    app.run()
