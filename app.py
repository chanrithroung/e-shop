from flask import Flask, render_template

app = Flask(__name__)


 # front-end routes
@app.route('/')
def home():
    return render_template('frontend/home.html')

@app.route('/detail')
def detail():
    return render_template('frontend/detail.html')

@app.route('/shop')
def shop():
    return render_template('frontend/shop.html')


@app.route('/product')
def product():
    return render_template('frontend/product.html')


@app.route('/new')
def new():
    return render_template('frontend/new.html')


###########################################################


# back-end routes
@app.route('/admin')
def admin():
    return render_template('admin/admin.html')


@app.route('/admin/list-product')
def listPorduct():
    return render_template('admin/list-post.html')


@app.route('/admin/add-post')
def addPost():
    return render_template('admin/add-post.html')




if __name__ == '__main__':
    app.run()