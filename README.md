Vendor Management System:

The Vendor Management System is a Django-based web application designed to handle vendor profiles, track purchase orders, and 
calculate vendor performance metrics.

Setup Instructions

1) Clone the Repository:
	
	git clone https://github.com/aswinambalir8/vendor.git

2)Navigate to the Project Directory:

	cd Vendor/vmsproject

3)Install Dependencies:

	pip install -r requirements.txt

4)Apply Database Migrations:

	python manage.py migrate

5)Run the Development Server:

	python manage.py runserver

6)Access the Application:

	Open your web browser and go to http://localhost:8000 to view the Vendor Management System.


Usage

Admin Interface:

1) Access the Django admin interface at http://localhost:8000/admin.

2) Log in with your admin credentials.

3) Manage vendor profiles and purchase orders.

4) Add,Edit,Update,Delete Vendor and purchase order data through admin interface.

if required
*admin credentials:

username : vendor
password : 1234


API Endpoints

-> Vendor List API: http://localhost:8000/

-> Vendor Detail API: http://localhost:8000/vendors/{vendor_id}/

-> Purchase Order List/Create API: http://localhost:8000/purchase_orders/

-> Purchase Order Detail API: http://localhost:8000/purchase_orders/{po_id}/

-> vendor performance metrics API: http://localhost:8000/vendors/{vendor_id}/performance

## To Add a New vendor (through frontend)
 
-> Vendor List API: http://localhost:8000/

-> Go To Content:
	(use JSON format)
   eg:
	[ {
        "id": numeric value,
        "name": "username",
        "contact_details": "fill",
        "address": "fill",
        "vendor_code": "code",
        "on_time_delivery_rate": 0.0,
        "quality_rating_avg": 0.0,
        "average_response_time": 0.0,
        "fulfillment_rate": 0.0
    }]

-> POST

## To Retrieve Vendor Details

-> Vendor Detail API: http://localhost:8000/vendors/{vendor_id}/

## Update Vendor Data

-> Vendor Detail API: http://localhost:8000/vendors/{vendor_id}/

-> Go To Content:
	(use JSON format)
   eg:
	[ {
        "id": {vendor_id},
        "name": "update",
        "contact_details": "update",
        "address": "update",
        "vendor_code": "update",
        "on_time_delivery_rate": 0.0,
        "quality_rating_avg": 0.0,
        "average_response_time": 0.0,
        "fulfillment_rate": 0.0
    }]

-> POST

## Delete Vendor

-> Vendor Detail API: http://localhost:8000/vendors/{vendor_id}/
-> DELETE


## To Add a Purchase order (through frontend)
 
-> Purchase Order List/Create API: http://localhost:8000/purchase_orders/

-> Go To Content:
	(use JSON format)
   eg:
	 [{
        "id": numeric value,
        "po_number": "fill",
        "order_date": "date",
        "delivery_date": "date",
        "quantity": numeric,
        "status": "fill",
        "quality_rating": 0.0,
        "issue_date": "date",
        "acknowledgment_date": "date",
        "vendor": {vendor_id}
    }]

-> POST

## To Retrieve Purchase order Details

-> Purchase Order Detail API: http://localhost:8000/purchase_orders/{po_id}/

## Update Purchase order 

-> Purchase Order Detail API: http://localhost:8000/purchase_orders/{po_id}/

-> Go To Content:
	(use JSON format)
   eg:
	[{
        "id": {po_id},
        "po_number": "update",
        "order_date": "update",
        "delivery_date": "update",
        "quantity": update,
        "status": "update",
        "quality_rating": 0.0,
        "issue_date": "update",
        "acknowledgment_date": "update",
        "vendor": {vendor_id}
     }]

-> POST

## Delete Purchase order

-> Purchase Order Detail API: http://localhost:8000/purchase_orders/{po_id}/
-> DELETE


##To Get Performance Of Each Vendor

-> vendor performance metrics API: http://localhost:8000/vendors/{vendor_id}/performance

Testing

The project includes a test suite to ensure the functionality and reliability of the API endpoints.

1) Run the tests with the following command:

   python manage.py test

                                                                                    **END**
