# SocioCollabs

## How to run this project:

### Step # 1 -clone this repo
$ git clone https://github.com/Ganiti/SocioCollabs.git.   
  cd SocioCollabs

### Step # 2 - Create a virtual environment

 ***Virtualenv modules installation (Unix based systems)***  
$ virtualenv env.   
  source env/bin/activate. 

 ***Virtualenv modules installation (Windows based systems).***   
$  virtualenv env. 
 .\env\Scripts\activate. 

### Step # 3 - Install dependencies. 

 ***Install requirements.*** 
$ pip3 install -r requirements.txt. 

### Step # 4 - Set Up Environment. 

 ***Set the FLASK_APP environment variable.***.  
$ (Unix/Mac) export FLASK_APP=run.py.  
  (Windows) set FLASK_APP=run.py.   
  (Powershell) $env:FLASK_APP = ".\run.py".   

### Step # 5 - Create Tables (SQLite persistance).  

 ***Create tables.*** 
$ flask shell.  
$ >>> from app import db.  
$ >>> db.create_all().  

### Step #6 - (optional) Enable DEBUG Environment (local development). 

 ***Set up the DEBUG environment.***.  
$  (Unix/Mac) export FLASK_ENV=development.   
$  (Windows) set FLASK_ENV=development.   
$  (Powershell) $env:FLASK_ENV = "development".   

### Step #7 - Start the project. 

 ***Run the application.*** 
$ # --host=0.0.0.0 - expose the app on all network interfaces (default 127.0.0.1).
$ --port=5000    - specify the app port (default 5000).  
$ flask run --host=0.0.0.0 --port=5000.   

$ # Access the app in browser: http://127.0.0.1:5000/. 
