from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
import sqlalchemy
import logging
import pandas as pd

db = SQLAlchemy()
DB_NAME= 'transection.db'

df = pd.read_csv(r"C:\Users\Daniel\Python-movie-project\project\Daniel\website\static\shoppingcart.csv")

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY']= 'ddfoenfwoei iowfmeofoi'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'

    logging.basicConfig()
    logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

    # tell SQLAlchemy the app we are using 
    db.init_app(app) 

    from .views import views

    app.register_blueprint(views, url_prefix="/")
    print(' ================== init flask =============')
    # print(app.config)
    from .model import Order_details
    create_database(app)
    return app

class SellOrder(object):
    def __init__(self,genericName,brandName):
        self.genericName = genericName
        self.brandName = brandName
        

def create_database(app):
    # project\Daniel\instance\transection.db
    # project\Daniel\website\__init__.py
    print(path.exists(r'C:\Users\Daniel\Python-movie-project\project\Daniel\instance'+ '\\'+ DB_NAME))
    # print(path.exists('..\\..\\instance'+ DB_NAME))
    if not path.exists('..\instance'+ DB_NAME):
        # context manager
        with app.app_context():
            # db.drop_all()
            db.create_all()
        #test code
        # from sqlalchemy import create_engine, MetaData, Table

        # # Create a database engine
        # engine = create_engine('sqlite:///transection.db')

        # # Create a metadata object
        # metadata = MetaData()

        # # Define the table you want to drop
        # my_table = Table('my_table_name', metadata, autoload=True, autoload_with=engine)

        # # Drop the table
        # my_table.drop(engine)

        print('created database')