from aiohttp import DataQueue
import twint
import pandas
import sys

import nltk
from nltk import sent_tokenize, word_tokenize
from nltk.stem.snowball import SnowballStemmer
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import stopwords
import re
import string

# nltk.download("stopwords")
stopwords = stopwords.words('english')
ps= nltk.PorterStemmer()

print("Enter Twitter Username:")

# Configure
c = twint.Config()
c.Username = input()
# c.Limit = 1000
Pandas = True
name = c.Username

# store data as csv
c.Store_csv = True
c.Count = True
c.Store_csv = True
c.Output = name + ".csv"

# Run
twint.run.Search(c)
#print(df_pd)

# transfer "tweet" column from Twint to Pandas
df_pd = pandas.read_csv(c.Output)

# removing @s
df_pd["tweet"]= df_pd["tweet"].str.replace(r"@[^\s]+", " ")

# removing links
df_pd["tweet"]= df_pd["tweet"].str.replace(r"http\S+", " ")

# removing punctuation
df_pd["tweet"]= df_pd["tweet"].str.replace("[^a-zA-Z0-9]", " ")

#removing tweets less than three characters
df_pd["tweet"]= df_pd["tweet"].apply(lambda x: " ".join ([w for w in x.split() if len (w)>3]))

# tokenization
def tokenize(text):
  tokens = re.split("\W+", text)
  return tokens
df_pd['tweet']= df_pd['tweet'].apply (lambda x: tokenize(x.lower()))

#removing stopwords
def remove_stopword(text):
  text_nostopword= [char for char in text if char not in stopwords]
  return text_nostopword
df_pd['tweet']= df_pd['tweet'].apply(lambda x: remove_stopword(x))

#stemming/lemmatize
def stem(tweet_no_stopword):
  text = [ps.stem ( word) for word in tweet_no_stopword]
  return text
df_pd["tweet"]= df_pd["tweet"].apply(lambda x: stem(x))

#print(df_pd["tweet"])

# clean tweets into a list
data_list = df_pd.loc[:,"tweet"].to_list()
flat_data_list = [item for sublist in data_list for item in sublist]

#print(flat_data_list)

#count frequency
data_count= pandas.DataFrame(flat_data_list)
data_count= data_count[0].value_counts()
from nltk.probability import FreqDist

freq_count = FreqDist()
for words in data_count:
  freq_count[words] +=1
  freq_count

data_count = data_count[:10,]
# print(data_count)

#print(data_count.index)

# freq_list = flat_data_list[words]
# print (freq_list)

top_words = ""
for i in data_count.index:
  top_words += i +" "

print (top_words)

# text to image ai

import requests
r = requests.post(
    "https://api.deepai.org/api/text2img",
    data={
        'text': top_words,
    },
    headers={'api-key': 'ebd84227-71a0-4e66-b308-223348ec1f4e'}
)
print(r.json())

# debug twint pyhton version error
def run_as_command():
    if sys.version_info[:2] < (3, 6):
        print("[-] TWINT requires Python version 3.6+.")
        sys.exit(0)

    #main()

