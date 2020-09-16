import json

from flask import Flask, jsonify, request
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/teko"
mongo = PyMongo(app)
ALL_DATA = []
hash_sku = {}

@app.route('/hotdeal')
def hotdeal_handler():
    with open('data/hotdeal.json') as json_file:
        data = json.load(json_file)
        return jsonify(data)


@app.route('/product/<product_sku>', strict_slashes=False)
def get_product(product_sku):
    return jsonify(ALL_DATA[hash_sku[str(product_sku)]])


@app.route('/category')
def get_category():
    with open('data/category.json') as json_file:
        data = json.load(json_file)
        return jsonify(data)


@app.route('/product-range')
def get_product_range():
    start = request.args.get('from', default=0, type=int)
    offset = request.args.get('offset', default=1, type=int)
    return jsonify(ALL_DATA[start:(start + offset)])


@app.route('/all-product')
def get_all_product():
    return jsonify(ALL_DATA)


@app.route('/intro')
def get_intro_data():
    with open('data/intro.json') as json_file:
        data = json.load(json_file)
        return jsonify(data)


@app.route('/sample-image')
def get_sample_image():
    return jsonify(
        {'image_url': "https://res.cloudinary.com/vdn1999bxvp/image/upload/v1600095144/intro-home_ua2g6v.png"})


@app.route('/')
def hello_world():
    return 'Hello World!'


def initialize_data():
    with open('./data/all.json', "r") as fp:
        counter = 0
        for line in fp:
            json_data = json.loads(line)
            ALL_DATA.append(json_data)
            existing_document = mongo.db.teko.find_one(json_data)
            if not existing_document:
                mongo.db.teko.insert(json_data, check_keys=False)
            hash_sku[json_data["sku"]] = counter
            counter += 1


initialize_data()

if __name__ == '__main__':
    app.run()
