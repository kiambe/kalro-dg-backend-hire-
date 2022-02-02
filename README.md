# Digital Green - KALRO

## Backend Project

Hi! Here below goes the project. All the best!

To start off, evaluation will be on below criteria:
●	Designing a well thought out modular architecture
●	Writing a clean, well-commented, error-handled code
●	Consistency using Git commits
●	Correctness around edge-cases
●	Performance and integrity from a scalability perspective

## Final Deliverable:
Please create a private repository on Github and add username dg-backend-hire as a contributor. Please don't create a public repo, as that would make your solution public for others to see.
Problem Statement
To implement a small ecommerce web application backend with the below features. Features have been grouped by 3 different user types (roles) - admin, customer and sales-agent.

### Admin:
1.	Login using username and password.
2.	Create users for roles (customer, sales-agent)
3.	Create new products and update existing products. 
a.	Update product info
b.	Update current price
c.	Update current stock level
d.	Update product status - currently eligible for selling

* See Notes below for details of the product entity.

### Customer:
1.	Login using mobile number and an OTP (mocking OTP will be sufficient)
2.	View products for sale
3.	Place an order for multiple products:
a.	While placing a new order, the customer's last purchase price for every product that has been purchased in the past should be shown along with the current price.
b.	Only products which are “In stock” should be allowed to order.
4.	View past orders

### Sales Agent:
1.	Login using username and password.
2.	View orders for all customers
3.	Process an Order:
a.	Update order status [“Accepted”, “Delivered”, “Cancelled”]
b.	On order accept:
i.	An invoice* is created 
ii.	Customer's financial ledger* is updated. 
iii.	An SMS is sent to the customer (Hint: Make it asynchronous.)
c.	On marking a previously “Confirmed” order as “Cancelled”, reverse financial ledger entries are created. An order can be cancelled until “Delivered”.
4.	Record cash payments from the customer (only cash payments are supported, so only agent creates them)
5.	View financial ledger of a customer (bonus - time period based filters)

* See Notes below for details of invoice and ledger.

### Notes:
●	Product
Fields - name, description, price, stock, etc. 

A product can have multiple variants which could differ in attributes like size, colour, texture etc.

Example - 
Red 15-inch V140 laptop
Blue 13-inch V140 laptop
are two product variants where
Red and Blue are values of color attribute
15-inch and 13-inch are values of size attribute
V140 is the product

### Invoice
Fields - customer, status, time, products (Quantity, Price, Subtotal), total amount, sales agent etc.

### Financial ledger:
○	Customer, Transaction date, Amount, Post Transaction balance. 
○	John Doe, 21 May 2021, - $. 100, $. 400
○	Jane G, 20 May 2021, + $. 500, $. 500
●	Don’t need to send actual SMSs. Mocking is sufficient.
●	Use appropriate design patterns (Decorator, Singleton, etc.)




