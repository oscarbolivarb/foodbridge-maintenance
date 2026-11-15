# FoodBridge Coding Standards

Reviewed November 14, 2026
Based on application commit 432ea27

Step 3 Coding Standards
Names and formatting: lower case words should be used with underscores for variables, methods and files such as assigned_today. Capitalized words should be used for classes, such as InventoryService and the uppercase names for constants. This will keep the names consistent with the existing code.
There should be four spaces for indentation, never tabs and spaces around operators. Each line should be under 79 characters and when a call uses several lines, there should be closing brackets on a separate line. These rules will help prevent any format errors, like the one encountered in the previous assignment, milestone 2.
Comments and method size: short comments should be used to explain the decisions that are not obvious and a description should be added to the public method. This explains what the method does, what information it needs, what it returns, which file it changes and any possible errors.
Each method should be kept under 40 lines and longer methods should be reviewed to see if the task can be separated. By keeping loading records, assigning drivers and creating the report separately, it will help the daily process to be easy to follow. 
Updates and documentation: updating the instructions, data descriptions, known problems and test commands in the same branch as the code changes. TODO notes should explain the problem, include an issue number and describe the needed fix. Review changes and run relevant checks before they are merged, so that the guides match the code. 
File organization in shared rules: by keeping the main workflow in app.py, service tasks in services, shared validation and utils and guide in docs, it will prevent repeated code and inconsistent calculation. Both inventory methods should be used in the _required_food_boxes(), so they can check and remove the same number of boxes.  
