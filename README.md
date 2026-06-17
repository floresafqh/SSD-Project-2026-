# SSD-Project-2026-
# Secure Inventory Management System
# Name: SITI NURDAMIA AFIQAH BINTI AZREE & ELIS KARISHA BINTI KAMARUL HISAM

## 1. Project Description
This repository hosts a hardened, lightweight Inventory Management System built using the Python Django Framework. It demonstrates proactive implementation of security controls directly into the backend architecture to neutralize common vulnerabilities like SQL Injection (SQLi), Cross Site Scripting (XSS) and unauthorized data tampering.

## 2. Security Features Summary
* **SQLi Protection:** Full implementation of the Django ORM for parameterized queries.
* **XSS Defense:** Context aware automatic HTML entity encoding on all view templates.
* **Hardened Authentication:** Enforced complexity matrices through `AUTH_PASSWORD_VALIDATORS`.
* **Session Safeguards:** Non-predictable session tokens paired with `HttpOnly` cookie structures.
* **Immutable Security Audit Log:** Operational monitoring hooks overridden inside `admin.py` to prevent data deletions, making security logs strictly read only.
* **Secret Isolation:** Separation of runtime parameters and secret keys utilizing isolated `.env` environments.

## 3. Dependencies
The application dependencies are strictly locked within `requirements.txt`:
* `Django>=4.2.0,<5.0.0`
* `python-dotenv>=1.0.0`

## 4. Installation Steps & How to Run the App
Follow these steps to deploy and execute the platform locally:

# Clone the repository
$git clone https://github.com/floresafqh/SSD-Project-2026-.git$ cd "SSD-Project-2026-"

# Create and activate an isolated virtual environment
$python -m venv .venv$ source .venv/bin/activate  # On Windows use: .venv\Scripts\activate

# Install locked project dependencies
$ pip install -r requirements.txt

# Configure environmental variables
# Copy .env.example to .env and configure your local SECRET_KEY and DEBUG=True/False flags
$ cp .env.example .env

# Execute local database migrations
$ python manage.py migrate

# Create your high-privilege administrative superuser account
$ python manage.py createsuperuser

# Boot up the local secure development web server
$ python manage.py runserver
