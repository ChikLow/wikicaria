from flask import Flask, render_template,request
import os
from scripts_db import CarsDB
app = Flask(__name__)
app.config['SECRET_KEY'] = "1a2b7ggggggqwertyzxcqwechinaitaly328"
PATH = os.path.dirname(__file__) + os.sep
db = CarsDB("cars.db")

@app.route("/")
def index():
    cars = db.get_all_cars()
    return render_template("index.html", title = "site about cars",cars=cars)

@app.route("/car/<car_id>")
def car(car_id):
    car = db.get_car(car_id)
    return render_template("car.html",title = "site about cars",car=car)

@app.route("/search")
def search():
    query = request.args.get("query")
    cars = db.search_car(query)
    return render_template("index.html", title = "site about cars",cars=cars)




if __name__ == "__main__":
    app.config['TEMPLATES_AUTO_RELOAD'] = True  # автоматичне оновлення шаблонів
    app.run(debug=True) # Запускаємо веб-сервер з цього файлу