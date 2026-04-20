# User Login System

Secure user authentication system with login attempt limiting and password reset via email, built with Python and FastAPI.

## About

This project was built to practice and deepen knowledge of backend development, focusing on security patterns used in real production systems. It includes account blocking after failed attempts, secure password hashing and email-based password reset with expiring tokens.

## Features

- User registration with encrypted password (bcrypt)
- Login with JWT authentication
- Account blocking after 3 failed login attempts
- Password reset via email with expiring token (30 minutes)
- Modular architecture with FastAPI routers

## Tech Stack

- **Python 3.12** — OOP, modular architecture
- **FastAPI** — REST API framework
- **Uvicorn** — ASGI server
- **SQLite3** — relational database
- **bcrypt** — password hashing
- **JWT (python-jose)** — authentication tokens
- **smtplib** — email sending
- **python-dotenv** — environment variables management

## Project Structure