import requests

# 1. base url
# 2. end-point

BASE_URL = 'http://127.0.0.1:8000/'
END_POINT = 'api/json-cbv2/'

response1 = requests.get(BASE_URL + END_POINT)
# Convert response into JSON
data1 = response1.json()


response2 = requests.post(BASE_URL + END_POINT)
# Convert response into JSON
data2 = response2.json()


response3 = requests.put(BASE_URL + END_POINT)
# Convert response into JSON
data3 = response3.json()


response4 = requests.delete(BASE_URL + END_POINT)
# Convert response into JSON
data4 = response4.json()


print("="*35)
print(data1)  # {'msg': 'This is GET method'}
print("="*35)

print()

print("="*35)
print(data2)  # {'msg': 'This is GET method'}
print("="*35)

print()

print("="*35)
print(data3)  # {'msg': 'This is GET method'}
print("="*35)

print()

print("="*35)
print(data4)  # {'msg': 'This is GET method'}
print("="*35)
