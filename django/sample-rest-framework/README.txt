// create project directory

// create virtual envirnonment
    python -m venv venv

// activate virtual environment
    source venv/bin/activate

// make a workspace

// create a requirements file
    pip freeze > requirements.txt

//Add dependencies
    django
    djangorestframework
    pyyaml
    requests
    django-cors-headers

// install dependencies
    pip install -r requirements.txt

// create a backend folder for django application
    django-admin startproject core .

// create a python folder for api client


