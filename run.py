from flask import Flask, render_template, url_for


app = Flask(__name__)


products = [
    {
        'id': '0',
        'brand': 'Brand Name 1',
        'name': 'Product Name 1',
        'description': 'This is the description for product 1',
        'price': '10',
        'units_sold': '0'

    },
    {
        'id': '1',
        'brand': 'Brand Name 2',
        'name': 'Product Name 2',
        'description': 'This is the description for product 2',
        'price': '20',
        'units_sold': '1'
    },
    {
        'id': '2',
        'brand': 'Brand Name 3',
        'name': 'Product Name 3',
        'description': 'This is the description for product 3',
        'price': '7',
        'units_sold': '2'

    },
    {
        'id': '3',
        'brand': 'Brand Name 2',
        'name': 'Product Name 4',
        'description': 'This is the description for product 4',
        'price': '30',
        'units_sold': '3'
    },
    {
        'id': '4',
        'brand': 'Brand Name 3',
        'name': 'Product Name 5',
        'description': 'This is the description for product 5',
        'price': '2',
        'units_sold': '4'

    },
    {
        'id': '5',
        'brand': 'Brand Name 4',
        'name': 'Product Name 6',
        'description': 'This is the description for product 6',
        'price': '50',
        'units_sold': '5'
    },
    {
        'id': '6',
        'brand': 'Brand Name 1',
        'name': 'Product Name 7',
        'description': 'This is the description for product 7',
        'price': '9',
        'units_sold': '6'

    },
    {
        'id': '7',
        'brand': 'Brand Name 2',
        'name': 'Product Name 8',
        'description': 'This is the description for product 8',
        'price': '29',
        'units_sold': '7'
    },
    {
        'id': '8',
        'brand': 'Brand Name 4',
        'name': 'Product Name 9',
        'description': 'This is the description for product 8',
        'price': '35',
        'units_sold': '8'
    }
    ]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', products=products, title='Home')


@app.route("/about")
def about():
    return render_template('about.html', title="About")


@app.route("/contact")
def contact():
    return render_template('contact.html', title="Contact")


@app.route("/product/<int:product_id>")
def product_page(product_id):
    product = products[product_id]
    return render_template('product.html', title=(products[product_id])['name'], product=product)


if __name__ == '__main__':
    app.run(debug=True)
