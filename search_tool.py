import urllib.request as request
import json

search_product = input("Search for your makeup brand: ")

with request.urlopen('http://makeup-api.herokuapp.com/api/v1/products.json') as response:
  source = response.read()
data = json.loads(source)


if search_product in data  == True:
 products = data['brand']    
 d = {v[search_product]: h for h, v in products.items()}
 print(d)
else:
  print("Product not found")
