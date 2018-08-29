import requests
import json

#specify url
url = '{API Gateway address}/hello/hessam'
data = {"dateOfBirth": "2000-08-25"}

headers = {"Content-Type" : "application/json"}

#Call REST API
response = requests.get(url, headers=headers)

#Print Response
parsed = json.loads(response.content)
print (json.dumps(parsed, indent=4, sort_keys=True))
