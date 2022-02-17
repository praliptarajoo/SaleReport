# SaleReport
Display data for a sale structure

# Problem statement 
Create a one page Django application that helps to summarize the sales data of a company. Check sample CSV below & create Django models to store the data in a normalized form. Load all data of sample CSV into a MySQL DB using Django ORM. 

# User can generate report 
1- List of all orders - Order ID, Order Date, Country(Region), Item Type, Sales Channel, Delivery Date, Delivery Time (Delivery Date - Order Date), Units Sold, Unit Price, Unit Cost, Total Profit ((Unit Price - Unit Cost) * Units Sold) → This should be paginated
2- Top 10 Sales Countries (Order By Total Revenue)
3- Top 3 Sales Regions (Order By Total Revenue)
4- Top 5 Selling Items(Order By Units Sold)
5- Online vs Offline Sales
6-Year_Profit listing (Order By Total Profit in the whole year)

# installing
# Clone the project 
https://github.com/praliptarajoo/SaleReport.git/tree/master
cd SaleReportApp

# Install dependencies & activate virtualenv
Set up a virtual environment - python -m venv env
Activate the virtual environment - source env/bin/activate

# Apply migrations
python source/manage.py migrate

# Collect static files
python source/manage.py collectstatic

# Running 
# A development server 
Just run this command:
python source/manage.py runserver
