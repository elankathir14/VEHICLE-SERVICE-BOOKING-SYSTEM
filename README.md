Vehicle Service Booking System

# Problem Statement

Many vehicle service centers still manage customer bookings manually using registers or phone calls. This can result in booking errors, scheduling conflicts, delayed services, and poor customer experience. A Vehicle Service Booking System helps automate service appointments, manage vehicle records, and improve service center efficiency.

# Project Objectives

- Allow customers to book vehicle service appointments online.
- Manage vehicle service schedules efficiently.
- Track service status in real time.
- Maintain customer and vehicle records.
- Reduce manual booking errors.
- Improve service center productivity and customer satisfaction.

# Technologies Used

## Front End

- HTML
- CSS
- JavaScript

## Back End

- Python (Flask/Django)

## Database

- MySQL

# Modules

- User Management
- Customer Management
- Vehicle Management
- Service Booking Management
- Service Status Tracking
- Payment Management
- Notification Management
- Report Generation

# Database Tables

## User

| Field Name | Data Type |
|------------|-----------|
| user_id | INT |
| username | VARCHAR |
| password | VARCHAR |
| role | VARCHAR |

## Customer

| Field Name | Data Type |
|------------|-----------|
| customer_id | INT |
| customer_name | VARCHAR |
| contact_number | VARCHAR |
| address | VARCHAR |

## Vehicle

| Field Name | Data Type |
|------------|-----------|
| vehicle_id | INT |
| customer_id | INT |
| vehicle_number | VARCHAR |
| vehicle_model | VARCHAR |
| vehicle_type | VARCHAR |

## Service Booking

| Field Name | Data Type |
|------------|-----------|
| booking_id | INT |
| customer_id | INT |
| vehicle_id | INT |
| service_type | VARCHAR |
| booking_date | DATE |
| status | VARCHAR |

## Payment

| Field Name | Data Type |
|------------|-----------|
| payment_id | INT |
| booking_id | INT |
| amount | DECIMAL |
| payment_date | DATE |

# Expected Outcome

The system will provide an efficient platform for customers to schedule vehicle services, track service progress, manage vehicle records, and improve overall service center operations.

# Conclusion

The Vehicle Service Booking System enhances service booking accuracy, reduces manual work, improves customer satisfaction, and provides an effective solution for managing vehicle service operations.
