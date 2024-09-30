# Tutorial 1: FastAPI

## Learning Outcomes

### Upon completing your learning, you will be able to:

- Explain what FastAPI is and its benefits compared to other frameworks
- Set up a development environment for FastAPI
- Create a basic FastAPI application

## Quest Details
### Introduction
Ready to embark on a journey to discover FastAPI? It is a lightweight web development framework that excels in delivering efficient applications with minimal code. We will delve into what FastAPI is, highlight its advantages, and showcase its diverse applications.

You will acquire the skills to develop a FastAPI web application, which can incorporate other packages and libraries to create more sophisticated and functional APIs. Finally, you will be well-equipped to harness FastAPI's capabilities and easily construct intricate web applications.


## Quest Steps
Total Steps: 4


### Step 1: The Capabilities of FastAPI
Before we get to creating the web application with Flask, it is important to learn about Flask and why it could be a web development framework worth using.

For a basic introduction, read this article for a quick overview of FastAPI.

FastAPI offers a multitude of benefits that make it a preferred choice for web application development. Here are the key advantages summarized in a list:

- **Speed and Performance:** FastAPI is renowned for its exceptional speed, thanks to its asynchronous capabilities. It can efficiently handle a large number of requests, making it ideal for high-performance applications.
- **Automatic Data Validation:** FastAPI automatically validates incoming data, reducing the risk of errors and vulnerabilities in your application. This feature simplifies input handling and improves data security.
- **Scalability:** FastAPI is well-suited for both small projects and large-scale applications, making it a versatile choice for developers with varying needs

### Step 2: Installing FastAPI
With your newfound knowledge of FastAPI, it's time to embark on the development journey! To kick things off, let's establish a development environment tailored to your FastAPI application.

We will create a virtual environment that encapsulates a self-contained Python environment to manage dependencies separately. This setup allows you to install and manage Python packages specific to this project or environment, all without impacting your system-wide Python installation or any other ongoing projects. Given that FastAPI is written in Python, those who are already familiar with the language will find these steps familiar.

You will need to install Python 3 and its package manager “pip”. To check if you have Python installed on your computer, you can enter the command `python --version` in your terminal. If a version number is returned, you have it installed. For users using cloud development environments like Gitpod, Codespaces and Google Cloud Shell, you most likely have Python and pip already installed.

🪟 For **Windows users**, you may download and install it at Python’s official website.

🍎 For **Mac users**, enter the following command in your terminal

`brew install python`

We will create a folder **FastAPI**. In this folder, create a folder named **tut1**. Within tut1,  create two new files – **main.py** and **requirements.txt**.

Next, open a terminal in the **tut1** directory and run the following command to create a virtual environment. The **venv** module is a built-in module in Python used for creating virtual environments.

`python3 -m venv ./venv/`

Next, we will be using the following command to activate the virtual environment that we just created. Once the command runs, you will notice the prompt in your terminal change, which now includes (venv). This indicates that you are now working in the virtual environment.

For Windows users

`.\venv\Scripts\activate.bat`
For MacOS and Linux users

`source ./venv/bin/activate`
Next, in **requirements.txt**, enter the following and save the file.

```text
    fastapi
    uvicorn
```

Plain text
Then, run the following command in your terminal to install the required packages that we listed in the requirements.txt file.

`pip install -r requirements.txt`

Uvicorn is a server implementation for Python. It is used primarily for running asynchronous web applications built with frameworks like FastAPI and Starlette. 