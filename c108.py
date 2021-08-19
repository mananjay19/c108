import pandas as pd
import csv
import plotly.figure_factory as ff

df = pd.read_csv('data.csv')
heightlist = df['Height(Inches)'].tolist()
fig = ff.create_distplot([heightlist],['height'],show_hist=False)
fig.show()