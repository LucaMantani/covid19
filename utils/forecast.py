import pandas as pd
import numpy as np
from scipy.optimize import curve_fit


def exp_predict(data, countries):

    def func(x, a, b, c):
        return a*np.exp(b*x) + c

    predictions = {}

    for country in countries:

        mask = data["Country/Region"] == country

        data_country = data.loc[mask].iloc[:, 40:]

        x = np.arange(0, data_country.shape[1])
        y = data_country.values.sum(axis=0)

        popt, pcov = curve_fit(func, x, y)

        # plt.scatter(x, y, label=country, s=10)
        # plt.plot(x, func(x, *popt))

        prediction = func(x[-1] + 1, *popt) - y[-1]

        predictions[country] = prediction

    return predictions
