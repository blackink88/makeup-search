import urllib.request
import json
#User input
search_brand = input("Enter the brand: ")
#Request the data needed to be read
with urllib.request.urlopen("http://makeup-api.herokuapp.com/api/v1/products.json") as url:
    data = json.loads(url.read().decode())
#Return the brand that was searched
for brands in data:
 d = [k for k,v in brands.items() if v == search_brand]
 print(d)
