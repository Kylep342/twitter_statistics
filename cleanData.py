import html
import nltk


class cleanTweets(object):
    """
    """
    def __init__(self, input_text):
        """
        Instantiating this object escapes
        """
        self.text = html.unescape(input_text)
        self.text_list = self.text.split()
        self.word_list = [word for word in self.text_list if
                          word.isalpha()]
        self.words = " ".join(self.word_list)
        self.hashtags = [word for word in self.text_list if
                         word[0] == '#']
        self.mentions = [word for word in self.text_list if
                         word[0] == '@']

    def get_pos(self, tagset='universal'):
        if tagset == 'universal':
            nltk.download('universal_tagset')
        return nltk.pos_tag(self.word_list, tagset=tagset)
