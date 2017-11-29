import html
import nltk


class cleanTweets(object):
    """
    """
    def __init__(self, input_text):
        """
        Instantiating this object escapes
        """
        self.text = html.escape(input_text)
        self.text_list = self.text.split()
        self.word_list = [word for word in self.text_list if
                          word.isalpha()]
        self.hashtags = [word for word in self.text_list if
                         word[0] == '#']
        self.mentions = [word for word in self.text_list if
                         word[0] == '@']
