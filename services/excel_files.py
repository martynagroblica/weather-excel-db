import pandas as pd
import os
from config import Config
import openpyxl

def save_to_excel(data):
    try:
        new_df = pd.DataFrame([data])
        if os.path.exists(Config.XLSX_PATH):
            current = pd.read_excel(Config.XLSX_PATH)
            concat_data = pd.concat([current, new_df], ignore_index=True)
            concat_data.to_excel(Config.XLSX_PATH, index = False)
        else:
            new_df.to_excel(Config.XLSX_PATH, index=False)
    except Exception as e:
        print(e)

def read_excel_file(path):
    try:
        file = pd.read_excel(path)
        return file
    except Exception as e:
        print(e)




























# data1 = {
#     "Kraj": ["Polska", "Niemcy", "Japonia"],
#     "Stolica": ["Warszawa", "Berlin", "Tokio"],
#     "Populacja": ["36", "80", "120"]
# }
#
# df1 = pd.DataFrame(data1)
# print(df1)

#df1.to_csv("test.csv", encoding="utf8")
#df1.to_excel("test.xlsx")
#df1.to_html("test.html")
#df1.to_json("test.json")

# data2 = [
#     {
#     "kraj":"Polska",
#     "stolica":"Warszawa",
#     "populacja":"36"
#     },
#     {
#         "kraj": "Niemcy",
#         "stolica": "Berlin",
#         "populacja": "80"
#     }
# ]
# df2 = pd.DataFrame(data2)
# print(df2)