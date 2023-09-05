from flask import Blueprint, render_template, request, redirect, session, url_for, jsonify
from .model import Order_details, Order_detail, Order, Orders, Product
from . import db
from . import df
import pandas as pd
from datetime import datetime
from sqlalchemy import select, func
from sqlalchemy.orm import aliased, Session
import json
from .Recommendation import generate_recommendations

# from sqlalchemy.orm import sessionmaker
views = Blueprint('views', __name__)

@views.route('/')
def home():
        if request.method == "GET":
                # df = pd.read_csv(r"C:\Users\Daniel\Python-movie-project\project\Daniel\website\static\shoppingcart.csv")
        #      languages = ["C++", "Python", "PHP", "Java", "C", "Ruby",
        #              "R", "C#", "Dart", "Fortran", "Pascal", "Javascript"]
                Itemnames= df['Itemname'].unique().tolist()

                #replace this {} with the (most top 10 products) from db
                # hot_seller_ScalarResult  = db.session.execute(select(Order_detail).order_by(Order_detail.Quantity).limit(10))
                # # db.engine
                # # db.session
                # hot_seller = hot_seller_ScalarResult.scalars().all()
                # print('===',hot_seller)
                # =============== the (most top 10 products) from db ========= {
                # sql:
                        # select job, max(salary) from cmdev.emp
                        # where job in(
                        # select job from cmdev.emp
                        # group by job
                        # order by count(job) desc
                        # )group by job 
                        # limit 10
                      
        # Create an alias for the OrderDetail class
                order_detail_alias = aliased(Order_details)
        # Create a session
                session = db.session
        # Create a subquery to get the Itemnames ordered by count
                subq = (
                session.query(order_detail_alias.Itemname)
                .group_by(order_detail_alias.Itemname)
                .order_by(func.count(order_detail_alias.Itemname).desc())
                .subquery()
                )
        # Build the main SQLAlchemy query using the subquery
                query = (
                session.query(order_detail_alias.Itemname,func.max(order_detail_alias.Price))
                .filter(order_detail_alias.Itemname.in_(subq))
                .group_by(order_detail_alias.Itemname)
                .limit(10)
                )
                
        # Execute the query and fetch the results
                results = query.all()

        # Close the session when done
                print('----------------: ',results)
                session.close()
        return render_template('home.html',  Itemnames=Itemnames, hot_seller=results)

@views.route('/search_input',methods=["POST","GET"])
def search_input():
        if request.method == "POST":
                data = json.loads(request.data)
                search_input = data["search_input"]
                search_input_list = [search_input]
                shoppingcart_list=[]
                # ==========recoommendation_list==========
                recoommendation_list= generate_recommendations(search_history=search_input_list, shoppingcart_list=shoppingcart_list)
                print('==========recoommendation_list==========', recoommendation_list)
                # ==========recoommendation_list==========

                # search_input = request.form["search_input"]
                print("==== search_input ======", search_input)
                # product = db.session.query(Order_details.Itemname, func.max(Order_details.Price)).filter(Order_details.Itemname==search_input).group_by(Order_details.Itemname).first()
                product = db.session.query(Product.Itemname, Product.Price).filter(Product.Itemname==search_input).first()
                
                print('------product----------: ',product)
                return render_template('product_info_recommendation.html', product=product)
                # return redirect(url_for('views.product_info_recommendation',product=product))
               
        elif request.method == "GET":
                return render_template('product_info_recommendation.html')
        
@views.route('/product_info_recommendation/<product>', methods=["GET"])
def product_info_recommendation(product):
        return render_template('shopping_cart.html',product=product)
# @views.route('/cart',methods=["POST","GET"])
# def cart():
#         if request.method == "GET":
                        
#                 return render_template('shopping_cart.html') #,product=product
#         elif request.method == "POST":
#                 return 's'
@views.route('/carts',methods=["POST", "GET"])
def carts():
        if request.method == "GET":
                s = pd.read_csv(r"C:\Users\Daniel\Python-movie-project\project\Daniel\website\static\shoppingcart.csv")
                # ======= create order detail db ==========
                # print(s['Date'][0])
                # datetime_object = datetime.strptime(s['Date'][0], '%d/%m/%Y %H:%M')
                # # datetime_object = datetime.strptime(s['Date'][0], '%Y/%m/%d %H:%M')
                # print(datetime_object)
                # # new_order_details = Order_details(id=5,Itemname="WHITE METAL LANTERN",Quantity=7,Country="United Kingdom",BillNo=581588, date=datetime_object, Price=50.0, Total=350.0) #BillNo=BillNo
                
                # new_order_details = []
                # for i in range(s['id'].count()):
                # # for i in range(5):
                #         datetime_object = datetime.strptime(s['Date'][i], '%d/%m/%Y %H:%M')
                #         order_detail =Order_details(CustomerID=int(s['CustomerID'][i]),Itemname=s['Itemname'][i],Quantity=s['Quantity'][i],Country=s['Country'][i],BillNo=s['BillNo'][i], date=datetime_object, Price=s['Price'][i], item_sum=s['Total'][i])
                #         new_order_details.append(order_detail) #BillNo=BillNo,
                #         print(order_detail)
                # db.session.add_all(new_order_details)
                # db.session.commit()
                # ======= new order detail ==========
                # new_order = Orders(date= datetime.now(), Total = 350.0) #Quantity*Price
                # # new_order = Orders(BillNo=581588, date= datetime.now(), Total = 350.0) #Quantity*Price
                # db.session.add(new_order)
                # db.session.commit()

                # new_order_details = Order_detail(CustomerID=17850, Itemname="WHITE METAL LANTERN",Quantity=7,Country="United Kingdom",BillNo=new_order.BillNo, date=datetime.now(), Price=50.0, item_sum=350.0)
                # new_order_details2 = Order_detail(CustomerID=17850, Itemname="WHITE METAL LANTERN",Quantity=7,Country="United Kingdom",BillNo=new_order.BillNo, date=datetime.now(), Price=50.0, item_sum=350.0)

                # order=[new_order_details,new_order_details2]
                # db.session.add_all(order)
                # db.session.commit()
                # print('new order')
                # =========== init Product list table ======
                # product = db.session.query(Order_details.Itemname, func.max(Order_details.Price)).group_by(Order_details.Itemname)
                # # for i in product:
                # #         print(i)
                # new_product_list=[]
                # for Itemname, Price in product:
                #         new_product=Product(Itemname=Itemname,Price=Price)
                #         new_product_list.append(new_product)
                #         print(new_product)
                #         print(Itemname, Price)
                # db.session.add_all(new_product_list)
                # db.session.commit()                
                return render_template('shopping_cart.html')
                # return render_template('product_info_recommendation.html')
        elif request.method == "POST":
        #        Itemname= request.form.get('Itemname')
        #        Quantity= request.form.get('Quantity')
        #        Country=request.form.get('Country')
        #        Itemname=request.form.get('Itemname')
        #        BillNo=request.form.get('BillNo')
        #        CustomerID=request.form.get('CustomerID')
        #        Price=request.form.get('Price')

        #        new_order_details = Order_details(Itemname=Itemname,Quantity=Quantity,Country=Country,BillNo=BillNo) #BillNo=BillNo
        #        new_order_details = Order_details(Itemname="WHITE METAL LANTERN",Quantity=6,Country="United Kingdom",BillNo=581588) #BillNo=BillNo
        #        db.session.add(new_order_details)
        #        db.session.commit()
               return redirect(url_for('views.home'))
               
               