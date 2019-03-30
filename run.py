from flask import Flask, render_template, url_for


app = Flask(__name__)


products = [
    {
        'brand': 'Brand Name 1',
        'name': 'Product Name 1',
        'description': 'This is the description for product 1',
        'price': '10 USD'

    },
    {
        'brand': 'Brand Name 2',
        'name': 'Product Name 2',
        'description': 'This is the description for product 2',
        'price': '20 USD'
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


if __name__ == '__main__':
    app.run(debug=True)
