# Vendor-management-system

This is a Develop a Vendor Management System using Django and Django REST Framework. This system will handle vendor profiles, track purchase orders, and calculate vendor performance metrics.

## Prerequisites
   Python (version 3.x recommended)
   
   Django
   
   Django REST Framework

## Setup Instructions

1) **Create Virtual Environment**
   ```bash
   pip install pipenv
   pipenv shell (Activate the virtual envirnoment)

2) **Install Dependencies**
   ```bash
   pipenv django
   pipenv djangorestframework

3) **Clone the Repository:**
   ```bash
   git clone https://github.com/RushabSG/Vendor-management-system.git

4) **Run Migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate

5) **Create Superuser (Optional):**
   ```bash
   python manage.py createsuperuser

6) **Run Development Server:**
   ```bash
   python manage.py runserver

7) **Access Admin Interface:**
   ```bash
   Visit http://127.0.0.1:8000/admin/ and log in with the superuser credentials.

## API Endpoints
   Include the Token in Authentication Section in Postman/Insomnia or can use the CURL command to test the API Endpoint \
   
   CURL -X GET http://127.0.0.1:8000/ "Authorization: Token (__add the generated Token for User__)

## Vendor Management:

1) **Create a new vendor:**
   ```bash
   POST /api/vendors

   This Endpoint is used to create a New vendor

2) **List all vendors:**
   ```bash
   GET /api/vendors

   The Endpoint fetches all records for the Vendor

3) **Display a specific vendor's details:**
   ```bash
   GET /api/vendors/{vendor_id}

   Endpoint to get Vendor specific details

4) **Update a vendor's details:**
   ```bash
   PUT /api/vendors/{vendor_id}
   
   Endpoint to Update Vendor specific details

5) **Delete a vendor:**
   ```bash
   DELETE /api/vendors/{vendor_id}

   Endpoint to delete Vendor details

## Purchase Order Tracking:

1) **Create a purchase order:**
   ```bash
   POST /api/purchase_orders

   Endpoint to create Purchase Order

2) **List all purchase orders:**
   ```bash
   GET /api/purchase_orders

    Endpoint to Display all Purchase Order

3) **Display details of a specific purchase order:**
   ```bash
   GET /api/purchase_orders/{po_id}

   Endpoint to get a Purchase Order by ID

4) **Update a purchase order:**
   ```bash
   PUT /api/purchase_orders/{po_id}

   Endpoint to update a Purchase Order by ID

5) **Delete a purchase order:**
   ```bash
   DELETE /api/purchase_orders/{po_id}

   Endpoint to delete a Purchase order by ID

## Vendor Performance Evaluation:

## Display a vendor's performance metrics:
   GET /api/vendors/{vendor_id}/performance

   Endpoint to get specific Vendors performance Metrics

## Authentication
   POST /api/api-token
   Generate User Token by providing Username and Password

## Update Acknowledge Endpoint
   ```bash
   POST /api/purchase_orders/{po_id}/acknowledge

   Endpoint to update the acknowledged date
