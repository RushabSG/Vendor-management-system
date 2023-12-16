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
   python manage.py makemigrations
   python manage.py migrate

6) **Create Superuser (Optional):**
   ```bash
   python manage.py createsuperuser

7) **Run Development Server:**
   ```bash
   python manage.py runserver

8) **Access Admin Interface:**
   ```bash
   Visit http://127.0.0.1:8000/admin/ and log in with the superuser credentials.

## API Endpoints

## Vendor Management:
   
1) **Create a new vendor:**
   ```bash
   POST /api/vendors

2) **List all vendors:**
   ```bash
   GET /api/vendors

3) **Display a specific vendor's details:**
   ```bash
   GET /api/vendors/{vendor_id}

4) **Update a vendor's details:**
   ```bash
   PUT /api/vendors/{vendor_id}

5) **Delete a vendor:**
   ```bash
   DELETE /api/vendors/{vendor_id}

## Purchase Order Tracking:

1) **Create a purchase order:**
   ```bash
   POST /api/purchase_orders

2) **List all purchase orders:**
   ```bash
   GET /api/purchase_orders

3) **Display details of a specific purchase order:**
   ```bash
   GET /api/purchase_orders/{po_id}

4) **Update a purchase order:**
   ```bash
   PUT /api/purchase_orders/{po_id}

5) **Delete a purchase order:**
   ```bash
   DELETE /api/purchase_orders/{po_id}

## Vendor Performance Evaluation:

## Display a vendor's performance metrics:
   ```bash
   GET /api/vendors/{vendor_id}/performance
