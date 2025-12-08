import mysql.connector
from mysql.connector import Error


def create_record(data):
    try:
        conn = mysql.connector.connect(
            host="localhost",  # lub "127.0.0.1",
            user="root",
            password="Martyn@2000",
            database="weather_db"
        )
        if not conn.is_connected():
            raise Error("Nie połączono")

        cursor = conn.cursor(dictionary=True)

        sql = """
           INSERT INTO records 
           (temp,temp_feels_like,pressure,humidity,weather_desc,place,wind,clouds,created) 
           VALUES 
           (%s, %s, %s, %s, %s, %s, %s, %s, NOW());
       """
        variables = (
            data['temperatura'],
            data['odczuwalna'],
            data['cisnienie'],
            data['wilgotnosc'],
            data['opis'],
            data['miejsce'],
            data['predkosc_wiatru'],
            data['zachmurzenie']
        )
        cursor.execute(sql, variables)
        conn.commit()
        print("Zapisano do MySQL")

    except Error as e:
        print(e)
    finally:
        conn.close()
        cursor.close()


def get_employees():
    try:
        conn = mysql.connector.connect(
            host="localhost", # lub "127.0.0.1",
            user="root",
            password="Martyn@2000",
            database="cwiczenia_db"
        )
        if conn.is_connected():
            print("Nawiązano połączenie")
        else:
            raise Error("Nie połączono")

        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM employees")
        result = cursor.fetchall()
        return result

    except Error as e:
        print(e)
    finally:
        conn.close()
        cursor.close()

data = get_employees()

for x in data:
    print(f"{x.get("first_name")} {x.get("last_name")}")