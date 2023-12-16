# Vendor-management-system

This is a Develop a Vendor Management System using Django and Django REST Framework. This system will handle vendor profiles, track purchase orders, and calculate vendor performance metrics.

## Setup Instructions

1) **Clone the Repository:**
   ```bash
   git clone https://github.com/RushabSG/Vendor-management-system.git
   
2) **Setup the development environment:**
   ```bash
   pip install pipenv
   pipenv install 

3) **Activate the Virtual environment:**
   ```bash
   pipenv shell

4) **Install Dependencies:**
   ```bash
   pipenv install --dev

5) **Run Migrations:**
   ```bash
   python manage.py migrate

6) **Create Superuser (Optional):**
   ```bash
   python manage.py createsuperuser

7) **Run Development Server:**
   ```bash
   python manage.py runserver

**Access Admin Interface:**
   ```bash
   Visit http://127.0.0.1:8000/admin/ and log in with the superuser credentials.
