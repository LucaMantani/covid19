import pandas as pd
import numpy as np


def Data_Reader(final_date='03-20-2020'):


    path = 'COVID-19-data/csse_covid_19_data/csse_covid_19_daily_reports/'

    day = np.arange(1, 32)
    year = 2020
    final_day = int(final_date[3:5])
    final_month = int(final_date[0:2])
    month = np.arange(1, final_month + 1)
    main_dict = {}

    for m in month:
        for d in day:
            if (d == final_day) & (m == final_month):
                break

            if (m == 1) & (d < 22):
                # Ignores the days in Jan where we have no data
                continue

            else:
                if d < 10:
                    date = '0' + str(m) + '-' + '0' + str(d) + '-' + str(year)
                    main_dict[date] = pd.read_csv(path + date + '.csv')

                else:

                    if (m == 2) & (d > 29):
                        # Feb has 29 days in 2020
                        continue
                    else:
                        date = '0' + str(m) + '-' + str(d) + '-' + str(year)
                        main_dict[date] = pd.read_csv(path + date + '.csv')

    return main_dict

