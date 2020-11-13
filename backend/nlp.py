#!/usr/bin/env python3

from   utils  import dbg_print, dbg_print_mult
from   spacy  import displacy
import de_core_news_lg
import wikipedia
import requests
import word2vec
import gensim
import spacy
import nltk
import sys
import re
import os

### Above: what I found in files. Below: What I added myself.
from gensim.models import Word2Vec, KeyedVectors

nlp = spacy.load("de_core_news_lg")
doc = ""

# Download language model(s) on the first run.
gScriptDir     = os.path.dirname(os.path.realpath(__file__))
gModelFullpath = os.path.join(gScriptDir, 'models' ,"german.model")
if not os.path.exists(gModelFullpath):
    with open(gModelFullpath, 'wb') as f:
        url = 'https://cloud.devmount.de/d2bc5672c523b086/german.model'
        dbg_print("Downloading 'german.model'...")
        r = requests.get(url, allow_redirects=True)
        f.write(r.content)
        dbg_print("Done! 'german.model' saved under models/.")

### This may seem like butchery but it will save a lot of headaches :)
### One class per previous file.
#--------------------------------------------------------------------------------
class Sentence:
    def simplifysentence(self, sentence):
        return "simplified"


    def sentenceWithoutSubSentence(self, sentence):
        return "sentence - SubSentence"
#--------------------------------------------------------------------------------
class Question:
    def createTopicQuestion(self, topic):
        return "Was ist " + topic

    def createPersonQuestion(self, rest):
        return "Wer ist " + rest + "?"

    def nounAtTheBeginning(self, rest):
        return "Was" + rest

    def createTermQuestion(self, term):
        return "Was ist den Definition" + term

    def explainDifference(self, term, analogy):
        return "Was ist der Unterschied zwischen" + term + "und" + analogy

    def verbWithSub(self, verb, sub, isPlural):
        if(isPlural):
            return "Wie" + verb + "sind" + sub
        else:
            return "Wie" + verb + "ist" + sub

    def createLocationQuestion(self, word):
        return "Wo liegt " + word + "?"

#--------------------------------------------------------------------------------
class Word2vec:
    #TODO: if theres too much time wasted here, make the model import global
    model = KeyedVectors.load_word2vec_format(gModelFullpath,
                                                       unicode_errors='ignore',
                                                       binary='true')
    def SeachSimilarWord(self, word):
        return self.model.most_similar(word)

#--------------------------------------------------------------------------------
class QuestionBuilder:
    nlp = spacy.load("de_core_news_sm")
    question = Question()

    def buildQuestion(self, label, word):
        if label == "PER":

            return self.question.createPersonQuestion(word)
        if label == "LOC":
            return self.question.createLocationQuestion(word)
        else:
            print(label, word)
            return label

#--------------------------------------------------------------------------------
def checkWiki():
    wikipedia.set_lang("de")
    page = wikipedia.page("KI")
    doc = nlp(page)


def buildQuestions():
    for sentence in doc.sents:
        for nc in sentence.noun_chunks:
            if nc.root.dep_ == "sb":
                print("Was ist " + nc.text + "?")


if __name__ == '__main__':
    print ("meow.")                

