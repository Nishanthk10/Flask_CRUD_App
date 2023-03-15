from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.automap import automap_base


app = Flask(__name__)
app.secret_key = "Secret Key"

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:adminroot%40123@localhost/northwind'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  #Doesnt display warnings

db = SQLAlchemy(app)
with app.app_context():
    Base = automap_base()
    Base.prepare(db.engine, reflect=True)
    Customers = Base.classes.customers
    Products = Base.classes.products
    Orders = Base.classes.orders



@app.route('/')
def index():
    all_data = db.session.query(Customers, Orders).select_from(Customers).join(Orders).filter(Customers.customerid == 'BLONP').all()
    for customer, order in all_data:
        print(order.orderid, order.orderdate, order.shippeddate, order.requireddate)

    return ''
    # return render_template("index.html", employees = all_data)

@app.route('/customers')
def customers():
    all_data = db.session.query(Customers).all()
    return render_template("customer.html", customers = all_data)


@app.route('/customers/insert', methods = ['POST'])
def insertcustomer():
    if request.method == 'POST':
        customerid = request.form['customerid']
        companyname = request.form['companyname']
        contactname = request.form['contactname']
        contacttitle = request.form['contacttitle']
        address = request.form['address']
        city = request.form['city']
        region = request.form['region']
        postalcode = request.form['postalcode']
        country = request.form['country']
        phone = request.form['phone']
        fax = request.form['fax']

        my_data = Customers(customerid=customerid, companyname=companyname, contactname=contactname, contacttitle=contacttitle, address=address, city=city, region=region, postalcode=postalcode, country=country, phone=phone, fax=fax)
        db.session.add(my_data)
        db.session.commit()

        flash("Customer Inserted Successfully")
        return redirect(url_for('customers'))

@app.route('/customers/update', methods = ['GET', 'POST'])
def updatecustomer():
    if request.method == 'POST':
        my_data = db.session.query(Customers).get(request.form.get('customerid'))
        my_data.companyname = request.form['companyname']
        my_data.contactname = request.form['contactname']
        my_data.contacttitle = request.form['contacttitle']
        my_data.address = request.form['address']
        my_data.city = request.form['city']
        my_data.region = request.form['region']
        my_data.postalcode = request.form['postalcode']
        my_data.country = request.form['country']
        my_data.phone = request.form['phone']
        my_data.fax = request.form['fax']
        
        db.session.commit()
        flash("Customer Updated Successfully")
        return redirect(url_for('customers'))
    
@app.route('/customers/delete/<customerid>/', methods = ['GET','POST'])
def deletecustomer(customerid):
    my_data = db.session.query(Customers).get(customerid)
    db.session.delete(my_data)
    db.session.commit()
    flash("Employee Deleted Successfully")
    return redirect(url_for('customers'))

@app.route('/customers/orderhistory/<customerid>/', methods=['POST','GET'])
def orderhistory(customerid):
    all_data = db.session.query(Customers, Orders).select_from(Customers).join(Orders).filter(Customers.customerid == customerid).all()

    return render_template("orderhistory.html", orderhistory = all_data, customerid = customerid)

#Products

@app.route('/products')
def products():
    all_data = db.session.query(Products).all()
    return render_template("products.html", products = all_data)


@app.route('/products/insert', methods = ['POST'])
def insertproduct():
    if request.method == 'POST':
        productid = request.form['productid']
        productname = request.form['productname']
        supplierid = request.form['supplierid']
        categoryid = request.form['categoryid']
        quantityperunit = request.form['quantityperunit']
        unitprice = request.form['unitprice']
        unitsinstock = request.form['unitsinstock']
        unitsonorder = request.form['unitsonorder']
        reorderlevel = request.form['reorderlevel']
        discontinued = request.form['discontinued']

        my_data = Products(productid=productid, productname=productname, supplierid=supplierid, categoryid=categoryid, quantityperunit=quantityperunit, unitprice=unitprice, unitsinstock=unitsinstock, unitsonorder=unitsonorder, reorderlevel=reorderlevel, discontinued=discontinued)
        db.session.add(my_data)
        db.session.commit()

        flash("Product Inserted Successfully")
        return redirect(url_for('products'))

@app.route('/products/update', methods = ['GET', 'POST'])
def updateproduct():
    if request.method == 'POST':
        my_data = db.session.query(Products).get(request.form.get('productid'))
        my_data.productname = request.form['productname']
        my_data.supplierid = request.form['supplierid']
        my_data.categoryid = request.form['categoryid']
        my_data.quantityperunit = request.form['quantityperunit']
        my_data.unitprice = request.form['unitprice']
        my_data.unitsinstock = request.form['unitsinstock']
        my_data.unitsonorder = request.form['unitsonorder']
        my_data.reorderlevel = request.form['reorderlevel']
        my_data.discontinued = request.form['discontinued']
        
        db.session.commit()
        flash("Product Updated Successfully")
        return redirect(url_for('products'))
    
@app.route('/products/delete/<productid>/', methods = ['GET','POST'])
def deleteproduct(productid):
    my_data = db.session.query(Products).get(productid)
    db.session.delete(my_data)
    db.session.commit()
    flash("Employee Deleted Successfully")
    return redirect(url_for('products'))

#Orders

@app.route('/orders')
def orders():
    all_data = db.session.query(Orders).all()
    return render_template("order.html", orders = all_data)


@app.route('/orders/insert', methods = ['POST'])
def insertorder():
    if request.method == 'POST':
        orderid = request.form['orderid']
        customerid = request.form['customerid']
        employeeid = request.form['employeeid']
        orderdate = request.form['orderdate']
        requireddate = request.form['requireddate']
        shippeddate = request.form['shippeddate']
        shipvia = request.form['shipvia']
        freight = request.form['freight']
        shipname = request.form['shipname']
        shipaddress = request.form['shipaddress']
        shipcity = request.form['shipcity']
        shipregion = request.form['shipregion']
        shippostalcode = request.form['shippostalcode']
        shipcountry = request.form['shipcountry']

        my_data = Orders(orderid=orderid, customerid=customerid, employeeid=employeeid, orderdate=orderdate, requireddate=requireddate, shippeddate=shippeddate, shipvia=shipvia, freight=freight, shipname=shipname, shipaddress=shipaddress, shipcity=shipcity, shipregion=shipregion, shippostalcode=shippostalcode, shipcountry=shipcountry)
        db.session.add(my_data)
        db.session.commit()

        flash("Order Inserted Successfully")
        return redirect(url_for('orders'))

@app.route('/orders/update', methods = ['GET', 'POST'])
def updateorder():
    if request.method == 'POST':
        my_data = db.session.query(Orders).get(request.form.get('orderid'))
        my_data.customerid = request.form['customerid']
        my_data.employeeid = request.form['employeeid']
        my_data.orderdate = request.form['orderdate']
        my_data.requireddate = request.form['requireddate']
        my_data.shippeddate = request.form['shippeddate']
        my_data.shipvia = request.form['shipvia']
        my_data.freight = request.form['freight']
        my_data.shipname = request.form['shipname']
        my_data.shipaddress = request.form['shipaddress']
        my_data.shipcity = request.form['shipcity']
        my_data.shipregion = request.form['shipregion']
        my_data.shippostalcode = request.form['shippostalcode']
        my_data.shipcountry = request.form['shipcountry']
        
        db.session.commit()
        flash("Order Updated Successfully")
        return redirect(url_for('orders'))
    
@app.route('/orders/delete/<orderid>/', methods = ['GET','POST'])
def deleteorder(orderid):
    my_data = db.session.query(Orders).get(orderid)
    db.session.delete(my_data)
    db.session.commit()
    flash("Order Deleted Successfully")
    return redirect(url_for('orders'))



if __name__ == "__main__":
    with app.app_context():
        app.run(debug=True)