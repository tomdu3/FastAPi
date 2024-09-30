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