# Django Basics to DRF Learning Project

This project is created while learning Django fundamentals and transitioning towards Django REST Framework (DRF).  
It demonstrates how to return data using different approaches like HttpResponse, JsonResponse, and Class-Based Views.

---

## 🚀 Project Purpose

The main goal of this project is to understand:

- How Django views work
- Difference between HTML response and JSON response
- How APIs evolve from simple Django views to DRF structure
- Basics of Class-Based Views (CBV)
- Handling different HTTP methods (GET, POST, PUT, DELETE)

---

## 📌 Features Covered

### 1. Function-Based Views (FBV)
- Returning HTML response using `HttpResponse`
- Returning JSON using `json.dumps()`
- Using `JsonResponse`

### 2. Class-Based Views (CBV)
- Basic GET request handling
- Handling multiple HTTP methods:
  - GET
  - POST
  - PUT
  - DELETE

---

## 🧑‍💻 Example Endpoints

| Endpoint | Description |
|----------|-------------|
| `/emp/` | Returns HTML response (non-REST style) |
| `/emp/json/` | Returns JSON using HttpResponse |
| `/emp/json-response/` | Returns JSON using JsonResponse |
| `/cbv/` | Class-based JSON response |
| `/cbv2/` | Handles GET, POST, PUT, DELETE methods |

---

## 📂 Project Structure

---

## ⚙️ Technologies Used

- Python
- Django
- JSON handling
- Basic HTTP concepts

---

## 📚 Learning Outcome

Through this project, I learned:

- Difference between HTML and JSON responses
- Why REST APIs are important
- How CBVs make code more structured
- Basics required before learning Django REST Framework (DRF)

---

## 🚧 Next Steps

- Move towards Django REST Framework (DRF)
- Use `APIView` and `Serializers`
- Build proper RESTful APIs
- Connect with database models

---

## 👨‍💻 Author

***Sajjad Ali***
Learning Django & DRF step by step 🚀


django-to-drf-learning
