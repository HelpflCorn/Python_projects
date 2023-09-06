from typing import Union
import mysql.connector
from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

@app.get("/")
def read_root():
    return {"Hello": "World"}



@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": Item, "item_id": item_id}


def connector(query):
    cnx = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="44992067",
        database="newschema")

    cur = cnx.cursor()

    # Execute a query
    cur.execute(query)

    # Fetch one result
    row = cur.fetchall()
    print(row)

    # Close connection
    cnx.close()



@app.get("/employees")
def task1():
    q = connector("SELECT first_name, last_name FROM employees;")
    cconverted_data_into_dict =  dict((i,j) for i,j in q)
    return print(cconverted_data_into_dict)

task1()