import matplotlib.pyplot as plt
import numpy as np

from ListToFreqDict import ListToFreqDict


class AnalyzeTweets(object):
    """
    """

    def __init__(self, wordlist, top=25):
        """
        """
        worddict = ListToFreqDict(wordlist)
        self.freqdict = {}
        for word in worddict.keys():
            self.freqdict[word] = worddict[word]

        self.mostfreqdict = dict(sorted(self.freqdict.items(),
                                 key=lambda x: x[1],
                                 reverse=True)[:top])

    def wordfreqgraph(self, title):
        indexes = np.arange(len(self.mostfreqdict.keys()))
        width = 0.7
        plt.clf()
        plt.title(title)
        plt.xlabel('Word')
        plt.ylabel('Frequency')
        plt.bar(indexes, self.mostfreqdict.values(), width)
        plt.xticks(indexes, self.mostfreqdict.keys(), rotation=90)
        plt.tight_layout()
        plt.savefig("plots/{0}.png".format(title.replace("'", "").replace(" ", "_")))
