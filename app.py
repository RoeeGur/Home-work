from flask import Flask, redirect, url_for


app = Flask(__name__)




@app.route('/')
def hello_func():
    return 'Welcome to Home page!'


@app.route('/about')
def about_func():
    #TODO
    # Do something with DB
    return redirect('/catalog')

@app.route('/catalog')
def catalog_func():
    return redirect(url_for('product_func'))

@app.route('/product')
def product_func():
    return 'Welcome to P!'




if __name__ == '__main__':
    app.run(debug=True)