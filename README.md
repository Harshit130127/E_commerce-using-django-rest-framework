# Django E-Commerce Website

This project is a fully functional **Django-based E-commerce website** where users can browse products, add them to the cart, and proceed to checkout. The project demonstrates the complete workflow of an online shopping system, including product management, cart functionality, and order processing. The goal was to create a real-world application that simulates an online store with all essential features.

---

## Problem Statement

To develop a web application that allows users to:

- Browse a catalog of products with images and descriptions  
- Search for specific products using a search bar  
- View detailed information about individual products  
- Add products to a shopping cart and maintain cart state across sessions using **local storage**  
- Manage and update cart items (increase/decrease quantity, remove items)  
- View the number of items in the cart dynamically on the navbar  
- Checkout and place orders with user details  
- Calculate and store order totals in the database for record-keeping  

---

## Features

- Product listing with images and descriptions  
- Product search by name or category  
- Pagination for large product catalogs  
- Product detail page  
- Add to cart with local storage support  
- Cart popover displaying selected items and quantity  
- Dynamic update of cart item count  
- Checkout form and order placement  
- Order total calculation and storage  
- Responsive design for mobile and desktop  

---

## Steps Performed

### 1. Project Setup
- Initialized a Django project and created a virtual environment  
- Installed required dependencies using `requirements.txt`  
- Configured the SQLite database and applied migrations  
- Set up static and template directories  

### 2. Creating Models
- Defined `Product` and `Order` models in `models.py`  
- Fields included: name, description, price, category, image, and order details  

### 3. Adding Products
- Added sample products via Django admin panel  
- Verified proper data storage and frontend display  

### 4. Building Views
- Index view to display all products  
- Product detail view for individual product information  
- Cart view to manage cart items  
- Checkout view for order placement  

### 5. Frontend Development
- Designed HTML templates for index, product details, cart, and checkout pages  
- Applied CSS styling and Bootstrap 5 for a modern look  
- JavaScript for dynamic cart updates and popovers  

### 6. Search and Pagination
- Implemented search functionality to filter products  
- Added pagination for better user experience with large datasets  

### 7. Cart Functionality
- Add, remove, and update cart items using local storage  
- Cart popover in navbar showing selected items  
- Dynamic update of cart item count  

### 8. Checkout Process
- Checkout page with form for user details  
- Dynamic calculation of order totals  
- Orders stored in database for record-keeping  

### 9. Testing and Debugging
- Verified product display, search, cart operations, and checkout  
- Fixed bugs in price calculation and cart storage  
- Tested responsiveness on multiple devices  

---

## Project Structure

- **models.py** – Defines `Product` and `Order` models  
- **views.py** – Handles all page views and logic  
- **urls.py** – URL routing for all views  
- **templates/** – HTML templates  
- **static/** – CSS, JS, and image files  
- **cart.js** – Handles local storage and dynamic cart updates  

---

## Technologies Used

- Python 3.x  
- Django 4.x  
- HTML, CSS, JavaScript  
- Bootstrap 5  
- SQLite / PostgreSQL  
- Local storage for frontend cart persistence  

---

## Usage

- Browse products on the homepage  
- Search or filter products  
- Click on a product to view details  
- Add products to cart and view them in the navbar popover  
- Update quantities or remove items  
- Proceed to checkout and submit order  

---

## Key Learnings

- End-to-end Django web application development  
- Integration of backend and frontend functionalities  
- Handling dynamic cart functionality with local storage  
- Implementing search, pagination, and product details  
- Form handling and database storage of orders  
- Debugging and responsive web design  

---

## Future Improvements

- Add user authentication for personalized carts and order history  
- Implement payment gateway integration  
- Add product categories and filters  
- Enhance UI/UX with advanced CSS and animations  
- Add email notifications for order confirmation
