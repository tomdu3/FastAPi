# Tutorial 2: Creating a Basic API Server with FastAPI

## Learning Outcomes
Upon completing your learning, you will be able to:

- Understand how FastAPI works
- Create a Pydantic model
- Create simple CRUD API routes
- Use Postman to test your API

## Quest Details
### Introduction
Previously, you learnt about FastAPI and its capabilities, created your development environment, and deployed a basic FastAPI web application. However, the website currently only returns text upon receiving a GET request. You will be adding more routes than a typical API server would have.

You will learn how to create a basic API that can create, read, update and delete operations for a single data structure. Thereafter, we will be using the Postman application to test our API.

For this quest, you can attempt it using a cloud development environment like Codespaces and Gitpod, or on your local device.

## Quest Steps
Total Steps: 9

### Step 1: Basic HTTP with FastAPI
Previously, you created a single route at “/” for a page that simply returns some text upon receiving a GET request. However, API servers are expected to have many more endpoints that support various request methods for different purposes.

Typically, this is how API servers work in the context of managing users, with reference to the CRUD framework.

**GET** - Read

**POST** - Create

**PUT** - Update

**DELETE** - Delete

For example, the API endpoint for retrieving a list of users would look like

`GET /users`

For adding a new user to the database, it could look like the following, with a JSON body.

```
    POST /users

    {
        “username”: “john”,
        “email”: “john@stackup.com”
    }
```

And it would be very similar to updating an existing user.

```
    PUT /users

    {
        “username”: “john”,
        “email”: “john@stackup.com”
    }
```
To delete a user, a request like this could be utilised, to delete a user with the ID 1.

`DELETE /users/1`

There are many other ways API servers can be set up, including using query parameters like in “DELETE /users?id=1”, but it all depends on preference.

## Step 2: Routing with FastAPI
We now know how HTTP request methods can be utilised in creating an API server. However, different web frameworks utilise different methods for handling these request methods.

Previously, we used the following code to create the endpoint to return text when a GET request is made to “/”.

```python
    @app.get("/")
    def index():
        return "Hello from StackUp :D"
```
In the first line of this specific block of code, a decorator is used to add a handler for GET requests, as seen in “app.get”, including the route(“/”) as an argument.

To create handlers for other request methods, all you have to do is edit the “get” portion of the decorator. For an API endpoint for users, it would be:

```python
    @app.get("/users")
    @app.post("/users")
    @app.put("/users")
    @app.delete("/users/<int:id>")
```

## Step 3: Setting Up Our Environment
We will create some endpoints that will allow users to interact with our database with different HTTP methods.

For simplicity, let’s create a new folder **tut2** to prevent issues of conflict with your previously written code.

Within the tut2 folder, create 3 files – **main.py**, **models.py **and **requirements.txt**.

Next, create a virtual environment. Open a terminal in the **tut2** directory and run the following command to create a virtual environment. The venv module is a built-in module in Python used for creating virtual environments. Note, if python3 does not work, you can try using python.

`python3 -m venv ./venv/`

To initialise your virtual environment, you will need to enter the following command in your terminal. Once done, you should see (venv) appear in front of your direction in your terminal.

🪟 Windows users: `.\venv\Scripts\activate.bat`

🍎 MacOS and Linux Users: `source ./venv/bin/activate`

Then, declare the dependencies to install in requirements.txt. Be sure to save your file once done.

```
    fastapi
    uvicorn
    pydantic
```

Pydantic is a Python library crucial for data validation in web frameworks like FastAPI. Leveraging Python type annotations, it defines data models. FastAPI then uses these models to validate incoming request data and serialize response data. Its clear error messages and automatic documentation generation make it indispensable for efficient web development, enhancing robustness and productivity in creating and managing APIs.

In the terminal, we will proceed to install our dependencies with the following command.

`pip3 install -r requirements.txt`