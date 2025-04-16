# DevBlog API

## Overview
DevBlog API is a Django-based RESTful API for managing blog posts, user authentication, and more.

## Table of Contents
- [Installation](#installation)
- [Running the Application](#running-the-application)
- [API Endpoints](#api-endpoints)
- [Testing](#testing)
- [License](#license)

## Installation

Follow these steps to set up the project locally:

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Mouhamed-B/devblog-api.git
   cd devblog-api
   ```

2. **Create a Virtual Environment**
   It is recommended to use a virtual environment to manage dependencies.
   ```bash
   python -m venv .venv
   ```

3. **Activate the Virtual Environment**
   - On Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```

4. **Install Dependencies**
   Install the required packages using pip:
   ```bash
   pip install -r requirements.txt
   ```

5. **Set Up Environment Variables**
   Create a `.env` file in the root directory and add the necessary environment variables. You can use `.env.example` as a reference.

6. **Run Migrations**
   Apply the database migrations:
   ```bash
   python manage.py migrate
   ```

7. **Create a Superuser (Optional)**
   If you want to access the Django admin panel, create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

## Running the Application

To start the development server, run:
```bash
python manage.py runserver
```
The application will be available at `http://127.0.0.1:8000/`.

## API Endpoints

Swagger UI for the API documentation available at `http://127.0.0.1:8000/api/schema/swagger-ui/`

- **User Registration**: `POST /api/register/`
- **User Login**: `POST /api/login/`
- **Create Post**: `POST /api/posts/`
- **Update Post**: `PUT /api/posts/{id}/`
- **Retrieve Post**: `GET /api/posts/{id}/`

Refer to the API documentation for more details on request and response formats.

## Testing

To run the tests, use the following command:
```bash
python manage.py test
```

## Demo

https://devblog-api.vercel.app/

https://devblog-api.vercel.app/api/schema/swagger-ui/

## How it Works


We allow "\*.vercel.app" subdomains in `ALLOWED_HOSTS`, in addition to 127.0.0.1:

```python
# api/settings.py
ALLOWED_HOSTS = ['127.0.0.1', '.vercel.app']
```

The `wsgi` module must use a public variable named `app` to expose the WSGI application:

```python
# api/wsgi.py
app = get_wsgi_application()
```

The corresponding `WSGI_APPLICATION` setting is configured to use the `app` variable from the `api.wsgi` module:

```python
# api/settings.py
WSGI_APPLICATION = 'api.wsgi.app'
```
