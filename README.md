# Django Without Rest

This project is created while learning Django fundamentals and transitioning towards Django REST Framework (DRF).

It demonstrates how to return data using different approaches like:
- `HttpResponse`
- `JsonResponse`
- Function-Based Views (FBV)
- Class-Based Views (CBV)
- Python API consumption using `requests`
- Basic API testing

---

# 🚀 Project Purpose

The main goal of this project is to understand:

- How Django views work
- Difference between HTML response and JSON response
- How APIs evolve from simple Django views to DRF structure
- Basics of Function-Based Views (FBV)
- Basics of Class-Based Views (CBV)
- Handling different HTTP methods
- Consuming APIs using Python client scripts
- Writing basic API tests

---

# 📌 Features Covered

## 1. Function-Based Views (FBV)

- Returning HTML response using `HttpResponse`
- Returning JSON using `json.dumps()`
- Using `JsonResponse`

---

## 2. Class-Based Views (CBV)

- Basic GET request handling
- Handling multiple HTTP methods:
  - GET
  - POST
  - PUT
  - DELETE

---

## 3. Python API Client

Using Python `requests` library to:

- Consume Django APIs
- Fetch JSON data
- Parse API responses
- Display API data in terminal

---

## 4. Basic API Testing

- Added `test.py`
- Practicing API testing concepts
- Understanding response validation

---

# 🧑‍💻 Example Endpoints

| Endpoint | Description |
|----------|-------------|
| `/emp/` | Returns HTML response |
| `/emp/json/` | Returns JSON using HttpResponse |
| `/emp/json-response/` | Returns JSON using JsonResponse |
| `api/json-cbv/` | Class-based JSON response |
| `api/json-cbv2/` | Handles GET, POST, PUT, DELETE methods |

---

# 📂 Project Structure

```bash
django-to-drf-learning/
│
├── withoutRestAPI/
│   ├── views.py
│   ├── urls.py
│   
│
├── test.py
├── test2.py
├── manage.py
└── README.md
```

---

# ⚙️ Technologies Used

- Python
- Django
- JSON Handling
- HTTP Methods
- Requests Library
- Class-Based Views

---

# 📚 Learning Outcome

Through this project, I learned:

- Difference between HTML and JSON responses
- How APIs work internally
- Why REST APIs are important
- How CBVs make code cleaner and structured
- How Python applications consume APIs
- Basics required before learning Django REST Framework (DRF)

---

# 🚧 Next Steps

- Move towards Django REST Framework (DRF)
- Function-Based Views (FBV)
- Learn Serializers
- Learn APIView
- Add database models
- Add CRUD operations
- Add Authentication
- Connect frontend with APIs

---

# 👨‍💻 Author

**Sajjad Ali**

Learning Django & DRF step by step 🚀

---
