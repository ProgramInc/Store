from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://zem:zemer123!@mystoredbinstance.cct9ivwkorcm.eu-central-1.rds.amazonaws.com/dbstore'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    brand = db.Column(db.String(30), nullable=False)
    name = db.Column(db.String(30), unique=True, nullable=False)
    description = db.Column(db.String(100), unique=True, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    units_sold = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f" 'id': '{self.id}', 'brand': '{self.brand}', 'name': '{self.name}'," \
               f" 'description':'{self.description}', 'price': '{self.price}', 'units_sold': '{self.units_sold}'"


@app.route("/")
@app.route("/home")
def home():
    data = Product.query.all()
    products = []
    for row in data:
        products.append({row})
    return render_template('home.html', products=products, title='Home')


@app.route("/about")
def about():
    return render_template('about.html', title="About")


@app.route("/contact")
def contact():
    return render_template('contact.html', title="Contact")


@app.route("/product/<int:product_id>")
def product_page(product_id):
    product= Product.query.get_or_404(product_id)
    return render_template('product.html', title=product.name, product=product)


if __name__ == '__main__':
    app.run(debug=True)
