# Django Lead Management System

A Django REST Framework based Lead Management System that provides CRUD operations, JWT Authentication, lead filtering, status tracking, and API endpoints.

## Features

- User Authentication using JWT
- Lead Management (Create, Read, Update, Delete)
- REST APIs
- Status Workflow
- Search & Filter Leads
- CSV & Excel Export
- Custom Exception Handling
- MySQL/SQLite Support
- Postman API Testing

---

## Technologies Used

- Python 3.x
- Django
- Django REST Framework
- Simple JWT
- SQLite / MySQL
- Git & GitHub
- Postman

---

## Project Structure

```
project/
│
├── Controller/
├── Models/
├── migrations/
├── Templates/
├── static/
├── manage.py
├── requirements.txt
└── README.md
```

---

## Installation

Clone the repository

```bash
git clone <repository-url>
```

Move into the project directory

```bash
cd project
```

Create Virtual Environment

```bash
python -m venv venv
```

Activate Environment

Windows

```bash
venv\Scripts\activate
```

Install Dependencies

```bash

```

Apply Migrations

```bash
python manage.py migrate
```

Run Server

```bash
python manage.py runserver
```

---

## Authentication

JWT Authentication is implemented.

Generate Token

```
POST /api/token/
```

Refresh Token

```
POST /api/refresh/
```

Add the Access Token in the Authorization header.

```
Authorization: Bearer <access_token>
```

---

## API Endpoints

### Authentication

| Method | Endpoint |
|---------|----------|
| POST | /api/token/ |
| POST | /api/refresh/ |

### Lead APIs

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | /list/ | Get All Leads |
| POST | /list/add/ | Add Lead |
| PUT/PATCH | /list/update/<id>/ | Update Lead |
| DELETE | /list/delete/<id>/ | Delete Lead |

---

## Lead Fields

- Name
- Email
- Phone
- Source
- Status
- Assigned User
- Created Date

---

## Lead Status Workflow

- New
- Contacted
- Qualified
- Proposal Sent
- Won
- Lost

---

## Testing

- Tested using Postman
- JWT Authentication Verified
- CRUD APIs Tested

---

## Future Improvements

- Pagination
- Email Notifications
- Dashboard Analytics
- Role Based Access Control

---

## Author

Palak Batra
