from sys import argv

from analyzeData import AnalyzeTweets
from cleanData import CleanTweets
from getData import GetTweets

script, handles = argv

def main(handles):
    for handle in handles:
        AnalyzeTweets(CleanTweets(GetTweets().findTweets(handle)).filter_by_pos('noun')).wordfreqgraph(handle)


if __name__ == '__main__':
    main(handles)
