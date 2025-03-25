# Josh Talks Task

## Overview
This project provides a task management system with RESTful APIs to:
- Create tasks with a name and description.
- Assign tasks to one or multiple users.
- Retrieve all tasks assigned to a specific user.

Built with Django and Django Rest Framework (DRF), it uses SQLite as the database and follows best practices for clean, modular code with robust error handling.

---

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/MahakGupta03/Josh-Talks-Task.git
   cd Josh-Talks-Task

2. Install dependencies: 
   ```
   pip install -r requirements.txt
   ```

3. Apply migrations:
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```
4. Run the server: 
   ```
   python manage.py runserver
   ```


## API Endpoints

### Create a User

- **URL** - http://127.0.0.1:8000/api/users/
- **Method** - POST
- **Request:**
  ```json
  {
    "name": "John Doe",
    "email": "john@example.com",
    "mobile": "7858523698"
  }
- **Response(201 Created):**
  ```json
  {
    "id": 1,
    "name": "John Doe",
    "email": "john@example.com",
    "mobile": "7858523698"
  }
  ```

### Create a User

- **URL** - http://127.0.0.1:8000/api/tasks/
- **Method** - POST
- **Request:**
  ```json
  {
    "name": "Task 1",
    "description": "First task description"
  }
  ```
- **Response(201 Created):**
  ```json
  {
    "id": 1,
    "name": "Task 1",
    "description": "First task description",
    "created_at": "2023-10-01T12:00:00Z",
    "task_type": "general",
    "completed_at": null,
    "status": "pending",
    "assigned_users": []
  }
  ```

### Assign Task to Users

- **URL** - http://127.0.0.1:8000/api/tasks/<task_id>/assign/
- **Method** - POST
- **Request (Assign task ID to users 1 and 2):**
  ```json
  {
    "user_ids": [1, 2]
  }
  ```
- **Response (200 OK):**
  ```json
  {
    "message": "Users assigned to task"
  }
  ```
- **Error (Task not found):**
  ```json
  {
    "error": "Task not found"
  }
  ```

### Get Tasks for a User

- **URL** - http://127.0.0.1:8000/api/users/<user_id>/tasks/
- **Method** - GET

- **Request (Tasks for user ID 1):** http://127.0.0.1:8000/api/users/1/tasks/

- **Response (200 OK):**
  ```json
  [
    {
      "id": 1,
      "name": "Task 1",
      "description": "First task description",
      "created_at": "2023-10-01T12:00:00Z",
      "task_type": "general",
      "completed_at": null,
      "status": "pending",
      "assigned_users": [1, 2]
    }
  ]
  ```
- **Error (User not found):**
  ```json
  {
    "error": "User not found"
  }
  ```

