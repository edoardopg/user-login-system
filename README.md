# User Login System

Secure user authentication system with login attempt limiting and password reset via email, built with Python and FastAPI.

## About

This project was built to practice and deepen knowledge of backend development, focusing on security patterns used in real production systems. It includes account blocking after failed attempts, secure password hashing and email-based password reset with expiring tokens.

## Features

- User registration with encrypted password (bcrypt)
- Login with JWT authentication and OAuth2 standard
- Account blocking after 3 failed login attempts
- Password reset via email with expiring token (30 minutes)
- Account deletion with JWT protection
- Modular architecture with FastAPI routers
- Environment variables for sensitive credentials (.env)
- Web frontend (HTML/CSS/JS)

## Tech Stack

- **Python 3.12** — OOP, modular architecture
- **FastAPI** — REST API framework
- **Uvicorn** — ASGI server
- **SQLite3** — relational database
- **bcrypt** — password hashing
- **JWT (python-jose)** — authentication tokens
- **OAuth2PasswordRequestForm** — standard OAuth2 login
- **smtplib** — email sending
- **python-dotenv** — environment variables management

## Project Structure
user-login-system/
│
├── database.py          # Database connection
├── models.py            # Table creation and initial data
├── main.py              # Entry point
├── api.py               # FastAPI app and router registration
│
├── crud/
│   ├── init.py
│   └── users.py         # User CRUD class
│
├── routers/
│   ├── init.py
│   └── users.py         # API endpoints
│
├── utils/
│   ├── init.py
│   ├── security.py      # Password hashing and token generation
│   └── email.py         # Email sending
│
└── frontend/
├── login.html
├── register.html
├── forgot-password.html
├── reset-password.html
└── dashboard.html
## Requirements

- Python 3.8 or higher
- Install dependencies:

```bash
pip install fastapi uvicorn python-jose bcrypt python-dotenv python-multipart
```

## Environment Variables

Create a `.env` file in the root of the project:
EMAIL=youremail@gmail.com
EMAIL_PASSWORD=your_app_password
FRONTEND_URL=http://127.0.0.1:5500/frontend
## How to Run

Clone the repository and initialize the database:

```bash
git clone https://github.com/edoardopg/user-login-system.git
cd user-login-system
python main.py
```

Start the API server:

```bash
uvicorn api:app --reload
```

Open `frontend/login.html` with Live Server and use the following test credentials:
- **Username:** admin
- **Password:** admin123

Or explore the API directly at `http://localhost:8000/docs`.

## Roadmap

- [x] User registration
- [x] Login with JWT and OAuth2
- [x] Account blocking after 3 failed attempts
- [x] Password reset via email
- [x] Account deletion
- [x] Frontend (HTML/CSS/JS)
- [ ] Deploy to Railway/Render

## Author

Edoardo — Biomedical Engineer transitioning to Software Development.  
[GitHub](https://github.com/edoardopg)