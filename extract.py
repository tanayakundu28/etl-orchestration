import requests
import pandas as pd
from transform import convert_to_csv

url = "https://airbnb13.p.rapidapi.com/search-location"

querystring = {"location":"Kolkata","checkin":"2023-10-28","checkout":"2023-10-29","adults":"1","children":"0","infants":"0","pets":"0","page":"1","currency":"INR"}

headers = {
	"X-RapidAPI-Key": "1b4592c084msh8c6c58ace22cb56p1bb1abjsn0cb6773af6ed",
	"X-RapidAPI-Host": "airbnb13.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)
json_data = response.json()

# load the json output into a dataframe
df = pd.DataFrame(json_data['results'])

# transform and convert the dataframe into csv file
convert_to_csv(df)
