# extract data from twitter
import twint
import pandas as pd

import sys

# solve compatability issues with notebooks and RunTime errors
import nest_asyncio 
nest_asyncio.apply()

# import nltk libraries to clean tweets
#import nltk
#from nltk import sent_tokenize, word_tokenize
#from nltk.stem.snowball import SnowballStemmer
#from nltk.stem.wordnet import WordNetLemmatizer
#from nltk.corpus import stopwords
#import re
#import string

#nltk.download("stopwords")
#stopwords = stopwords.words('english')
#ps= nltk.PorterStemmer()

print("Enter Twitter Username:")

# Configure twint
c = twint.Config()

# extracting data from twitter
c.Username = input()
c.Lang= "en"
c.Pandas = True
c.Limit = 20 

# Saving in dataframes
def column_names():
  return twint.output.panda.Tweets_df.columns
def twint_to_pd(columns):
  return twint.output.panda.Tweets_df[columns]
print(column_names())

# transfer "tweet" column from Twint to Pandas
#column_names()
tdf = twint_to_pd(['tweet']) 

# removing punctuation
#data["tweet"]= data["tweet"].str.replace("[^a-zA-Z0-9]", "")

# store data as csv
c.Store_csv = True
c.Count = True
name = c.Username
c.Output = name + ".csv"

# Run
twint.run.Search(c)

# debug twint pyhton version error
def run_as_command():
    if sys.version_info[:2] < (3, 6):
        print("[-] TWINT requires Python version 3.6+.")
        sys.exit(0)

    #main()

