import nltk
from nltk.tokenize import word_tokenize
import pandas as pd
from nltk.corpus import stopwords

FILENAME = 'twitterdataset/tweets.csv'
stop_words = set(stopwords.words(‘english’))

wholeset = pd.read_csv(FILENAME, encoding='ISO-8859-1')
wholeset.columns = ['target','text']

def deleteUsernames(file):
	for row in wholeset['text'].iterrows():
		for word in row:
			if (word[0]=='@'):
				row = row.replace(word,'')
	wholeset.to_csv(FILENAME)


def tokenize(file):
	wholeset['text'] = wholeset['text'].apply(word_tokenize)
	wholeset.to_csv(FILENAME)

def removeStopwords(file):
	for row in wholeset['text'].iterrows():
		row = [w for w in row if not w in stop_words]
	wholeset.to_csv(FILENAME)





