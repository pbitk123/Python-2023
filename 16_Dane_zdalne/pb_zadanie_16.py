import requests
from pprint import pprint

url = "https://restcountries.com/v3.1/name/Poland?fullText=true"
response = requests.request(method="GET", url=url)

pprint(response.json())
#
#content = response.json()
#population = content['population']
#capital = content['capital'][0]
print()
print(25*"*")
print()
#print(f'{capital}')
powierzchnia = response.json()[0]['population']
print(f'Powierzchnia: {powierzchnia} km2')
print(response.json()[0]['currencies'])
print(response.json()[0]['population'])
print(response.json()[0]['area'])