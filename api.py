from flask import Flask, render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy


app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://wsltest:Test1234!@172.29.64.1:3306/ecommerce-shop'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
class Customer(db.Model):
    __tablename__='customer'
    id = db.Column('Customer_ID', db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
class Product(db.Model):
    __tablename__='product'
    id = db.Column('Product_ID', db.Integer, primary_key=True, autoincrement=True)
    name = db.Column("Product_Name",db.String(100), nullable=False)
    quantity = db.Column(db.Integer,nullable=False)
    description = db.Column(db.String(1000), nullable=False)
    price = db.Column(db.Numeric(precision=8, scale=2), nullable=False)
class Supplier(db.Model):
    __tablename__='supplier'
    id = db.Column('Supplier_ID', db.Integer, primary_key=True, autoincrement=True)
    name = db.Column('Supplier_Name',db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    phone=db.Column("Phone_Number",db.String(100), nullable=False)
    address=db.Column(db.String(1000), nullable=False)


@app.route('/', methods=["GET"])
def home():
    return render_template('index.html')

@app.route('/customers', methods=['GET','POST'])
def customer():
    if request.method == 'POST':
        name=request.form.get('cname')
        email=request.form.get('cemail')
        add=Customer(name=name, email=email)
        
        try:
            
            db.session.add(add)
            db.session.commit()
            return redirect('/customers') 
        except Exception as e:
            return f"There was an issue adding the customer: {e}"
    
    s=Customer.query.all()
    return render_template('customer.html',users=s)

@app.route('/products', methods=['GET','POST'])
def product():
    if request.method == 'POST':
        name=request.form.get('pname')
        quantity=request.form.get('pquan')
        description=request.form.get('pdes')
        quantity=request.form.get('pquan')
        price=request.form.get('pprice')
        add=Product(name=name, quantity=quantity,description=description,price=price)
        
        try:
            
            db.session.add(add)
            db.session.commit()
            return redirect('/products') 
        except Exception as e:
            return f"There was an issue adding the product: {e}"
    s=Product.query.all()
    
    return render_template('product.html',users=s)

@app.route('/suppliers', methods=['GET','POST'])
def supplier():
    if request.method == 'POST':
        name=request.form.get('sname')
        email=request.form.get('semail')
        phone=request.form.get('sphone')
        address=request.form.get('saddress')
        add=Supplier(name=name, email=email,phone=phone,address=address)
        try:
            
            db.session.add(add)
            db.session.commit()
            return redirect('/suppliers') 
        except Exception as e:
            return f"There was an issue adding the supplier: {e}"
    s=Supplier.query.all()
    return render_template('supplier.html',users=s)

if __name__ == "__main__":
    app.run(port=8080,debug=True)
