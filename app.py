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




if __name__ == "__main__":
    app.config['TEMPLATES_AUTO_RELOAD'] = True  # автоматичне оновлення шаблонів
    app.run(debug=True) # Запускаємо веб-сервер з цього файлу