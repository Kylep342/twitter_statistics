import yaml

from analyzeData import AnalyzeTweets
from cleanData import CleanTweets
from getData import GetTweets


def main():
    instruct = yaml.load(open('instructions.yaml', 'r'))
    for handle in instruct['accounts']:
        # print(handle)
        AnalyzeTweets(CleanTweets(GetTweets().findTweets(handle)).filter_by_pos('noun')).wordfreqgraph(handle)


if __name__ == '__main__':
    main()
