import pandas as pd
import twint
from datetime import datetime, timedelta
from time import sleep
import os

#query = 'Words OR To OR Search OR here'
start_str = "2020-04-01"
end_str = "2020-06-25"
start_date = pd.to_datetime(start_str, format='%Y-%m-%d', errors='ignore')
end_date = pd.to_datetime(end_str, format='%Y-%m-%d', errors='ignore')
data_folder = "/Path/To/Save/"
filename = f"{data_folder}collect_tweets_{start_str}_{end_str}.txt"
resume_file = f"{data_folder}resume.txt"

c = twint.Config()
c.Verified = True
c.Retweets = False
c.Filter_retweets = False 
c.Hide_output = False
c.Output = filename
c.Resume = resume_file
#c.Search = query
c.Lang = 'en'
c.Links = "exclude"
#c.Custom["tweet"] = ["tweet"]
c.Format = "{tweet}"

while start_date < end_date:

    check = 0
    c.Since = datetime.strftime(start_date, format='%Y-%m-%d')
    c.Until = datetime.strftime(start_date + timedelta(days=1), format='%Y-%m-%d')

    while check < 1:
        try:
            print("Running Search: Check ", start_date)
            twint.run.Search(c)
            check += 1

        except Exception as e:
            # pause when twitter blocks further scraping
            print(e, "Sleeping for 7 mins")
            print("Check: ", check)
            sleep(420)

    # before iterating to the next day, remove the resume file
    os.remove(resume_file)

    # increment the start date by one day
    start_date = start_date + timedelta(days=1)