import json
from pprint import pprint

with open('data.json') as f:
    data = json.load(f)


pprint(data[0]['survey'][0]['survey_title'])
pprint(data[0]['survey'][0]['survey_description'])

