<img src="https://media.licdn.com/dms/image/D4E12AQF9yzpGOro1AA/article-cover_image-shrink_720_1280/0/1662417464111?e=2147483647&v=beta&t=ObCOfTGhLzI4QUFDg1mlZlMtL65kq3lX7OPNrN5saZE" alt="flixfix">

# Vendor Management

## UML
> Intended UML

<h1 align="center">
  <br>
  <img src="https://i.imgur.com/flsLO8x.png" alt="uml" height="600">
  <br>
</h1>

## Roadmap

* [X] All Views protected by login except user creation(test login in api/docs)
* [ ] All tests for every model

* [X] REQ-01 Bank CRUD
    * [X] Bank name 50 char.

* [X] REQ-02 Vendor and Bank
    * [X] Vendor Name
    * [X] Vendor NIT with regex
    * [X] Contact Name (Optional) - CONFLICT: required fields will prevent for fields to be empty
    * [X] Contact Phone Number
    * [X] Bank Name
    * [X] Bank Number
    * [X] Check missing fields
    * [X] Appropiate response for SUCCESS
    * [ ] Combobox

* [ ] REQ-03 Views for Vendor and Accounts
    * [X] GET models by id and CRUD
    * [ ] Actual HTML views

* [ ] REQ-04 Dashboard
    * [X] Registry counter (works with every model GET /api/<model>/) (not in dashboard yet)
    * [ ] Logic in views
    * [ ] Edit and Delete buttons (logic implemented)
    * [ ] Empty index "No info in table"
    * [X] Paginate in blocks of 10 (backend)
    * [X] Same validation in edit as in create
    * [ ] Parciales (I need to investigate)

* [X] REQ-05 Login System
    * [X] Auth and Permissions
    * [X] Successful login message with token response
    * [X] Check if email exists
    * [X] Unsuccesful login check
    * [X] Custom Auth lib and Perms

* [X] Entire Backend API created


## How to use

* Clone the repository and install dependencies
* Install and create python venv in the root folder of the project
* Activate venv
* Install dependencies from requirements.txt
* Create and run migrations
* Run Server

```bash
katapult-commerce$git clone https://github.com/andylopezr/katapult-commerce.git
katapult-commerce$python3 -m pip install --user virtualenv
katapult-commerce$python3 -m venv env
katapult-commerce$source env/bin/activate
(env) katapult-commerce$pip install -r requirements.txt
(env) katapult-commerce$python3 manage.py makemigrations
(env) katapult-commerce$python3 manage.py migrate
(env) katapult-commerce$python3 manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
February 04, 2023 - 06:12:47
Django version 4.1.5, using settings 'vendormanager.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

* If it is running successfully, visit the following website to test the API endpoints.
```
http://127.0.0.1:8000/api/docs
```

## Built with

* Python 3.10.6
* Django 4.1.5
* Django Ninja 0.20.0
* sqlite3
