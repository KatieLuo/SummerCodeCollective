import twint
import pandas
import sys

print("Enter Twitter Username:")

# Configure
c = twint.Config()
c.Username = input()
c.Limit = 20
name = c.Username

# # store data as csv
# c.Store_csv = True
# c.Count = True
# c.Store_csv = True
c.Output = name + ".csv"

# Run
twint.run.Search(c)

# debug twint pyhton version error
def run_as_command():
    if sys.version_info[:2] < (3, 6):
        print("[-] TWINT requires Python version 3.6+.")
        sys.exit(0)

    #main()

