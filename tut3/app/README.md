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

### Step 2: Updating Your Dependencies
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

### Step 3: Connecting a Database
Before we start creating our database tables, we need to connect to a database. This could be MySQL, PostgreSQL or other servers. We will use an SQLite database file for simplicity.

In the file **database.py**, enter the following code to create the engine, session and base that will be imported into the other files for database operations. Replace StackUp_USERNAME with your StackUp username.

```python
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./STACKUP_USERNAME.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
```


This code creates an SQLAlchemy engine that connects to the URL specified in the `SQLALCHEMY_DATABASE_URL` variable, which in this case is an SQLite database file. If the database file does not exist, it will create the file in the tut3 folder the first time you establish a connection.

It then creates a sessionmaker object to create Session objects that can be used to interact with the database and a `Base` which will help with generated mapped Table objects for your models.


### Step 4: Creating the Models
Now, we want to create some classes that SQLAlchemy can use to help us with querying and managing our database. For this project, we will create 1 class that reflects the attributes of a table containing item/product information.

In **models.py**, paste the following code and save the file.

```python
from sqlalchemy import Column, Integer, String

from .database import Base

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    price = Column(Integer)
```

The code creates the Item class with some standard attributes such as the product’s title, description and price.


### Step 5: Organising the Schemas

With the database connection set up and our Item model defined, we now need to create schemas with Pydantic that allow FastAPI to expect pre-defined data structures in requests for specific actions.

In **schemas.py**, paste the following code to create these classes.

In the first line, we import the `BaseModel` class that we can use to define how our data looks and its validation requirements.

```python
from pydantic import BaseModel
```

Subsequently, we create the `ItemBase` class using the BaseModel to define the attributes our Item class should contain.

```python
class ItemBase(BaseModel):
    title: str
    description: str | None = None
    price: float
```

Within the ItemBase class, we define 3 attributes:

- The title, which should be a string
- The description, which should be a string but is optional
- The price, which should be a float/decimal

Next, we create the ItemCreate class.

```python
class ItemCreate(ItemBase):
    pass
```

This class inherits the attributes from the `ItemBase` class and can contain any other attributes that may be required for creation.

Lastly, we create the Item class that contains the ID attribute for when the database assigns an auto-incrementing ID number to the object.

```python
class Item(ItemBase):
    id: int
```
Your **schemas.py** file should now look like this. Remember to save your file.

```python
from pydantic import BaseModel

class ItemBase(BaseModel):
    title: str
    description: str | None = None
    price: float

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: int
```

### Step 6: Creating the Controllers

For our application to execute CRUD operations on the database, we should first define some reusable helper functions that we could use later.

In **controllers.py**, enter the following code in order.

First, we import the Session class from SQLAlchemy and the models and schemas we defined earlier.

```python
from sqlalchemy.orm import Session

from . import models, schemas
```

Next, we can write the function that reads rows from the database.

```python
def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()
```

The function takes in a database session, the `skip` and `limit` arguments to allow users to filter data by offset and limit the number of results returned. It then queries the database for all filtered Item objects.

We can write a similar function to query a single Item object by specifying the ID.

```python
def get_item(db: Session, item_id: int):
    return db.query(models.Item).filter(models.Item.id == item_id).first()
```

Then, we can write the function to Create, or add rows to the Items table.

```python
def create_item(db: Session, item: schemas.ItemCreate):
    db_item = models.Item(title=item.title, description=item.description, price=item.price)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
```

The function takes in a database session and an item object using the schema we created earlier. It creates an Item object using the model we created in models.py. It uses the attributes from the item passed in and adds the object to the database. It then commits the change.

To allow updating of rows, we can use the following function.

```python
def update_item(db: Session, item_id: int, item: schemas.ItemCreate):
    db_item = db.query(models.Item).filter(models.Item.id == item_id).first()
    db_item.title = item.title
    db_item.description = item.description
    db_item.price = item.price
    db.commit()
    db.refresh(db_item)
    return db_item
```

The function takes in a database session, the ID of the item to update, and the item object with the updated attributes. It first queries the existing row by retrieving the Item object with the corresponding ID, then assigning new values to the attributes and finally committing the changes.

Lastly, a function to delete Item objects by their numerical ID.

```python
def delete_item(db: Session, item_id: int):
    db_item = db.query(models.Item).filter(models.Item.id == item_id).first()
    db.delete(db_item)
    db.commit()
    return db_item
```

The function takes in a database session and the ID of the item to delete. It then simply queries the Item with the corresponding ID and deletes it from the database, committing the changes afterwards.

Your final code in **controllers.py** should look similar to this. Remember to save your file.

```python
from sqlalchemy.orm import Session

from . import models, schemas

def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()

def get_item(db: Session, item_id: int):
    return db.query(models.Item).filter(models.Item.id == item_id).first()

def create_item(db: Session, item: schemas.ItemCreate):
    db_item = models.Item(title=item.title, description=item.description, price=item.price)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def update_item(db: Session, item_id: int, item: schemas.ItemCreate):
    db_item = db.query(models.Item).filter(models.Item.id == item_id).first()
    db_item.title = item.title
    db_item.description = item.description
    db_item.price = item.price
    db.commit()
    db.refresh(db_item)
    return db_item

def delete_item(db: Session, item_id: int):
    db_item = db.query(models.Item).filter(models.Item.id == item_id).first()
    db.delete(db_item)
    db.commit()
    return db_item
```

### Step 7: Putting Everything Together

Now that all our models, schemas and controllers have been created, we can put the application together in **main.py**. For all the code chunks mentioned in this step, add them to main.py.

Firstly, we import our FastAPI and SQLAlchemy dependencies, as well as the classes we wrote earlier.

```python
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import controllers, models, schemas
from .database import SessionLocal, engine
```

Next, create all the tables defined in models.py.

```python
models.Base.metadata.create_all(bind=engine)
```

Then, create the FastAPI application.

```python
app = FastAPI()
```

We can define a helper function `get_db()` that will be used as a dependency to check if the database is up.

```python
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

Now we can write the functions for our CRUD operations.

To allow users to read from our database, we can create endpoints at `/items` and `/items/{item_id}` that support GET requests, utilising the functions, `read_items()` and `read_item()` we created in controllers.py.

```python
@app.get("/items/", response_model=list[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = controllers.get_items(db, skip=skip, limit=limit)
    return items

@app.get("/items/{item_id}", response_model=schemas.Item)
def read_item(item_id: int, db: Session = Depends(get_db)):
    db_item = controllers.get_item(db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item
```

In the `read_items` function, we take in the `skip` and `limit` arguments as query parameters. These arguments allow users to filter through the data. For example, skip=1 selects from the second row onwards, and limit=50 limits the number of rows returned to the first fifty. The function then creates a database connection using our helper function `get_db()`.

It then passes the database connection and the arguments to our `get_items()` controller function to retrieve all items, and returns it as JSON that conforms to the response model list (`schemas.Item`) which means an array/list of Item classes.

`read_item()` is similar but retrieves only one item by its ID, as in `/items/1`, returning a single dictionary if the item exists.

Next, we create a listener for POST requests to `/items` which allows users to create Items, or add rows to the table.

```python
@app.post("/items/", response_model=schemas.Item)
def create_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    return controllers.create_item(db=db, item=item)
```

The code is similar to the Read functions, except it expects a JSON request body that is validated by our `ItemCreate` schema. If valid, it creates an item and returns the Item as a JSON object, following the Item schema.

For updating rows, we create a listener for PUT requests to `/items/{item_id}`, which allows users to specify the ID of the item they would like to update in the URL, e.g. /items/1.

```python
@app.put("/items/{item_id}", response_model=schemas.Item)
def update_item(item_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)):
    db_item = controllers.update_item(db, item_id=item_id, item=item)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item
```

The function expects a JSON request body matching our `ItemCreate` schema, and passes it to our `update_item()` controller function with the specified ID. If the ID exists, the row in the table is updated. Otherwise, it simply responds with an error with the status code 404 and “Item not found” message.

Lastly, create a listener for DELETE requests to `/items/{item_id}` to allow users to delete Items by their ID.

```python
@app.delete("/items/{item_id}", response_model=schemas.Item)
def delete_item(item_id: int, db: Session = Depends(get_db)):
    db_item = controllers.delete_item(db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item
```

By now, your main.py should contain the following code. Remember to save your file. 

```python
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import controllers, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/items/", response_model=list[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = controllers.get_items(db, skip=skip, limit=limit)
    return items

@app.get("/items/{item_id}", response_model=schemas.Item)
def read_item(item_id: int, db: Session = Depends(get_db)):
    db_item = controllers.get_item(db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

@app.post("/items/", response_model=schemas.Item)
def create_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    return controllers.create_item(db=db, item=item)

@app.put("/items/{item_id}", response_model=schemas.Item)
def update_item(item_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)):
    db_item = controllers.update_item(db, item_id=item_id, item=item)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

@app.delete("/items/{item_id}", response_model=schemas.Item)
def delete_item(item_id: int, db: Session = Depends(get_db)):
    db_item = controllers.delete_item(db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item
```