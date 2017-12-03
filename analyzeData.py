import matplotlib.pyplot as plt
import numpy as np

from ListToFreqDict import ListToFreqDict


class AnalyzeTweets(object):
    """
    """

    def __init__(self, wordlist, threshold=5):
        """
        """
        worddict = ListToFreqDict(wordlist)
        self.freqdict = {}
        for word in worddict.keys():
            if worddict[word] > threshold:
                self.freqdict[word] = worddict[word]

    def wordfreqgraph(self, title):
        indexes = np.arange(len(self.freqdict.keys()))
        width = 0.7
        plt.title(title)
        plt.xlabel('Word')
        plt.ylabel('Frequency')
        plt.bar(indexes, self.worddict.values(), width)
        plt.xticks(indexes + width * 0.5, self.freqdict.keys())
        plt.savefig("plots/{0}.png".format(title))
