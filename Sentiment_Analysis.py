import csv
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from collections import Counter
import csv
import pandas as pd

# Taks 2:  Finds the best and worst business idea
def sentimentalaysis(data):
    scores = []
    analyzer = SentimentIntensityAnalyzer()
    for i in range(0, len(data)):
        score = analyzer.polarity_scores(data.Purpose[i])['compound']
        scores.append(score)
    data['Score'] = scores
    data = data.sort_values('Score').reset_index(drop=True)
    print("Best Business Idea\n Company: " + data.Name.iloc[-1] + "\n Purpose: " + data.Purpose.iloc[-1] +
          "\n Score: " + str(data.Score.iloc[-1]))
    print("Worst Business Idea\n Company: "+data.Name[0]+"\n Purpose: "+data.Purpose[0] +
          "\n Score: "+str(data.Score[0]))
    return




