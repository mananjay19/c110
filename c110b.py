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

def randomsetofmean(counter):
    dataset = []
    for i in range(0,counter):
        randomindex = random.randint(0,len(data)-1)
        value = data[randomindex]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

def showfig(meanlist):
    df = meanlist
    fig = ff.create_distplot([df],['average'],show_hist=False)
    fig.show()

def setup():
    meanlist = [] 
    for i in range(0,1000):
        setofmean= randomsetofmean(100)
        meanlist.append(setofmean)
    showfig(meanlist)
    print(statistics.mean(meanlist))
    print(statistics.stdev(meanlist))

setup()