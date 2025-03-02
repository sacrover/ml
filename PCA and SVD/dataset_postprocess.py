import pandas as pd 

covid_data = pd.read_csv("time-series-19-covid-combined.csv")

# print(!dir)
# processed_data = covid_data.copy()
# df = processed_data.groupby(['Country/Region','Province/State'])
z = covid_data.pivot(index=['Country/Region','Province/State'], columns='Date', values='Deaths')

z.index = z.index.droplevel(-1)
print(z.index)
z2 = z.groupby(['Country/Region']).sum()
z2.to_csv('Covid_Deaths.csv')
