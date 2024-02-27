import sqlite3

class CarsDB():
    def __init__(self,dbname):
        self.dbname = dbname
        self.conn = None
        self.cursor = None

    def open(self):
        self.conn = sqlite3.connect(self.dbname)
        self.cursor = self.conn.cursor()

    def close(self):
        self.cursor.close()
        self.conn.close()

    def get_all_cars(self):
        self.open()
        self.cursor.execute("SELECT * FROM cars")
        data = self.cursor.fetchall()
        self.close()
        return data
    
    def get_car(self,car_id):
        self.open()
        self.cursor.execute("SELECT * FROM cars WHERE id=?", [car_id])
        data = self.cursor.fetchone()
        self.close()
        return data
    
    def search_car(self,query):
        self.open()
        query = '%' + query + '%'
        self.cursor.execute("SELECT * FROM cars WHERE (brand LIKE ? OR series LIKE ? OR kuzov LIKE ? OR year LIKE ?)", [query,query,query,query])
        data = self.cursor.fetchall()
        self.close()
        return data