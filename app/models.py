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

# def get_food_data(fdc_id):
#     try:
#         query = {
#             'api_key': 'your_api_key_here',
#             'nutrients': '203,204,205,255',
#             'format': 'abridged'
#         }
#         response = requests.get(f'https://api.nal.usda.gov/fdc/v1/food/{fdc_id}', params=query)
#         response.raise_for_status()  # Raises an exception for HTTP errors
#         return response.json()
#     except requests.exceptions.RequestException as e:
#         print(f"Error fetching data: {e}")
#         return None
