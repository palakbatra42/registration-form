# Lead Management System

A Django-based Lead Management System with JWT authentication and REST APIs for managing leads. The application provides secure authentication, CRUD operations, lead status management, validation, filtering, exporting, email notifications, and Google Sheets integration.

---

## Features

* User Authentication using JWT
* Create, Read, Update, and Delete (CRUD) Leads
* Protected APIs with authentication
* Lead status management
* Input validation
* Search and filter leads
* Filter by Name, Email, Phone, Status, Source, Date Range, and Assigned User
* Sort lead records
* Export filtered leads to CSV and Excel
* Select columns for export
* Lead status history tracking
* Email notifications when leads are created or updated
* Google Sheets integration for lead export/synchronization
* Duplicate lead handling
* REST API built with Django REST Framework
* JWT access and refresh tokens
* API testing using Postman

---

## Technologies Used

* Python 3
* Django
* Django REST Framework
* Simple JWT
* MySQL
* Google Sheets API
* Postman
* Git & GitHub

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
├── README.md
└── Lead Management API.postman_collection.json
```

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/your-repository.git
```

### 2. Navigate to the Project

```bash
cd your-repository
```

### 3. Create and Activate Virtual Environment

```bash
python -m venv myenv
```

**Windows:**

```bash
myenv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install django djangorestframework djangorestframework-simplejwt pymysql
```

If a `requirements.txt` file is available:

```bash
pip install -r requirements.txt
```

### 5. Configure Database

Configure your MySQL database settings in `settings.py`.

Example:

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "your_database_name",
        "USER": "your_database_user",
        "PASSWORD": "your_database_password",
        "HOST": "localhost",
        "PORT": "3306",
    }
}
```

### 6. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Create Superuser

```bash
python manage.py createsuperuser
```

### 8. Run the Server

```bash
python manage.py runserver
```

The project will be available at:

```text
http://127.0.0.1:8000/
```

---

# Authentication

The project uses **JWT (JSON Web Token) authentication** through Django REST Framework Simple JWT.

## Generate Token

**POST**

```text
/api/token/
```

Request:

```json
{
    "username": "your_username",
    "password": "your_password"
}
```

Response:

```json
{
    "refresh": "<refresh_token>",
    "access": "<access_token>"
}
```

---

## Refresh Token

**POST**

```text
/api/refresh/
```

Request:

```json
{
    "refresh": "<refresh_token>"
}
```

---

## Authorization Header

Use the access token for protected APIs:

```text
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

**POST**

```text
/api/list/add/
```

```json
{
    "name": "John Doe",
    "email": "john@example.com",
    "phone": "9876543210",
    "status": "New"
}
```

---

# Lead Management

The application supports the following lead statuses:

* New
* Contacted
* Qualified
* Proposal Sent
* Won
* Lost

Lead records can be:

* Created
* Updated
* Deleted
* Filtered
* Searched
* Sorted
* Exported
* Assigned to users
* Tracked through status history

---

# Dashboard

The dashboard provides lead management and reporting functionality, including:

* Total Leads
* Open Leads
* Converted Leads
* Lost Leads
* Conversion Rate
* Recent Activity
* Lead filtering
* Lead sorting
* Export functionality
* Google Sheets export/synchronization

---

# CSV and Excel Export

The system supports exporting lead data to:

* CSV
* Excel

Exported data can be filtered based on:

* Name
* Email
* Phone
* Status
* Source
* Date Range
* Assigned User

Users can also select which columns should be included in the exported file.

---

# Email Notifications

The system supports email notifications for lead activities.

Notifications can be triggered when:

* A new lead is created
* An existing lead is updated

The email can contain relevant lead information such as:

* Lead name
* Email
* Phone
* Source
* Status

SMTP settings must be configured in `settings.py` for email functionality.

---

# Google Sheets Integration

The application supports integration with the **Google Sheets API** for exporting or synchronizing lead data.

The integration can be used to:

* Add lead data to Google Sheets
* Fetch lead data
* Synchronize lead records
* Avoid duplicate lead entries

Google Cloud credentials are required for Google Sheets API access.

Keep credential files such as `credentials.json` or `service.json` private and **do not commit them to GitHub**.

---

# API Testing

All REST APIs were tested using **Postman**.

The Postman collection is included in the project:

```text
Lead Management API.postman_collection.json
```

The collection can be imported into Postman to test:

* JWT authentication
* Token refresh
* Get leads
* Add leads
* Update leads
* Delete leads
* Protected API endpoints
* Validation and error responses

---

# Status Codes

| Code | Description           |
| ---- | --------------------- |
| 200  | OK                    |
| 201  | Created               |
| 400  | Bad Request           |
| 401  | Unauthorized          |
| 404  | Not Found             |
| 500  | Internal Server Error |

---

# Security

The project uses JWT authentication to protect API endpoints.

Sensitive configuration files and credentials should not be committed to the repository.

Recommended files to add to `.gitignore`:

```text
.env
credentials.json
service.json
__pycache__/
*.pyc
db.sqlite3
```

---

# GitHub

The project can be managed using Git and GitHub.

Basic commands:

```bash
git add .
git commit -m "Update Lead Management System"
git push origin main
```

---

## Author

**Palak Batra**
