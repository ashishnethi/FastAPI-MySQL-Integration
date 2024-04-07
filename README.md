# FastAPI-MySQL-Integration

## Overview

FastAPI-MySQL-Integration is a Python project that demonstrates the integration of FastAPI with a MySQL database using SQLAlchemy ORM. This project provides a simple RESTful API for creating users and assigning them roles.

## Features

- Create users with name, email, and role ID
- Assign predefined roles to users (roles include administrator and user)
- Validate user input using Pydantic schemas
- Ensure data integrity and relationships using SQLAlchemy ORM
- Easily extendable for additional CRUD operations or endpoints

- ## Setup

1. **Clone the repository:**
2. **Install dependencies:**
3. **Set up the MySQL database:**

- Create a MySQL database and note down the credentials.
- Update the `SQLALCHEMY_DATABASE_URL` in `app/database.py` with your MySQL connection string.

4. **Run the FastAPI application:**
5. **Test the API:**

Use a tool like Postman to send requests to the API endpoints:
- Create a new user: POST http://localhost:8000/users/
  - Example request body:
    ```json
    {
        "name": "John Doe",
        "email": "john@example.com",
        "role_id": 1
    }
    ```

6. **Explore the code:**

- `app/main.py`: Contains the FastAPI application and API endpoints.
- `app/models.py`: Defines SQLAlchemy models for users and roles.
- `app/schemas.py`: Provides Pydantic schemas for request and response validation.
- `app/crud.py`: Implements CRUD operations for interacting with the database.
- `app/database.py`: Configures the database connection and session management.

## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request
