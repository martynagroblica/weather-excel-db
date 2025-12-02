import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import pandas as pd



def create_plots(df):
    df["timestamp_dt"] = pd.to_datetime(
        df["timestamp"],
        format="%H:%M:%S %d-%m-%Y"
    )
    df = df.sort_values("timestamp_dt")

    fig = make_subplots(
        rows=2, cols=2,
        subplot_titles=["Temperatura","Wilgotność","Ciśnienie","Wiatr"]
    )

    fig.add_trace(
        go.Scatter(y=df["temp"], name="temp"),
        row=1, col=1
    )

    fig.add_trace(
        go.Scatter(y=df["humidity"], name="humidity"),
        row=1, col=2
    )

    fig.add_trace(
        go.Scatter(y=df["pressure"], name="pressure"),
        row=2, col=1
    )

    fig.add_trace(
        go.Scatter(y=df["wind"], name="wind"),
        row=2, col=2
    )

    fig.update_layout(height=700, width=900, title="Wiele wykresów")

    fig.show()

# def line_chart(df, city):
#     df["timestamp_dt"] = pd.to_datetime(
#         df["timestamp"],
#         format="%H:%M:%S %d-%m-%Y"
#     )
#     df = df.sort_values("timestamp_dt")
#
#     sub = df[df["place"] == city].sort_values("timestamp_dt")
#
#     fig = px.line(
#         sub,
#         x="timestamp_dt",
#         y="temp"
#     )
#     fig.show()