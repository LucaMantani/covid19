import pandas as pd
from utils.forecast import exp_predict

numbers = ["Confirmed", "Deaths"]

for number in numbers:

    print("Prediction of %s cases tomorrow:" % number)

    data_path = "COVID-19-data/csse_covid_19_data/csse_covid_19_time_series/"

    file = "time_series_19-covid-%s.csv" % number

    data = pd.read_csv(data_path + file)

    countries = ["Italy", "Spain", "France"]

    pred = exp_predict(data, countries)

    for key in pred.keys():
        print("     %s prediction: %i" % (key, int(pred[key])))
