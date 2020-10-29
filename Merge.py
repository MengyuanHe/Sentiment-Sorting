import csv
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from collections import Counter
import csv
import pandas as pd

# Taks 1: merge the csv documents in the previous homework
def merge(d=['companylist.csv', 'FE595Data1.csv','Mydata.csv','result.csv']):
    #merging all the csv files into one dataframe
    data = pd.concat(map(pd.read_csv, d),ignore_index=True)
    #return the dataframe to be used in to complete the problem
    return data




