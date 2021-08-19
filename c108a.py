import pandas as pd
import csv
import plotly.figure_factory as ff

df = pd.read_csv('data.csv')
weightlist = df['Weight(Pounds)'].tolist()
fig = ff.create_distplot([weightlist],['weight'],show_hist=False)
fig.show()