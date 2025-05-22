from flask import Flask, render_template, redirect, url_for, session, request

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

# Sample products
products = [
    {'id': 1, 'name': 'Laptop', 'price': 1000, 'category': 'Electronics', 'description': 'A high-end laptop.'},
    {'id': 2, 'name': 'Smartphone', 'price': 600, 'category': 'Electronics', 'description': 'Latest smartphone model.'},
    {'id': 3, 'name': 'Shoes', 'price': 100, 'category': 'Fashion', 'description': 'Comfortable running shoes.'},
    {'id': 4, 'name': 'Backpack', 'price': 50, 'category': 'Accessories', 'description': 'Durable travel backpack.'},
]

@app.route('/')
def index():
    return render_template('index.html', products=products)

@app.route('/product/<int:product_id>')
def product(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    return render_template('product.html', product=product)

@app.route('/add_to_cart/<int:product_id>')
def add_to_cart(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    if product:
        if 'cart' not in session:
            session['cart'] = []
        session['cart'].append(product)
    return redirect(url_for('cart'))

@app.route('/cart')
def cart():
    cart = session.get('cart', [])
    total = sum(item['price'] for item in cart)
    return render_template('cart.html', cart=cart, total=total)

@app.route('/checkout')
def checkout():
    session.pop('cart', None)
    return render_template('checkout.html')

if __name__ == '__main__':
    app.run(debug=True)

app.run(host='0.0.0.0', port=80)
