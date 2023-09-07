from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
import sqlalchemy
import logging
import pandas as pd
import redis
from mlxtend.frequent_patterns import apriori, association_rules

db = SQLAlchemy()
DB_NAME= 'transection.db'
redisClient = redis.Redis(host='localhost', port=6379, decode_responses=True, db=1)
redisdname='CartList'


df = pd.read_csv(r"C:\Users\Daniel\Python-movie-project\project\Daniel\website\static\shoppingcart.csv")
Item_names= df['Itemname'].unique().tolist()

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



def load_and_filiter_data(df, min_support=0.01, min_confidence=0.5):
    # 读取数据
    
    #過濾帳單出現次數小於2次的record
    item_counts = df['Itemname'].value_counts(ascending=False)
    filtered_items = item_counts.loc[item_counts > 1].index
    df = df[df['Itemname'].isin(filtered_items)]
    
    bill_counts = df['BillNo'].value_counts(ascending=False)
    filtered_bills = bill_counts.loc[bill_counts > 1].index
    df = df[df['BillNo'].isin(filtered_bills)]
    
    # Create pivot_table for encoding
    pivot_table = pd.pivot_table(df[['BillNo','Itemname']], index='BillNo', columns='Itemname', aggfunc=lambda x: True, fill_value=False)
    
    # Creaete Frequent table
    frequent_itemsets = apriori(pivot_table, min_support=min_support, use_colnames=True)
    
    # 生成關聯規則
    rules = association_rules(frequent_itemsets, "confidence", min_threshold=min_confidence)
    
    # Based on support sorting    
    rules = rules.sort_values(['confidence', 'lift'], ascending=[False, False])
    return rules
rules=load_and_filiter_data(df)
Top10=list(df.groupby('Itemname')['Quantity'].sum().sort_values(ascending=False).head(10).index)
    