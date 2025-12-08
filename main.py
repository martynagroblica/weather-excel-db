from services.openweather_api import fetch_weather
from services.excel_files import save_to_excel, read_excel_file
from config import Config
import time
from services.dashboard import create_plots
from services.mysql_db import create_record, get_employees


while True:
    weather = fetch_weather()
    save_to_excel(weather)
    create_record(weather)
    # weather_data = read_excel_file(Config.XLSX_PATH)
    # weather_data = read_excel_file("./services/pogoda_rozszerzona.xlsx")
    # create_plots(weather_data)
    print("Pobrałem dane")

    time.sleep(10)

