#Beautiful Soup is a Python library for pulling data out of HTML and XML files. 
#It works with your favorite parser to provide idiomatic ways of navigating, searching, and modifying the parse tree.
import bs4 as bs
import urllib.request  #The Requests package is recommended for a higher-level HTTP client interface
import re #regular expression
import nltk

scrapped_data = urllib.request.urlopen('https://en.wikipedia.org/wiki/Machine_learning')
article = scrapped_data .read()

 # Find all of the text between paragraph tags and strip out the html
parsed_article = bs.BeautifulSoup(article,'lxml')

paragraphs = parsed_article.find_all('p')

article_text = ""

for p in paragraphs:
    article_text += p.text

#Reomve Stop Words

try:
    import string
    from nltk.corpus import stopwords
    import nltk
except Exception as e:
    print(e)


class PreProcessText(object):

    def __init__(self):
        pass

    def __remove_punctuation(self, text):

        """
        Takes a String
        return : Return a String
        """

        message = []
        for x in text:
            if x in string.punctuation:
                pass
            else:
                message.append(x)
        message = ''.join(message)

        return message

    def __remove_stopwords(self, text):

        """
        Takes a String
        return List
        """

        words= []
        for x in text.split():

            if x.lower() in stopwords.words('english'):
                pass
            else:
                words.append(x)
        return words


    def token_words(self,text=''):

        """
        Takes String
        Return Token also called list of words that is used to
        Train the Model
        """

        message = self.__remove_punctuation(text)
        words = self.__remove_stopwords(message)
        return words

import nltk
flag = nltk.download("stopwords")

if (flag == "False" or flag == False):
    print("Failed to Download Stop Words")
else:
    print("Downloaded Stop words ...... ")
    helper = PreProcessText()
    #words = helper.token_words(text=txt)
    words = helper.token_words(text=article_text)

#Train Model

from gensim.models import Word2Vec
#model = Word2Vec([words], min_count=1)
model = Word2Vec([words], size=100, window=5, min_count=1, workers=4)
#
workers = use this many worker threads to train the model (=faster training with multicore machines). If your system is having 2 cores,
# and if you specify workers=2, then data will be trained in two parallel ways
vocabulary = model.wv.vocab
sim_words = model.wv.most_similar('cake')
sim_words
