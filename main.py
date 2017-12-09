import argparse
import yaml

from analyzeData import AnalyzeTweets
from cleanData import CleanTweets
from getData import GetTweets

parser = argparse.ArgumentParser(description='Analyze words by part of speech from Twitter.')
parser.add_argument('poslist',
                    type=str,
                    help='A part of speech to filter text by for analysis.')

args = parser.parse_args()


def main():
    instruct = yaml.safe_load(open('instructions.yaml', 'r'))
    for handle in instruct['accounts']:
        AnalyzeTweets(CleanTweets(GetTweets().findTweets(handle)).filter_by_pos(args.poslist)).wordfreqgraph(handle + "'s top 25 " + args.poslist + "s")


if __name__ == '__main__':
    main()
