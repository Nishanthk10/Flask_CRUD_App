from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.automap import automap_base
from unittest.mock import MagicMock
from sqlalchemy import create_engine
from sqlalchemy import text
from sqlalchemy.orm import sessionmaker, session,query
from app import Customers


# mock_conn = MagicMock(name="mock_conn")
# mock_conn.execute().return_value.fetchall().return_value = [('BOTTM', 'Bottom-Dollar Markets', 'Elizabeth Lincoln', 'Accounting Manager', '23 Tsawassen Blvd.',	'Tsawassen', 'BC', 'T2F 8M4', 'Canada', '(604) 555-4729', '(604) 555-3745'),]

# mock_db = MagicMock(name = "mock_db")
# mock_db.engine = create_engine('mysql://root:adminroot%40123@localhost/northwind')
# mock_db.engine.connect().return_value = mock_conn
mock_session = MagicMock(spec = sessionmaker)
mock_query = MagicMock(spec = query.filter)

mock_query.filter.return_value = mock_query
mock_query.first.return_value = Customers()

mock_session.query.return_value = mock_query

db_session = mock_session

data = db_session.mock_query(Customers).all()
print(data)

# app = Flask(__name__)
# app.secret_key = "Secret Key"

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:adminroot%40123@localhost/northwind'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  #Doesnt display warnings

# db = SQLAlchemy(app)
# with app.app_context():
#     Base = automap_base()
#     Base.prepare(db.engine, reflect=True)
#     Customers = Base.classes.customers
#     Products = Base.classes.products
#     Orders = Base.classes.orders




# def index():
    # conn = mock_db.engine.connect()
    # result = conn.execute(text("Select * from customer"))
    # customers = result.fetchall()
    # conn.close()

    # return None


# if __name__ == "__main__":
#     with app.app_context():
#         app.run(debug=True)

