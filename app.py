import json

from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/hotdeal')
def hotdeal_handler():
    with open('./data/hotdeal.json') as json_file:
        data = json.load(json_file)
        return jsonify(data)


@app.route('/product', defaults={'product_id': None})
@app.route('/product/<product_id>', strict_slashes=False)
def get_product(product_id):
    with open("./data/product.json") as json_file:
        data = json.load(json_file)
        return jsonify(data)


@app.route('/category')
def get_category():
    with open('./data/category.json') as json_file:
        data = json.load(json_file)
        return jsonify(data)


@app.route('/intro')
def get_intro_data():
    with open('./data/intro.json') as json_file:
        data = json.load(json_file)
        return jsonify(data)


@app.route('/sample-image')
def get_sample_image():
    return jsonify(
        {'image_url': "https://res.cloudinary.com/vdn1999bxvp/image/upload/v1600095144/intro-home_ua2g6v.png"})


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
