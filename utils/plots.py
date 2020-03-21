import matplotlib.pyplot as plt


def plot_timeseries(ax, data, countries, ylabel, file_name="test.pdf"):

    for country in countries:

        mask = data["Country/Region"] == country

        data_country = data.loc[mask].iloc[:, 40:]

        x = [date[:-3] for date in data_country.columns]
        y = data_country.values.sum(axis=0)

        ax.plot(x, y, label=country)

    ax.legend(frameon=False)
    ax.set_ylabel(ylabel, fontsize=16)
    # ax.set_xlabel("Date", fontsize=16)
    ax.tick_params(axis='x', rotation=45)

    for label in ax.xaxis.get_ticklabels()[::2]:
        label.set_visible(False)

    plt.savefig(file_name)
