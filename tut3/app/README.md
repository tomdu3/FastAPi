# Enhancing the FastAPI Server

## Learning Outcomes
Upon completing your learning, you will be able to:

- Create a fully functional API server
- Integrate SQLAlchemy with your API
- Use Postman to test your API

## Quest Details
### Introduction
Previously, you learnt how to create routes or endpoints in FastAPI for users to create, read, update and delete data on your server.

You will now learn how to integrate a database into the application using SQLAlchemy with FastAPI, allowing users to interact with the database through the API server. This means that the create, read, update, and delete operations in your server can now be directly linked to a database, storing or retrieving data as needed. SQLAlchemy's Object-Relational Mapping (ORM) feature is particularly useful; it lets you define your database models as Python classes, making it more intuitive to work with data.

## Quest Steps
Total Steps: 11


### Step 1: Application Brief
We will be developing a web application using FastAPI and SQLalchemy. The application will be integrated with an SQLite database to provide dynamic content that users can read and modify. In our case, it is an item list that can be used for an e-commerce website or to-do list application.

Previously, we used a dictionary for our application and carried out CRUD operations on it, making it volatile as it resets every time the application is run. Here, we will be developing a fully functional API server that can be scalable when connected to a database such as MySQL. However, we will use an SQLite database for simplicity.

SQLite databases are stored as single files on disk, which makes them highly portable and manageable. They are widely used in various applications, especially for applications that do not require large-scale data processing. It provides a simple and efficient way to store and retrieve structured data, making it a popular choice for many developers.

Before we start, read [this article](https://www.sqlalchemy.org/features.html) to understand what SQLAlchemy is and how it can be used to make database operations more seamless.

In short, SQLAlchemy is a powerful Python library that facilitates interaction with databases by abstracting database management complexities. It enables users to create, manage, and query databases using Python code, allowing for seamless integration between the code and the underlying database system.

We will use SQLAlchemy to carry out Create, Read, Update and Delete (CRUD) operations on the database to present a list of products and add a layer of authentication using Flask.

For this project, create new folders and files with the following file structure.

- Create a project folder named **tut3**
- Within the tut3 folder, create 1 folder named **app**
- Within the **app** folder, create 7 files
    - `__init__.py`
    - controllers.py
    - database.py
    - main.py
    - models.py
    - requirements.txt
    - schemas.py
Here's a brief description of what each file will do. 

1. `__init__.py` is used to indicate the directory should be treated as a Python package. We will not be adding any code to this file.
2. `controllers.py` will define our helper functions that carry out the CRUD operations
3. `database.py` contains our database connection code
4. `models.py` stores our database objects for SQLAlchemy to use
5. `requirements.txt` is used to enter the dependencies that will be installed
6. `schemas.py` will define our data structures for Python to use.
Run the following command in the **tut3** directory to initialise your virtual environment in the venv/ directory.

`python3 -m venv ./venv/`

To initialise your virtual environment, you will need to enter the following command in your terminal. 

🪟 Windows users: `.\venv\Scripts\activate.bat`

🍎 MacOS and Linux Users: `source ./venv/bin/activate`

# Step 2: Updating Your Dependencies
In the requirements.txt file, add the following lines to install the packages required in this project. Be sure to save your file once done.

```text
fastapi
uvicorn
pydantic
sqlalchemy
```

We will then install the packages with the following command. Ensure your terminal's working directory is **app**. If pip3 does not work, you can try using pip.

`pip3 install -r requirements.txt`

Your terminal output should show that the packages have been successfully installed.