import requests

# 1. base url 
# 2. end point 

BASE_URL = 'http://127.0.0.1:8000/'
# END_POINT = 'emp/json-response/'
END_POINT = 'emp/json/'

respo = requests.get(BASE_URL + END_POINT)

print(type(respo))
print('-'*35)

print(type(respo.json()))
print('-'*15)

# FATCH
# Python Application Accessing this data 
data = respo.json()

print('Data From Django Application')
print('='*40)

print(f'Employee ID : {data['emp_no']}')
print(f'Employee Name : {data['emp_name']}')
print(f'Employee Salary : {data['emp_sal']}')
print(f'Employee Address : {data['emp_add']}')

print('='*40)

print()
print()
print('*'*100)
print()
print()


BASE_URL = 'http://127.0.0.1:8000/'
END_POINT = 'emp/json-response/'


respo = requests.get(BASE_URL + END_POINT)

print(type(respo))
print('-'*35)

print(type(respo.json()))
print('-'*15)

# FETCH
# Python Application Accessing this data 
data = respo.json()

print('Data From Django Application')
print('='*40)

print(f'Employee ID : {data['emp_no']}')
print(f'Employee Name : {data['emp_name']}')
print(f'Employee Salary : {data['emp_sal']}')
print(f'Employee Address : {data['emp_add']}')

print('='*40)


# Both in one 👇

# import requests

# BASE_URL = 'http://127.0.0.1:8000/'

# endpoints = [
#     'emp/json/',
#     'emp/json-response/'
# ]

# for END_POINT in endpoints:

#     print(f'\nFetching from: {END_POINT}')
#     print('=' * 50)

#     response = requests.get(BASE_URL + END_POINT)

#     print(type(response))
#     print('-' * 35)

#     data = response.json()

#     print(type(data))
#     print('-' * 15)

#     print('Data From Django Application')
#     print('=' * 40)

#     print(f"Employee ID : {data['emp_no']}")
#     print(f"Employee Name : {data['emp_name']}")
#     print(f"Employee Salary : {data['emp_sal']}")
#     print(f"Employee Address : {data['emp_add']}")

#     print('=' * 40)

