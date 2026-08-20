# Lead Management System

A Django-based Lead Management System with JWT authentication and REST APIs for managing leads. The application provides secure authentication, CRUD operations, lead status management, validation, filtering, exporting, email notifications, and Google Sheets integration.

---

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Environment Setup](#environment-setup)
- [Database Setup](#database-setup)
- [Running the Project](#running-the-project)
- [Authentication](#authentication)
- [API Endpoints](#api-endpoints)
- [Lead Management](#lead-management)
- [Dashboard](#dashboard)
- [CSV and Excel Export](#csv-and-excel-export)
- [Email Notifications](#email-notifications)
- [Google Sheets Integration](#google-sheets-integration)
- [API Testing](#api-testing)
- [Status Codes](#status-codes)
- [Security](#security)
- [Deployment (Railway)](#deployment-railway)
- [GitHub Workflow](#github-workflow)
- [Author](#author)

---

## Project Overview

**Lead Management System** is a Django + Django REST Framework application built to help sales/marketing teams capture, track, and manage leads through their entire lifecycle — from initial contact to conversion. It exposes a secured REST API (JWT-based) for lead CRUD operations, supports filtering/searching/sorting, exports data to CSV/Excel, sends email notifications on lead activity, and integrates with Google Sheets for external synchronization.

The project also includes server-rendered dashboard templates (login/signup, lead listing, lead detail, document handling) alongside the API layer.

---

## Features

- User authentication using JWT (access + refresh tokens)
- Create, Read, Update, and Delete (CRUD) leads
- Protected APIs requiring authentication
- Lead status management (New, Contacted, Qualified, Proposal Sent, Won, Lost)
- Input validation on lead data
- Search and filter leads by Name, Email, Phone, Status, Source, Date Range, and Assigned User
- Sorting of lead records
- Export filtered leads to CSV and Excel, with selectable columns
- Lead status history tracking
- Email notifications when leads are created or updated
- Google Sheets integration for lead export/synchronization
- Duplicate lead handling
- REST API built with Django REST Framework
- API testing via a provided Postman collection

---

## Technology Stack

| Layer | Technology |
|---|---|
| Language | Python 3 |
| Web Framework | Django 5.2.4 |
| API Framework | Django REST Framework |
| Authentication | Simple JWT (`djangorestframework-simplejwt`) + Session Authentication |
| Database | MySQL, configured via `dj-database-url` |
| Phone Number Validation | `django-phonenumber-field` |
| Static Files | WhiteNoise (`whitenoise.middleware.WhiteNoiseMiddleware`, compressed manifest storage) |
| External Integration | Google Sheets API |
| WSGI Server (production) | Gunicorn |
| Hosting / Deployment | Railway (Railpack builder) |
| API Testing | Postman |
| Version Control | Git & GitHub |

---

## Project Structure

```text
.
├── blog/                        # Django project package (settings.py, wsgi.py, main_urls.py — the active ROOT_URLCONF)
├── project/
│   ├── Controller/               # Business logic / view helpers
│   ├── Models/                   # Django models (Lead, User, etc.)
│   ├── Routes/                   # API route handlers
│   │   ├── Api.py
│   │   ├── Lead.py
│   │   ├── Register.py
│   │   ├── Sync.py
│   │   └── Webhook.py
│   └── Templates/
│       ├── Dashboard/            # Lead dashboard, detail, document, record views
│       ├── Register/             # Login, signup, logout, home pages
│       └── Routes/               # Shared base template
├── staticfiles/                  # Collected static assets (admin, DRF UI)
├── manage.py
├── requirements.txt
├── railway.json                  # Railway deployment configuration
├── README.md
└── Lead Management API.postman_collection.json
```

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/your-repository.git
cd your-repository
```

### 2. Create and Activate a Virtual Environment

```bash
python -m venv myenv
```

**Windows:**

```bash
myenv\Scripts\activate
```

**macOS/Linux:**

```bash
source myenv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

If a `requirements.txt` file isn't yet present, install the core packages directly:

```bash
pip install django djangorestframework djangorestframework-simplejwt \
    dj-database-url python-dotenv whitenoise django-phonenumber-field[phonenumbers] \
    mysqlclient gunicorn
```

> Tip: once your environment is set up, freeze it for reproducibility:
> ```bash
> pip freeze > requirements.txt
> ```

---

## Environment Setup

`settings.py` loads variables from a `.env` file at the project root using `python-dotenv`. Create one next to `manage.py`:

```env
# Django core
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
CSRF_TRUSTED_ORIGINS=

# Database (used only when deploying — see Database Setup below)
DATABASE_URL=mysql://user:password@host:3306/dbname

# Email (SMTP)
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-gmail-app-password
```

Notes on what's actually read from the environment in `settings.py`:

| Variable | Used for | Default if unset |
|---|---|---|
| `DEBUG` | Toggles debug mode | `False` |
| `ALLOWED_HOSTS` | Comma-separated allowed hosts | `[]` (empty) |
| `CSRF_TRUSTED_ORIGINS` | Comma-separated trusted origins for CSRF | `[]` (empty) |
| `DATABASE_URL` | Full DB connection string, parsed by `dj-database-url` | falls back to a hardcoded local MySQL config (see below) |
| `EMAIL_HOST_USER` | Gmail SMTP username / from-address | — |
| `EMAIL_HOST_PASSWORD` | Gmail SMTP app password | — |

> ⚠️ **Security note:** `SECRET_KEY` is currently hardcoded directly in `settings.py` rather than read from the environment. Before deploying publicly, move it to an environment variable (`SECRET_KEY = os.getenv("SECRET_KEY")`) and add it to `.env` / Railway variables, then rotate the existing key since it's already present in source.
>
> Never commit your real `.env`, `credentials.json`, or `service.json` files to GitHub. Keep them listed in `.gitignore`.

---

## Database Setup

The project uses **MySQL** as its primary database, resolved by `dj-database-url`:

```python
DATABASE_URL = os.getenv("DATABASE_URL")
if DATABASE_URL:
    DATABASES = {
        "default": dj_database_url.config(default=DATABASE_URL)
    }
else:
    # local dev fallback only
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.mysql",
            "NAME": "newdb",
            "USER": "root",
            "PASSWORD": "root@1234",
            "HOST": "127.0.0.1",
            "PORT": "3306",
        }
    }
```

**Local development:**

1. Create a local MySQL database matching the fallback config (or edit the fallback block in `settings.py` to match your own local credentials):

   ```sql
   CREATE DATABASE newdb;
   ```

2. Apply migrations:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

3. Create a superuser for admin access:

   ```bash
   python manage.py createsuperuser
   ```

**Production / Railway:** set a single `DATABASE_URL` environment variable in Railway's *Variables* tab (Railway auto-generates this when you provision a MySQL database plugin), in the form:

```text
mysql://USER:PASSWORD@HOST:3306/DBNAME
```

When `DATABASE_URL` is present, it takes priority over the local fallback — no other `DB_*` variables are needed.

> ⚠️ The hardcoded local fallback credentials (`root` / `root@1234`) are fine for local development but should never be relied on in a shared or production environment — always set `DATABASE_URL` there.

---

## Running the Project

Start the local development server:

```bash
python manage.py runserver
```

The application will be available at:

```text
http://127.0.0.1:8000/
```

---

## Authentication

The project uses **JWT (JSON Web Token) authentication** via Django REST Framework Simple JWT as the primary method, with Django's `SessionAuthentication` also enabled as a fallback. All API views default to `IsAuthenticated`, and API errors are routed through a custom exception handler (`project.Controller.Api.Api.custom_exception_handler`) for consistent error responses.

Browser-based (template) views use Django's standard session login instead of JWT:
- `LOGIN_URL`: `/login/`
- On login, users are redirected to `Lead:Record`
- On logout, users are redirected to `Register:Login`

### Generate Token

**POST** `/api/token/`

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

### Refresh Token

**POST** `/api/refresh/`

Request:

```json
{
    "refresh": "<refresh_token>"
}
```

### Authorization Header

Use the access token on all protected endpoints:

```text
Authorization: Bearer <access_token>
```

---

## API Endpoints

| Method | Endpoint                   | Description            |
|--------|----------------------------|------------------------|
| POST   | `/api/token/`              | Generate JWT token     |
| POST   | `/api/refresh/`            | Refresh access token   |
| GET    | `/api/list/`               | Get all leads          |
| POST   | `/api/list/add/`           | Add a new lead         |
| PATCH  | `/api/list/update/<id>/`   | Update a lead          |
| DELETE | `/api/list/delete/<id>/`   | Delete a lead          |

### Sample: Add Lead

**POST** `/api/list/add/`

```json
{
    "name": "John Doe",
    "email": "john@example.com",
    "phone": "9876543210",
    "status": "New"
}
```

---

## Lead Management

Supported lead statuses:

- New
- Contacted
- Qualified
- Proposal Sent
- Won
- Lost

Lead records can be created, updated, deleted, filtered, searched, sorted, exported, assigned to users, and tracked through status history.

---

## Dashboard

The dashboard provides lead management and reporting functionality, including:

- Total leads
- Open leads
- Converted leads
- Lost leads
- Recent activity
- Lead filtering and sorting
- Export functionality
- Google Sheets export/synchronization

---

## CSV and Excel Export

Lead data can be exported to **CSV** and **Excel**, filtered by Name, Email, Phone, Status, Source, Date Range, and Assigned User. Users can also select which columns to include in the exported file.

---

## Email Notifications

Email notifications are triggered when a lead is created or updated. Emails can include the lead's name, email, phone, source, and status.

SMTP settings must be configured in `settings.py` (see [Environment Setup](#environment-setup)) for this feature to work.

---

## Google Sheets Integration

The application integrates with the **Google Sheets API** to:

- Add lead data to Google Sheets
- Fetch lead data
- Synchronize lead records
- Avoid duplicate entries

Google Cloud credentials are required. Keep credential files such as `credentials.json` or `service.json` private — **do not commit them to GitHub**.

---

## API Testing

All REST APIs were tested using **Postman**. The collection is included in the repository:

```text
Lead Management API.postman_collection.json
```

Import it into Postman to test JWT authentication, token refresh, lead CRUD operations, protected endpoints, and validation/error responses.

---

## Status Codes

| Code | Description              |
|------|--------------------------|
| 200  | OK                       |
| 201  | Created                  |
| 400  | Bad Request              |
| 401  | Unauthorized             |
| 404  | Not Found                |
| 500  | Internal Server Error    |

---

## Security

- All lead-management API endpoints are protected by JWT authentication.
- Sensitive configuration and credential files must never be committed to the repository.

Recommended `.gitignore` entries:

```text
.env
credentials.json
service.json
__pycache__/
*.pyc
db.sqlite3
myenv/
staticfiles/
```

---

## Deployment (Railway)

The project is configured for deployment on **Railway** using the Railpack builder and Gunicorn as the production WSGI server.

**`railway.json`:**

```json
{
  "$schema": "https://railway.com/railway.schema.json",
  "build": {
    "builder": "RAILPACK",
    "buildEnvironment": "V3"
  },
  "deploy": {
    "runtime": "V2",
    "numReplicas": 1,
    "startCommand": "gunicorn --access-logfile - --error-logfile - blog.wsgi:application",
    "sleepApplication": false,
    "useLegacyStacker": false,
    "ipv6EgressEnabled": false,
    "multiRegionConfig": {
      "ams": {
        "numReplicas": 1
      }
    },
    "restartPolicyType": "ON_FAILURE",
    "restartPolicyMaxRetries": 10
  }
}
```

### Deployment Steps

1. **Push the project to GitHub** (with `.env`, `credentials.json`, and `service.json` excluded via `.gitignore`).
2. **Create a new Railway project** and connect it to the GitHub repository.
3. **Add a MySQL database** on Railway (or connect an external managed MySQL instance), then copy the generated connection values.
4. **Set environment variables** in the Railway project's *Variables* tab — mirror everything from your local `.env` (`SECRET_KEY`, `DEBUG=False`, `ALLOWED_HOSTS`, `DB_*`, `EMAIL_*`, `GOOGLE_SHEETS_*`), plus `ALLOWED_HOSTS` should include your Railway-generated domain.
5. **Confirm the build**: Railway will use the Railpack builder (`buildEnvironment: V3`) to detect and install dependencies from `requirements.txt` automatically.
6. **Static files**: run `python manage.py collectstatic --noinput` as part of the build/release step so `staticfiles/` is populated for production.
7. **Start command**: Railway launches the app via Gunicorn as defined in `railway.json`:
   ```bash
   gunicorn --access-logfile - --error-logfile - blog.wsgi:application
   ```
8. **Region & scaling**: the app is configured to run 1 replica in the Amsterdam (`ams`) region, with automatic restarts on failure (up to 10 retries).
9. **Run migrations** on the deployed environment (via Railway's shell/CLI):
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```
10. Once deployed, Railway will provide a public URL for the application.

---

## GitHub Workflow

```bash
git add .
git commit -m "Update Lead Management System"
git push origin main
```

---

## Author

**Palak Batra**