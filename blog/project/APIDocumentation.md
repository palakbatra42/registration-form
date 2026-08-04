# Lead Management API Documentation

## Base URL

```
http://127.0.0.1:8000/api/
```

---

## Authentication

This API uses JWT Authentication.

### Get Access Token

**Endpoint**

```
POST /api/token/
```

**Request**

```json
{
    "username": "tester",
    "password": "tester123"
}
```

**Response**

```json
{
    "refresh": "your_refresh_token",
    "access": "your_access_token"
}
```

### Use the Access Token

Add the following header to protected APIs:

```
Authorization: Bearer <access_token>
```

---

## API Endpoints

### 1. Get All Leads

**Method:** GET

**Endpoint**

```
/api/list/
```

Authentication: Required

---

### 2. Add Lead

**Method:** POST

**Endpoint**

```
/api/list/add/
```

Sample Request

```json
{
    "name": "john",
    "email": "john@example.com",
    "phone": "9876543210",
    "status": "New"
}
```

---

### 3. Update Lead

**Method:** PATCH

**Endpoint**

```
/api/list/update/{id}/
```

Sample Request

```json
{
    "status": "Qualified"
}
```

---

### 4. Delete Lead

**Method:** DELETE

**Endpoint**

```
/api/list/delete/{id}/
```

---

## HTTP Status Codes

- 200 OK
- 201 Created
- 400 Bad Request
- 401 Unauthorized
- 404 Not Found
- 500 Internal Server Error

---

## API Testing

All endpoints were tested using Postman.

The Postman collection is included as:

```
Lead Management API.postman_collection.json
```