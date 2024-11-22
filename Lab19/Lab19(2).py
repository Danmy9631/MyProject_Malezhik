import pandas as pd
import json

with open('pupils.json', 'r') as file:
    pupils_data = json.load(file)

pupils_series = pd.Series(pupils_data)

years_series = pupils_series.apply(lambda date: int(date.split('-')[0]))

years_series.to_json('years.json')

