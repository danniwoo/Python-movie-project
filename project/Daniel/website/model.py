from . import db
from sqlalchemy.sql import func
# import sqlalchemy
from sqlalchemy import create_engine, text
import pandas as pd
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import Column, Integer, String, Float, Boolean, Date, DateTime, Enum
# offfical
from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase, MappedAsDataclass
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from datetime import datetime
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker

# df = pd.read_csv(r"C:\Users\Daniel\Python-movie-project\project\Daniel\website\static\shoppingcart.csv")
# # df['Itemname'].astype(int)
# print(df)
# # print(df.info())

# engine = create_engine('sqlite:///transection.db', echo=True)
# # Load DataFrame into database table
# df.to_sql("Order_details", engine, index=False, if_exists="replace")
	


# class Base(DeclarativeBase, MappedAsDataclass):
#     pass
# class Order_details(Base):
#     __tablename__ = "Order_details"
 
#     id: Mapped[int] = mapped_column(primary_key=True, init=False)
#     Itemname: Mapped[str] = mapped_column(String(10000))
#     Quantity: Mapped[float]
#     Country: Mapped[str] = mapped_column(String(1000))
#     BillNo: Mapped[int]
#     date: Mapped[datetime] = mapped_column(init=False, server_default=func.now())
#     #  addresses: Mapped[List["Address"]] = relationship(
#     #      back_populates="user", cascade="all, delete-orphan"
#     #  )
 
#     def __repr__(self) -> str:
#         return f"User(id={self.id!r}, Itemname={self.Itemname!r}, Quantity={self.Quantity!r}, Country{self.Country!r})"

# print(new_order_details)


# with engine.connect() as conn:
#     result = conn.execute(text('select "good job test"'))
#     print(result.all())
# Order_details.__table__.drop(engine)
# with engine.begin() as conn:
#     Base.metadata.create_all(conn)

# new_order_details = Order_details(Itemname="WHITE METAL LANTERN",Quantity=6,Country="United Kingdom",BillNo=581588)
# session = Session(engine)
# session.add(new_order_details)
# session.commit()
# # session.flush()
# # print(session.new)
# print(new_order_details)
# session.close()
# ===========================================================================
class Order_details(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    # BillNo = db.Column(db.Integer) #
    CustomerID = db.Column(db.Integer)
    BillNo = db.Column(db.Integer, db.ForeignKey('order.BillNo'))
    Itemname = db.Column(db.String(10000))
    Quantity = db.Column(db.Integer)
    date = db.Column(db.DateTime(timezone=True), default=func.now()) #
    Price=db.Column(db.Float)
    Country = db.Column(db.String(1000))
    item_sum=db.Column(db.Float)
#  Declarative Mapped Class
class Order_detail(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    # BillNo = db.Column(db.Integer) #
    CustomerID = db.Column(db.Integer)
    BillNo = db.Column(db.Integer, db.ForeignKey('orders.BillNo'))
    Itemname = db.Column(db.String(10000))
    Quantity = db.Column(db.Integer)
    date = db.Column(db.DateTime(timezone=True), default=func.now()) #
    Price=db.Column(db.Float)
    Country = db.Column(db.String(1000))
    item_sum=db.Column(db.Float)
    
class Order(db.Model):
    BillNo = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    Total=db.Column(db.Float)
    Order_details = db.relationship('Order_details')
    
class Orders(db.Model):
    BillNo = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    Total=db.Column(db.Float)
    Order_details = db.relationship('Order_detail')

class Product(db.Model):
    ProductId = db.Column(db.Integer, primary_key=True)
    Itemname = db.Column(db.String(10000))
    Price=db.Column(db.Float)
    date = db.Column(db.DateTime(timezone=True), default=func.now())

    # Order_details = db.relationship('Order_detail')

#     email = db.Column(db.String(150), unique=True)
#     password = db.Column(db.String(150))
#     first_name = db.Column(db.String(150))
    # "BillNo" TEXT, 
	# "Itemname" TEXT, 
	# "Quantity" BIGINT, 
	# "Date" TEXT, 
	# "Price" FLOAT, 
	# "CustomerID" TEXT, 
	# "Country" TEXT
