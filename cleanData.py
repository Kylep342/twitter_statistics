import html
import nltk


class CleanTweets(object):
    """
    This class hosts functions centered around organizing words in
    tweets by part-of-speech.
    """
    def __init__(self, input_text):
        """
        Instantiating this object escapes all characters in tweets.
        A CleanTweets() object also provides several attributes
        useful for analzying different aspects of tweets.
        """
        self.text = html.unescape(input_text)
        self.text_list = self.text.split()
        self.word_list = [word for word in self.text_list if
                          word.isalpha() and word != 'RT']
        self.words = " ".join(self.word_list)
        self.hashtags = [word for word in self.text_list if
                         word[0] == '#']
        self.mentions = [word for word in self.text_list if
                         word[0] == '@']

    def get_pos(self, tagset='universal'):
        try:
            return nltk.pos_tag(self.word_list, tagset=tagset)
        except:
            nltk.download('universal_tagset')
            return nltk.pos_tag(self.word_list, tagset=tagset)

    def filter_by_pos(self, pos):
        if pos.upper() not in ['NOUN',
                               'VERB',
                               'ADJECTIVE',
                               'ADJ',
                               'ADVERB',
                               'ADV']:
            print("Invalid part of speech choice.")
            exit()
        elif pos.upper() == 'ADJECTIVE':
            filterpos = 'ADJ'
        elif pos.upper() == 'ADVERB':
            filterpos = 'ADV'
        else:
            filterpos = pos.upper()
        return [word[0] for word in self.get_pos() if word[1] == filterpos]
