# Event Management API

This document provides a comprehensive guide to setting up, configuring, and using the backend API for an event management system. The API is built using Flask, SQLAlchemy, and Flask-Login, and allows for user authentication and event management.

## Table of Contents

- [Features](https://github.com/collinsbett023/events-management-backend?tab=readme-ov-file#features)
- [Installation](https://github.com/collinsbett023/events-management-backend?tab=readme-ov-file#installation)
- [Configuration](https://github.com/collinsbett023/events-management-backend?tab=readme-ov-file#configuration)
- [Usage](https://github.com/collinsbett023/events-management-backend?tab=readme-ov-file#usage)
- [API Endpoints](https://github.com/collinsbett023/events-management-backend?tab=readme-ov-file#api-endpoints)
  - [Authentication](https://github.com/collinsbett023/events-management-backend?tab=readme-ov-file#authentication)
    - [Sign Up](https://github.com/collinsbett023/events-management-backend?tab=readme-ov-file#signup)
    - [Login](https://github.com/collinsbett023/events-management-backend?tab=readme-ov-file#login)
    - [Logout](https://github.com/collinsbett023/events-management-backend?tab=readme-ov-file#logout)
- [Example Requests](https://collinsbett023/events-management-backend?tab=readme-ov-file#example-requests)
  - [Using `curl` for API Requests](https://github.com/collinsbett023/events-management-backend?tab=readme-ov-file#using-curl-for-api-requests)
    - [Sign Up:](https://github.com/collinsbett023/events-management-backend?tab=readme-ov-file#sign-up)
    - [Login:](https://github.com/collinsbett023/events-management-backend?tab=readme-ov-file#login-1)
    - [Logout:](https://github.com/collinsbett023/events-management-backend?tab=readme-ov-file#logout-1)
- [Contributing](https://github.com/collinsbett023/events-management-backend?tab=readme-ov-file#contributing)
- [License](https://github.com/collinsbett023/events-management-backend?tab=readme-ov-file#license)

## Features

- User authentication (signup, login, logout)
- Secure password hashing with bcrypt.
- Session management with Flask-Login
- CORS support for cross-origin requests.
- Database migrations with Flask-Migrate

## Installation 

1. **Clone the repository**:

- Use the following command to clone the repository to your local machine:
  
```bash
git@github.com:Dinah-Ngatia5/event-management-api.git
cd event-management-api
```

2. **Create a virtual environment**:

- A virtual environment is necessary to manage dependencies and isolate them from the global Python environment. Create and activate a virtual environment with these commands:

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

5. **Seed the database**:

- I have a `seed.py` file, to populate the database with initial data, run this command:

```bash
python seed.py
```

## Configuration

Configuration settings are managed in the `server/config.py` file. Here are the key settings:

- `SQLALCHEMY_DATABASE_URI`: The URI of the database to connect to.
- `SECRET_KEY`: A secret key used for session management and other security-related features.
- `SQLALCHEMY_TRACK_MODIFICATIONS`: Is set to `False` to disable modification tracking and save resources.

## Usage

1. **Run the application**:

- Start the Flask application with the following command:

```bash
flask run #or  Option 2: python manage.py
```

- The server will start and listen for requests at `http://localhost:5000`.

2. Run with Docker (optional):

- If you prefer using Docker, you can build and run the application using these commands:

```bash
docker build -t event-management-api .
docker run -p 5000:5000 event-management-api

```

## API Endpoints

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
  - Content: `{ "message": "Login successful" }`
  
- Error Response:
  - Code: 401
  - Content: `{ "message": "Invalid credentials" }`


#### Logout

- URL: `/logout`
- Method: `GET`
- Success Response:
  - Code: 200
  - Content: `{ "message": "Logged out successfully" }`


## Example Requests

### Using `curl` for API Requests

#### Sign Up:

Use this `curl` command to send a signup request to the API:

```bash
curl -X POST http://localhost:5000/signup \
-H "Content-Type: application/json" \
-d '{
    "username": "collins001",
    "email": "collinsbett35@gmail.com",
    "password": "aldfwieo234"
}'
```

#### Login:

Use this `curl` command to send a login request to the API:

```bash
curl -X POST http://localhost:5000/login \
-H "Content-Type: application/json" \
-d '{
    "email": "collinsbett35@gmail.com",
    "password": "aldfwieo234"
}'

```

#### Logout:

Use this `curl` command to send a logout request to the API:

```bash
curl -X GET http://localhost:5000/logout

```

## Contributing

Please feel free to send me a [pull request](https://github.com/collinsbett023/events-management-backend/pulls) or open an [issue](https://github.com/collinsbett023/events-management-backend/issues) incase of any bugs.

## License 

See [MIT Licensed](https://github.com/collinsbett023/events-management-backend/blob/main/LICENSE)
