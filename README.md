# Vendor-management-system

This is a Develop a Vendor Management System using Django and Django REST Framework. This system will handle vendor profiles, track purchase orders, and calculate vendor performance metrics.

## Setup Instructions

**Clone the Repository:**
   ```bash
   git clone https://github.com/RushabSG/Vendor-management-system.git
   
**Setup the development environment:**
   ```bash
   pip install pipenv
   pipenv install 

**Activate the Virtual environment:**
   ```bash
   pipenv shell

**Install Dependencies:**
   ```bash
   pipenv install --dev

**Run Migrations:**
   ```bash
   python manage.py migrate

**Create Superuser (Optional):**
   ```bash
   python manage.py createsuperuser

**Run Development Server:**
   ```bash
   python manage.py runserver

**Access Admin Interface:**
   ```bash
   Visit http://127.0.0.1:8000/admin/ and log in with the superuser credentials.