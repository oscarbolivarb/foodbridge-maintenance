# FoodBridge User Guide

Reviewed November 14, 2026 
Based on application commit 432ea27

Step 2 User Facing Documentation 

This version has no request form, buttons or scheduling screens. Here, an operator runs a program and the administrator should update the records. The staff should ask the administrator to make changes.
Submit or correct a request
1)	Give the administrator the family name, zip code, household size, contact information and any baby or hygiene supplies needed.
2)	Ask the administrator to add the request with its own ID and status of new. 
3)	Confirm the information before the program runs. For corrections provide the existing request ID to avoid creating a duplicate.

Review delivery assignments
1)	Ask the operator to back up the records and run the program.
2)	Review the updated request. A scheduled request should show the driver’s name and the delivery time from 9:00 am to 1:00 pm
3)	Confirm the assignment with the driver. The messages displayed during the run are previews. The program does not send real emails or texts.

Handle waiting request: the pending_inventory means that the supplies are missing, pending_driver means that there are no suitable drivers available and the invalid means that the household size needs to be checked. 
The administrator should receive the request ID and understand the problem. Waiting requests are not checked again automatically and each request should be reviewed before another attempt because resetting all the requests could repeat the deliveries and remove the supplies twice.

Create and read the report 
1)	Ask the operator to run the program. 
2)	Open the data/daily_report.txt in the text editor.
3)	Check the request totals, scheduled deliveries, waiting and invalid requests, remaining supplies and volunteer count.
