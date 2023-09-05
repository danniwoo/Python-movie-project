
from website import create_app
# from init import SellOrder
from flask import Flask


app= create_app()

if __name__ == '__main__':
    app.run(debug=True)
