# Twitter Statistics

![Alt text](git_images/@BarackObamas_top_25_nouns.png?raw=true "Sample Plot")

Welcome to Twitter Statictics!

twitter_statistics is a small Python library that allows for graphing
of various natural language analyses of Twitter users' Tweets.

## How to Run

To run an analysis, simply modify the `instructions.yaml` file to include
as many Twitter handles as you need to analyze!

Then run `python twitter_statistics.py noun` and you've got your graphs!

By default, you will get graphs of the top 25 of whatever part of speech you
pass at runtime used by each twitter handle passed in the `instructions.yaml`
file from their most recent 3240 tweets.

If you would like to make any custom modifications to the code, feel free to
adjust which parts of speech are being filtered.

## To come

1. Filtering on multiple parts of speech.
2. Baseline methods that show hashtag and mention statistics.
3. Pettifying the charts generated by pyplot (I've only worked with it for ~30 mins :D)
