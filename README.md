# Event Management API

This document provides a comprehensive guide to setting up, configuring, and using the backend API for an event management system. The API is built using Flask, SQLAlchemy and Redis.It allows for user authentication and event management.

## Requirements

- Python
- Postman - Testing Endpoints.
- Redis - Session Manager.

## Features

- User authentication (signup, login, logout)
- Secure password hashing with bcrypt.
- Session management with Redis.
- CORS support for cross-origin requests.
- Database migrations with Flask-Migrate.
- Endpoint for creating an event.
- Endpoint for listing events.
- Endpoint for booking an event.
- Endpoint for listing events.

## Installation 

1. **Clone the repository**:

- Use the following command to clone the repository to your local machine:
  
```bash
git@github.com:collinsbett023/events-management-backend.git
cd event-management-backend
```

2. **Create a virtual environment**:

- A virtual environment is necessary to manage dependencies and isolate them from the global Python environment. 
- Create and activate a virtual environment with these commands:

```bash
python3 -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
```

3. **Install dependencies**:

- Install the required dependencies listed in the `requirements.txt` file using pip:

```bash
pip install -r requirements.txt

```

4. **Set up the database**:

- Initialize and set up the database with Flask-Migrate commands. Run the following commands to create the database, apply migrations, and set it up:

```csharp
flask db init
flask db migrate
flask db upgrade
```


## Configuration

Configuration settings are managed in the `app/configuration.py` file. Here are the key settings:

- `SQLALCHEMY_DATABASE_URI`: The URI of the database to connect to.
- `SECRET_KEY`: A secret key used for session management and other security-related features.
- `SQLALCHEMY_TRACK_MODIFICATIONS`: Is set to `False` to disable modification tracking and save resources.
- `SESSION_TYPE` = "redis"
- `SESSION_PERMANENT` = False
- `SESSION_USE_SIGNER` = True
- `SESSION_REDIS` = redis.from_url("redis://red-cptadmeehbks73f1of80:6379")

## Usage

1. **Run the application**:

- Start the Flask application with the following command:

```bash
flask run #or  Option 2: python run.py
```

- The server will start and listen for requests at `http://localhost:5000`.

2. Run with Docker (optional):

- If you prefer using Docker, you can build and run the application using these commands:

```bash
docker build -t event-management-backend.
docker run -p 5000:5000 event-management-backend.

```

## API Endpoints
Use Postman application to check te following endpoints
```
  /register - User Signup.
  /login - User Login.
  /logout - User Logout.
  /event - Add an event.
  /events - list all events.
  /events/<int:id> - fetch one event details.
  /events/<int:id> - DELETE - delete an event
  /attendances - POST - Booking an event.
  /attendances - GET - Fetching events attended by user.
  
```

### Authentication

#### Signup

- URL: `/signup`
- Method: `POST`
- Data Params:
  - The request body should include a JSON object with the following fields:
  
```json
{
    "username": "your_username",
    "email": "your_email@gmail.com",
    "password": "your_password"
}

```

- Success Response:
  - Code: 200
  - Content: `{ "message": "User registered successfully" }`
  
- Error Response
  - Code: 400
  - Content: `{ "message": "Error message here" }`

#### Login

- URL: `/login`
- Method: `POST`
- Data Params:
  - The request body should include a JSON object with the following fields:
  
```json
{
    "email": "your_email@gmail.com",
    "password": "your_password"
}

```

- Success Response:
  - Code: 200
- Content: `{ "id": user.id,
             "email": user.email }`
  
- Error Response:
  - Code: 401
  - Content: `{"error": "Unauthorized"}`


#### Logout

- URL: `/logout`
- Method: `GET`
- Success Response:
  - Code: 200
  - Content: `{ "message": "Logout successful" }`


#### Event 

- URL: `/event`
- Method: `POST`
- Success Response:
  - Code: 201
  - Content: `{ "status": "Success",
        "message": "Added event successfully",
        "data": event data }`


#### Events

- URL: `/events`
- Method: `GET`
- Success Response:
  - Code: 200
  - Content: `{
        "status": "Success",
        "message": "Events fetched successfully",
        "data": events_data
    }`


#### Event

- URL: `/events/<int:id>`
- Method: `GET`
- Success Response:
  - Code: 200
  - Content: `{ "event_dict" }`


#### Event

- URL: `/events/<int:id>`
- Method: `DELETE`
- Success Response:
  - Code: 200
  - Content: `{
        "message": "Event deleted."
    }`


#### Attendances
- URL: `/attendances`
- Method: `POST`
- Success Response:
  - Code: 201
  - Content: `{
        "status": "Success",
        "message": "Added attendance successfully",
        "data": attendance_dict
    }`


#### Attendances
- URL: `/attendances`
- Method: `GET`
- Success Response:
  - Code: 200
  - Content: `{
        "status": "Success",
        "message": "Attendances fetched successfully",
        "data": attendances_data
    }`
    
## License 

MIT License

Copyright (c) 2024 Collinsbett023,LameckKambi,SafnetCo2,Oriri04 & Dinah-Ngatia5.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.