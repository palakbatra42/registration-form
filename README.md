# Lead Management System

A Django-based Lead Management System with JWT authentication and REST APIs for managing leads. The application provides secure CRUD operations, authentication, and lead management features.

---

## Features

* User Authentication using JWT
* Create, Read, Update, and Delete (CRUD) Leads
* Protected APIs with authentication
* Lead status management
* Input validation
* REST API built with Django REST Framework
* API tested using Postman

---

## Technologies Used

* Python 3
* Django
* Django REST Framework
* Simple JWT
* MySQL
* Postman

---

## Project Structure

```text
.
├── blog/
├── project/
│   ├── Controller/
│   ├── Models/
│   ├── Routes/
│   └── Templates/
├── manage.py
└── README.md
```

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/your-repository.git
```

### Navigate to the Project

```bash
cd your-repository
```

### Install Dependencies

```bash
pip install django djangorestframework djangorestframework-simplejwt pymysql
```

### Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Run the Server

```bash
python manage.py runserver
```

The project will be available at:

```
http://127.0.0.1:8000/
```

---

# Authentication

The project uses JWT Authentication.

## Generate Token

**POST**

```
/api/token/
```

Request

```json
{
    "username": "your_username",
    "password": "your_password"
}
```

Response

```json
{
    "refresh": "<refresh_token>",
    "access": "<access_token>"
}
```

---

## Refresh Token

**POST**

```
/api/refresh/
```

Request

```json
{
    "refresh": "<refresh_token>"
}
```

---

## Authorization Header

```
Authorization: Bearer <access_token>
```

---

# API Endpoints

| Method | Endpoint                 | Description          |
| ------ | ------------------------ | -------------------- |
| POST   | `/api/token/`            | Generate JWT Token   |
| POST   | `/api/refresh/`          | Refresh Access Token |
| GET    | `/api/list/`             | Get All Leads        |
| POST   | `/api/list/add/`         | Add New Lead         |
| PATCH  | `/api/list/update/<id>/` | Update Lead          |
| DELETE | `/api/list/delete/<id>/` | Delete Lead          |

---

## Sample Add Lead Request

```json
{
    "name": "John Doe",
    "email": "john@example.com",
    "phone": "9876543210",
    "status": "New"
}
```

---

## Status Codes

| Code | Description           |
| ---- | --------------------- |
| 200  | OK                    |
| 201  | Created               |
| 400  | Bad Request           |
| 401  | Unauthorized          |
| 404  | Not Found             |
| 500  | Internal Server Error |

---

## API Testing

All APIs were tested using Postman.

The Postman collection is included in the project:

```
Lead Management API.postman_collection.json
```

---

## Author

Palak Batra
