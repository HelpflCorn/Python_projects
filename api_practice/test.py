import mysql.connector
from fastapi import FastAPI
from main import connector
import requests
from typing import Union
from pydantic import BaseModel

url1 = ("http://127.0.0.1:8000/")


app = FastAPI()

@app.post("/")
async def root():
    return {connector("SELECT first_name, last_name FROM employees WHERE employee_id = 100"): "Whatever"}


# from fastapi import FastAPI, HTTPException
# import mysql.connector

# app = FastAPI()

# # Database connection parameters
# db_config = {
#     "host": "127.0.0.1",
#     "port": 3306,
#     "user": "root",
#     "password": "44992067",
#     "database": "newschema",
# }

# # Function to create a database connection
# def create_db_connection():
#     return mysql.connector.connect(**db_config)

# # Function to execute a query and fetch data
# def execute_query(query):
#     try:
#         cnx = create_db_connection()
#         cursor = cnx.cursor()

#         cursor.execute(query)
#         result = cursor.fetchall()

#         return result
#     except mysql.connector.Error as err:
#         raise HTTPException(status_code=500, detail=f"Database error: {err}")
#     finally:
#         cursor.close()
#         cnx.close()

# @app.get("/")
# async def root():
#     return {"message": "Hello World"}

# @app.post("/items/{item_id}")
# def create_item(item_id: int):
#     try:
#         # Define your SQL queries here
#         employee_id_query = f"SELECT employee_id FROM employees WHERE employee_id = {item_id}"
#         name_query = f"SELECT first_name, last_name FROM employees WHERE employee_id = {item_id}"

#         # Execute the queries and fetch data
#         employee_id = execute_query(employee_id_query)
#         name = execute_query(name_query)

#         if employee_id and name:
#             item_name = f"{name[0][0]} {name[0][1]}"
#             return {"item_name": item_name, "item_id": item_id}
#         else:
#             raise HTTPException(status_code=404, detail="Item not found")
#     except Exception as e:
#         raise HTTPException(status_code=500, detail="Internal Server Error")
