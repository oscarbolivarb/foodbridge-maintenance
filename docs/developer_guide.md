# FoodBridge Developer Guide

Reviewed November 14, 2026 
Based on application commit 432ea27

FoodBridge helps a non-profit organize food deliveries, assign volunteer drivers, track supplies, and create reports. This milestone is completed individually by Oscar Bolivar including and handled the developer documentation, user instructions, coding standards and the report presentation. The guide describes the main branch at commit 432ea27.
Structure and responsibilities: The program starts in app.py, its run_daily_process() method loads records, checks requests, finds drivers, reserves supplies, saves changes and creates a report. This application stores its records in JSON files and it does not have a web interface or working database connection.  

The services folder separates the main tasks:
•	request_service.py loads and saves the requests, its mark_scheduled() method adds to the assigned driver and the delivery time.
•	inventory_service.py it checks available supplies and removes the items when a delivery is scheduled 
•	volunteer_service.py find an active driver who covers the requested zip code and has fewer than three assignments.
•	notification_service.py prints the message and the alerts. 
•	reporting_service.py creates the summary report. 
•	legacy_admin.py Contains the tools for resetting the request and printing the records. These tools are separate from the daily process.

The data folder contains requests.json, inventory.json, and the volunteers.json. The utils folder contains the helper functions and the validate_request(), but the daily process does not use the validator. 
The README introduces the project and the docs/architecture_notes.txt provides the basic system notes. A developer should start with the app.py and then review the service related to what is planned to change.
Set up and data requirements: install Python 3 and Git, then clone the repository and open a terminal in the main project folder. There are not any extra Python packages needed. Run py app.py on Windows or python app.py where that command uses Python 3. Then run it from the project folder so that the program can find the data files. 
The application needs permission to read and update the JSON file and creates the data/daily_report.txt. The records need to be backed up first because running the program changes the request and inventory. 
The requests needs an ID, family name, zip code, positive household size, contact information, supply needs and status. The zip code should be stored as text and the fields needs_baby_items as well as needs_hygiene use true or false. 
The inventory records store the supply counts and the volunteer records include a name, role, active status, covered zip codes and the assignments count. Keep JSON format valid and use consistent data types.
The config.py file controls the report location, sender address, alert address and the SMS settings. Its database and mail settings do not provide working connections.

Rules and Milestone 2 Changes

The Households with one to three people will receive one food box, those with four to six will receive two boxes and those with 7 or more people will receive three boxes. Each requested baby or hygiene kit uses one item.
The commit 436c5cc from the refactor/shared-box-rule, moved the box calculation into the _required_food_boxes() and both inventory methods now use the same shared rule. The commit 69e9448 from the refactor/daily-process, replaced the nested conditions with earlier checks. The supplies are reserved only after a driver is found and the delivery time remains from 9:00 am to 1:00 pm
Known problem: only requests marked new are processed, the waiting requests are skipped on later runs and the driver assignment counts are not being saved by the app.py. The full request validation is not connected and the automated tests have not been saved. 
An interrupted run could leave the JSON files with inconsistent information, so only one operator should run the program at a time. Any hardcoded passwords and tools that print private client records should also need attention before a real use. 

