from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json


# Create your business logic / views here👇.

# Home Page
def home_view(request):
    return render(request, 'testapp/index.html')


# Emp_Data Without Rest 
def emp_data_view(request):
    # emp_no, emp_name, emp_sal, emp_add
    emp_data = {

        'emp_no':   101,
        'emp_name': "Sajjad Ali",
        'emp_sal':  80000,
        'emp_add':  "Mumbra",

    }

    response = f'''
<h1>
    Employee ID: {emp_data['emp_no']} <br>
    Employee Name: {emp_data['emp_name']} <br>
    Employee Salary: {emp_data['emp_sal']} <br>
    Employee Address: {emp_data['emp_add']} <br>
</h1>
<p>☝️This is the API which is not following any rest principle, It is bringing just the Dictionary Data.</p>
'''

    return HttpResponse(response)


# ===================================================
# DJANGO VIEW FUNCTION TO SEND RESPONSE DIRECTLY
# ===================================================

# In Terminal 
# python -m httpie http://127.0.0.1:8000/emp/json/   /   http http://127.0.0.1:8000/emp/json/

def emp_data_json_view(request):
    # emp_no, emp_name, emp_sal, emp_add
    emp_data = {

        'emp_no':   102,
        'emp_name': "Ali",
        'emp_sal':  300000,
        'emp_add':  "Bandra",

    }
    # Dict ===> Json using --> dumps()
    json_data = json.dumps(emp_data)
    return HttpResponse(json_data)


# ===================================================
# DJANGO VIEW FUNCTION TO SEND JsonRESPONSE DIRECTLY
# ===================================================

def emp_data_api_json_view(request):
    # emp_no, emp_name, emp_sal, emp_add
    emp_data = {

        'emp_no':   103,
        'emp_name': "Your Sajju",
        'emp_sal':  1800000,
        'emp_add':  "Kurla",

    }
    
    
    return JsonResponse(emp_data)
