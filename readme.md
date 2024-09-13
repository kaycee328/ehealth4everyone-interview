# User Authentication API

This is a simple authentication API that allows users to sign up and log in to the system. The API uses Django Rest Framework and Simple JWT for token-based authentication.

## Features
- User registration (Sign up)
- User login (Sign in)
- JWT-based authentication (access and refresh tokens)

## Prerequisites
Ensure you have the following installed:
- Python 3.x
- Django
- Django Rest Framework
- Simple JWT for token authentication

## Getting Started

### Install Dependencies
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>

### Install the required dependencies
pip install -r requirements.txt


### run database migrations
python manage.py migrate

### Start development server
python manage.py runserver

## API Endpoints
### User Registration (Sign Up)
URL: /api/register/
{
  "username": "your_username",
  "password": "your_password"
}

## User Login (Sign In)
### To log in, make a POST request to the following endpoint:
URL: /api/login/
Request Body (JSON):
{
  "username": "your_username",
  "password": "your_password"
}


## Access Protected Endpoints
### Once you are logged in, you can access protected endpoints using the JWT access token you received when you logged in
URL: /api/assignment/
Headers (for authenticated requests):
Authorization: Bearer .your_access_token.


## Refreshing the Access Token
### When your access token expires, you can get a new one using the refresh token.
URL: /api/token/refresh/
Request Body (JSON):
{
  "refresh": "your_refresh_token"
}
