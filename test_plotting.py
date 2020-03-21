import matplotlib.pyplot as plt
import pandas as pd
from utils.plots import plot_timeseries

plt.style.use("fivethirtyeight")

data_path = "COVID-19-data/csse_covid_19_data/csse_covid_19_time_series/"

file = "time_series_19-covid-Deaths.csv"

data = pd.read_csv(data_path + file)

fig = plt.figure(figsize=(7, 7))

ax = fig.add_subplot(111)

countries = ["Italy", "Spain", "France"]

plot_timeseries(ax, data, countries, "Deaths", file_name="deaths.pdf")
