#import streamlit
import pandas as pd
import matplotlib.pyplot as plt
import random

df = pd.read_excel("pogoda_rozszerzona.xlsx")



# Konwersja timestamp na datetime

df["timestamp_dt"] = pd.to_datetime(df["timestamp"],
                                 format="%H:%M:%S %d-%m-%Y")

# Sortowanie po timestamp
df = df.sort_values("timestamp_dt")
print(df.head())

# wykres punktowy: temp vs wilgotność
# plt.figure(figsize=(10,6))
# plt.scatter(df["temp"], df["humidity"], color="skyblue")
# plt.title("Temperatura vs wilgotność")
# plt.xlabel("Temperatura")
# plt.ylabel("Wilgotność")
# plt.grid(True)
# plt.xlim(-30, 50)
# plt.ylim(0, 100)
#plt.show()

# histogram rozkładu
# plt.figure(figsize=(8,6))
# plt.hist(df['temp'], bins=15, color="skyblue", edgecolor='black', alpha=0.7)
# plt.title('Rozkład temperatur')
# plt.xlabel('Temperatura (°C)')
# plt.ylabel('Liczba obserwacji')
# plt.grid(axis='y', alpha=0.75)
# plt.show()

# Histogram rozkładu temperatur
# plt.figure()
# # wyciąganie wartości y, x i informacji o słupkach
# y_values, x_values, patches = plt.hist(df['temp'])
# plt.xlabel("Temperatura")
# plt.ylabel("Liczba obserwacji")
# plt.title("Rozkład temperatur")
# plt.ylim(0,20)
#
# print(y_values, x_values, patches)
# for p in patches:
#     p.set_facecolor((random.random(), random.random(), random.random()))

#plt.show()


# wykres skrzynkowy
# # 5 najpopularniejszych miast
# top_cities = df["place"].value_counts().head().index
# subset = df[df["place"].isin(top_cities)]
# # Tworzymy listę list temperatur dla każdego miasta
# data_to_plot = [subset[subset['place'] == city]['temp'] for city in top_cities]
#
#
# print(data_to_plot)
#
# plt.figure(figsize=(10,6))
# plt.boxplot(data_to_plot, labels=top_cities, patch_artist=True)
# plt.title('Boxplot temperatur dla 5 najpopularniejszych miast')
# plt.xlabel('Miasto')
# plt.ylabel('Temperatura (°C)')
# plt.grid(axis='y', alpha=0.7)
# plt.show()

# city = "Lisbon"
# city_df = df[df["place"] == city]
#
# plt.figure()
# plt.plot(city_df["timestamp_dt"], city_df["temp"], label = "Temperatura", color = "red")
# plt.plot(city_df["timestamp_dt"], city_df["temp_feels_like"], label = "Temperatura odczuwalna", color = "blue")
# plt.legend()
#
# plt.title(f"Temperatura w czasie - {city}")
# plt.show()

# mean_temp = df.groupby("place")["temp"].mean().sort_values(ascending=False)
# print(mean_temp)
# plt.figure()
# plt.bar(mean_temp.index, mean_temp.values)
# plt.show()

# słupkowy ze średnią wilgotnością w miastach
# mean_hum = df.groupby("place")["humidity"].mean().sort_values(ascending=False)
# plt.figure()
# plt.bar(mean_hum.index, mean_hum.values, color='skyblue', edgecolor='black')
# plt.title('Średnia wilgotność w miastach', fontsize=16)
# plt.xlabel('Miasto', fontsize=12)
# plt.ylabel('Średnia wilgotność', fontsize=12)
# plt.grid(axis='y', alpha=0.7)
# plt.xticks(rotation=45)
# plt.show()

# liniowy ze średnią prędkością wiatru w Toronto
# df_toronto = df[df['place'] == 'Toronto']
# wind_daily = df_toronto.groupby(df_toronto['timestamp_dt'].dt.date)['wind'].mean()
# plt.figure()
# plt.plot(wind_daily.index, wind_daily.values, marker='o', color='skyblue')
# plt.title('Średnia prędkość wiatru w Toronto w czasie')
# plt.xlabel('Data')
# plt.ylabel('Średnia prędkość wiatru (m/s)')
# plt.grid(True, alpha=0.7)
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()

# wykres kołowy z udziałem procentowym typów pogody
# weather_counts = df['description'].value_counts()
# print(weather_counts)
# plt.figure(figsize=(10,8))
# colors = ['#%06X' % random.randint(0, 0xFFFFFF) for _ in range(len(weather_counts))]
# plt.pie(weather_counts, labels=None, autopct='%1.0f%%', startangle=90, colors=colors)
# plt.axis('equal')
# plt.legend(weather_counts.index, title="Typ pogody", bbox_to_anchor=(1.05, 0.5), loc='center left')
#
# plt.title("Udział procentowy typów pogody")
# plt.tight_layout()
# plt.show()

# wykres słupkowy z liczbą obserwacji dla każdego miasta
# city_counts = df['place'].value_counts()
# print(city_counts)
# plt.figure(figsize=(12,6))
# bars = plt.bar(city_counts.index, city_counts.values, color='skyblue', edgecolor='black')
# plt.title('Liczba obserwacji dla każdego miasta', fontsize=16)
# plt.xlabel('Miasto', fontsize=12)
# plt.ylabel('Liczba obserwacji', fontsize=12)
# plt.xticks(rotation=45)
# plt.grid(axis='y', alpha=0.7)
# for bar in bars:
#     height = bar.get_height()
#     plt.text(bar.get_x() + bar.get_width()/2, height * 1.01, str(int(height)),
#              ha='center', va='bottom')
# plt.tight_layout()
# plt.show()



# TERAZ ROBIMY PLOTLY
import plotly.express as px

# wykres kołowy

fig = px.pie(
    data_frame = df,
    names = "description",
    title = "Udział typów pogody"
)
fig.show()

# deklaratywne i imperatywne programowanie


# wykres słupkowy

fig = px.bar(
    data_frame = df,
    x = "place",
    title = "Liczba obserwacji w miastach"
)

fig.update_layout(xasis_title="Miasto")
fig.show()



