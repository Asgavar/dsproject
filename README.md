_Based on Gender statistics on /r/rateme dataset I want to check, if there exists a relation between age and sex of the author of the post and a feedback, which he is getting from other users. To achieve this, I need to create a model able to classify, if a comment is positive or negative. I can do this using a dataset of tweets from a contest on Kaggle._

### Datasets:
** [Reddit dataset](https://www.kaggle.com/nikkou/gender-statistics-of-rrateme) **  
** [Dataset to train model](https://www.kaggle.com/kazanova/sentiment140) **



### **Step 1: Data preprocessing**
Tokenization — convert sentences to words
Removing unnecessary punctuation, tags
Removing stop words — frequent words such as ”the”, ”is”, etc. that do not have specific semantic
Stemming — words are reduced to a root by removing inflection through dropping unnecessary characters, usually a suffix.
Lemmatization — Another approach to remove inflection by determining the part of speech and utilizing detailed database of the    language.

My first step will be preparing tweets from twitter dataset. To do this, I am going to use NLTK - The Natural Language Toolkit.


### Resources:
[Training a sentiment analysis core ml model](https://heartbeat.fritz.ai/training-a-sentiment-analysis-core-ml-model-28823b21322c)  
[A statistical analysis ml workflow of titanic](https://www.kaggle.com/masumrumi/a-statistical-analysis-ml-workflow-of-titanic)  
[How to build a data science project from scratch](https://medium.freecodecamp.org/how-to-build-a-data-science-project-from-scratch-dc4f096a62a1)  
[matplotlib guide](https://realpython.com/python-matplotlib-guide/)  
[machine learning text processing](https://towardsdatascience.com/machine-learning-text-processing-1d5a2d638958)  
[Sentiment analysis concept - analysis and applications](https://towardsdatascience.com/sentiment-analysis-concept-analysis-and-applications-6c94d6f58c17)  
[nltk](https://www.nltk.org/)  
[python csv](https://realpython.com/python-csv/)  
python data science handbook  
machine learning r brett lantz  
