from flask import Flask, render_template
import random
app = Flask(__name__)




@app.route('/')
def root():
    return render_template('index.html')

@app.route('/products')
def blue():
    return render_template('products.html')

@app.route('/favorite')
def green():
    return render_template('favorite.html')





if __name__ == '__main__':
    app.run(debug=True)