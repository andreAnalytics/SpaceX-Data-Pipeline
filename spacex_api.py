#the below lines fetch data using an API

# import requests
# import pandas as pd

# response = requests.get('https://api.spacexdata.com/v4/launches')
# data = response.json()

# df = pd.DataFrame(data)
# print(df.head())

# the below line fetch data directly using Pandas

import pandas as pd

url = 'https://api.spacexdata.com/v4/launches'

df = pd.read_json(url)
# Print(df.head())

# print(df.columns)

print(df.dtypes)