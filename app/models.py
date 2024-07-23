import requests

response = requests.get("https://api.nal.usda.gov/fdc/v1/food/790508?format=abridged&nutrients=203&nutrients=204&nutrients=205&api_key=eTGv7JpnyNxyZtdbKcpxlLhxaNs8QfBHRArxfjWu")
print(response.json())