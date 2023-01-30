# Data Analytics script on the gathered information
# Analytics type: Sentiment Analysis
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt

vader = SentimentIntensityAnalyzer()

def graphData(neg, neu, pos, com, l):
    plt.figure(figsize=(14,8))
    plt.subplot(2,2,1)
    plt.title("Negative sentiment")
    plt.hist(neg)
    plt.subplot(2,2,2)
    plt.title("Neutral Sentiment")
    plt.hist(neu)
    plt.subplot(2,2,3)
    plt.title("Positive Sentiment")
    plt.hist(pos)
    plt.subplot(2,2,4)
    plt.title("Compound Sentiment")
    plt.hist(com)
    plt.show()

def computeStats(stats,cont):
    ng = 0
    nu = 0
    ps = 0
    cm = 0
    for i in stats['neg']:
        ng += i
    for j in stats['neu']:
        nu += j
    for k in stats['pos']:
        ps += k
    for l in stats['com']:
        cm += l
    ng = ng/cont
    nu = nu/cont
    ps = ps/cont
    cm = cm/cont
    print("------------- Overall Sentiment --------------\n\nTotal Samples:\t{}\n\nNegative Sentiment:\t{}\nNeutral Sentiment:\t{}\nPositive Sentiment:\t{}\nCompound Sentiment:\t{}\n\n----------------------------------------------\n\n".format(cont,ng,nu,ps,cm))

def graphPolarityScores(polarityMap):
    neg = []
    neu = []
    pos = []
    com = []
    for sentiment, polarity in polarityMap.items():
        neg.append(polarity['neg'])
        neu.append(polarity['neu'])
        pos.append(polarity['pos'])
        com.append(polarity['compound'])
    l = len(com)
    stats = {}
    stats['neg'] = neg
    stats['neu'] = neu
    stats['pos'] = pos
    stats['com'] = com
    computeStats(stats,l)
    graphData(neg, neu, pos, com, l)

dataSource = input("Enter data source: ")
data = open(dataSource,"r")
sentimentMap = {}
for line in data:
    sentimentMap[line.strip()] = vader.polarity_scores(line.strip())
print("Showing the overall gathered sentiments:\n\n")
for sentence, polarity in sentimentMap.items():
    print("[\nSentence:\t{}\nPolarity:\t{}\n[\n\n".format(sentence,polarity))
graphPolarityScores(sentimentMap)
print("End of analysis")