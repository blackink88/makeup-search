import urllib.request
import json
#User input
search_input = input("Search for your makeup brand: ")
#Request the data needed to be read
with urllib.request.urlopen("http://makeup-api.herokuapp.com/api/v1/products.json") as url:
    data = json.loads(url.read().decode())
#Return the brand that was searched
for values in data:
 if values['brand'] == search_input:
  print(values['brand'])
  print(values['name'])



