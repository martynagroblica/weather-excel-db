from services.openweather_api import fetch_weather
from services.excel_files import save_to_excel, read_excel_file
from config import Config
import time
from services.dashboard import create_plots


while True:
    weather = fetch_weather()
    save_to_excel(weather)
    # weather_data = read_excel_file(Config.XLSX)
    weather_data = read_excel_file("./services/pogoda_rozszerzona.xlsx")
    create_plots(weather_data)
    print(weather_data, "Lisbon")

    time.sleep(1000)

