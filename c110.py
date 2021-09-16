import pandas as pd
import csv
import random
import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics

df = pd.read_csv('newdata.csv')
data = df['average'].tolist()
populationmean = statistics.mean(data)
populationstd = statistics.stdev(data)
print(populationmean)
print(populationstd)
fig = ff.create_distplot([data],['average'],show_hist=False)
fig.add_trace(go.Scatter(x = [populationmean,populationmean],y = [0,1],mode = 'lines',name = 'mean'))
fig.show()