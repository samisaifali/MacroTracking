import requests

query = {  
    'api_key': 'eTGv7JpnyNxyZtdbKcpxlLhxaNs8QfBHRArxfjWu',
    'nutrients': '203,204,205,255',
    'format': 'abridged'
}

fdcId= '790508'

params = { 
    'api_key': 'eTGv7JpnyNxyZtdbKcpxlLhxaNs8QfBHRArxfjWu' 
}

response = requests.get(f'https://api.nal.usda.gov/fdc/v1/food/{fdcId}', params=query)

print(response.json())
