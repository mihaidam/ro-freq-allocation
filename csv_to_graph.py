# Mihai DAMIAN
# UVT, Timisoara, 2021

import pandas
import plotly.express as px

# change khz according to desired file
dict_from_csv = pandas.read_csv('./khz_clean.csv', usecols=[1, 2, 3])

dict_from_csv = dict_from_csv.to_dict()

data = dict_from_csv

df = pandas.DataFrame(data)

fig = px.sunburst(df, path=['usess', 'freqs'])

fig.show()
