## Reason

This is a ongoing project to develop my Python and SQL coding skills in one big project. Feel free to download an adjust the script for personal use.  
This here will be a holostic BudgetBook solution for privat money management.  
for any questions on this feel free to contact me via LinkedIn.  

## current status

update 22.08.2024  
 - created Classes Procedure() and DBConnection() in BudgetBook.py
 - reorganized procedures in BudgetBook.py 
 - reorganized commentary for better understanding

update 16.08.2024  
 - BudgetBook.py starts the userInterface  
 - It checks a connection to the MySQL Server is possible.  
 - If connection possible: it  checks for database and tables. if not existing, it creates whatever is missing.  
 - Server connection can be managed in Settings. "Save" will start the checking und creation process.   


## User Interface

The UI is created in Pyside6-Designer.  
To make it easier to adjust, i kept the ui_main.ui in this repository.  

## Licence

The idea of the licence is that anyone can use this code and further develop for privat use.  
Limitations apply to Liability, Warranty, etc.  
see Licence for detailed information  

## Requirements  

### Python version

This was scripted in Python 3.12.2  

### MySQL version

This was scripted in MySQL 8.0.32  

### Libraries

PySide6.QtWidgets  
json  
mysql.connector  
