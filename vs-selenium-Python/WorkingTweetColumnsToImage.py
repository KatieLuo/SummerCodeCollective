import twint
import pandas
import sys

# from TwintAttempt import twint_to_pd

print("Enter Twitter Username:")

# Configure
c = twint.Config()
c.Username = input()
c.Limit = 10
name = c.Username

# store data as csv
c.Store_csv = True
c.Count = True
c.Store_csv = True
c.Output = name + ".csv"

# removing punctuation
#data["tweet"]= data["tweet"].str.replace("[^a-zA-Z0-9]", "")

# Run
twint.run.Search(c)
#print(df_pd)

# transfer "tweet" column from Twint to Pandas
df_pd = pandas.read_csv(c.Output)
print(df_pd["tweet"])

# text to image ai
import requests
r = requests.post(
    "https://api.deepai.org/api/text2img",
    data={
        'text': df_pd["tweet"],
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

