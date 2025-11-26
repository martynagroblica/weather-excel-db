from services.openweather_api import fetch_weather
from services.excel_files import save_to_excel, read_excel_file
from config import Config
import time


while True:
    weather = fetch_weather()
    save_to_excel(weather)
    weather_data = read_excel_file(Config.XLSX_PATH)
    print(weather_data)

    time.sleep(10)

