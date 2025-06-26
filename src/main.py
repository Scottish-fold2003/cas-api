from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

def get_db_connection():
  cnx = mysql.connector.connect(
    host = os.getenv("MYSQL_HOST"),
    user = os.getenv("MYSQL_USERNAME"),
    password = os.getenv("MYSQL_Password"),
    database = os.getenv("MYSQL_DATABASE")
  )
  return cnx

app = FastAPI()

app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"],
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"]
)

@app.get('/ref_division')
def  get_ref_division():
  cnx = get_db_connection()
  cursor = cnx.cursor()
  query = "SELECT * FROM ref_division"
  cursor.execute(query)
  rows = cursor.fetchall()
  cursor.close()
  cnx.close()
  return[dict(zip(cursor.column_names, row)) for row in rows]

@app.get('/ref_division_location')
def  get_ref_division_location():
  cnx = get_db_connection()
  cursor = cnx.cursor()
  query = "SELECT * FROM ref_division_location"
  cursor.execute(query)
  rows = cursor.fetchall()
  cursor.close()
  cnx.close()
  return[dict(zip(cursor.column_names, row)) for row in rows]

@app.get('/ref_floor')
def get_ref_floor():
  cnx = get_db_connection()
  cursor = cnx.cursor()
  query = "SELECT * FROM ref_floor"
  cursor.execute(query)
  rows = cursor.fetchall()
  cursor.close()
  cnx.close()
  return [dict(zip(cursor.column_names, row)) for row in rows]

@app.get('/data_asset')
def get_data_asset():
  cnx = get_db_connection()
  cursor = cnx.cursor()
  query = "SELECT * FROM data_asset"
  cursor.execute(query)
  rows = cursor.fetchall()
  cursor.close()
  cnx.close()
  return [dict(zip(cursor.column_names, row)) for row in rows]

@app.get('/data_asset_test')
def get_data_asset_test():
  cnx = get_db_connection()
  cursor = cnx.cursor()
  query = "SELECT * FROM data_asset_test"
  cursor.execute(query)
  rows = cursor.fetchall()
  cursor.close()
  cnx.close()
  return [dict(zip(cursor.column_names, row)) for row in rows]

@app.get('/data_asset_new')
def get_data_asset_new():
  cnx = get_db_connection()
  cursor = cnx.cursor()
  query = "SELECT * FROM data_asset_new"
  cursor.execute(query)
  rows = cursor.fetchall()
  cursor.close()
  cnx.close()
  return [dict(zip(cursor.column_names, row)) for row in rows]

@app.get('/data_dcd_project')
def get_data_dcd_project():
  cnx = get_db_connection()
  cursor = cnx.cursor()
  query = "SELECT * FROM data_dcd_project"
  cursor.execute(query)
  rows = cursor.fetchall()
  cursor.close()
  cnx.close()
  return [dict(zip(cursor.column_names, row)) for row in rows]

@app.get('/data_cctv')
def get_data_cctv():
  cnx = get_db_connection()
  cursor = cnx.cursor()
  query = "SELECT * FROM data_cctv"
  cursor.execute(query)
  rows = cursor.fetchall()
  cursor.close()
  cnx.close()
  return [dict(zip(cursor.column_names, row)) for row in rows]

@app.get('/data_land_court')
def get_data_land_court():
  cnx = get_db_connection()
  cursor = cnx.cursor()
  query = "SELECT * FROM data_land_court"
  cursor.execute(query)
  rows = cursor.fetchall()
  cursor.close()
  cnx.close()
  return [dict(zip(cursor.column_names, row)) for row in rows]

@app.get('/data_dcd_work')
def get_data_dcd_work():
  cnx = get_db_connection()
  cursor = cnx.cursor()
  query = "SELECT * FROM data_dcd_work"
  cursor.execute(query)
  rows = cursor.fetchall()
  cursor.close()
  cnx.close()
  return [dict(zip(cursor.column_names, row)) for row in rows]

@app.get('/data_dcd_project_new')
def get_data_dcd_project_new():
  cnx = get_db_connection()
  cursor = cnx.cursor()
  query = "SELECT * FROM data_dcd_project_new"
  cursor.execute(query)
  rows = cursor.fetchall()
  cursor.close()
  cnx.close()
  return [dict(zip(cursor.column_names, row)) for row in rows]

@app.get('/data_fireescape')
def get_data_fireescape():
  cnx = get_db_connection()
  cursor = cnx.cursor()
  query = "SELECT * FROM data_fireescape"
  cursor.execute(query)
  rows = cursor.fetchall()
  cursor.close()
  cnx.close()
  return [dict(zip(cursor.column_names, row)) for row in rows]

@app.get('/data_ojso_asset_plan')
def get_data_ojso_asset_plan():
  cnx = get_db_connection()
  cursor = cnx.cursor()
  query = "SELECT * FROM data_ojso_asset_plan"
  cursor.execute(query)
  rows = cursor.fetchall()
  cursor.close()
  cnx.close()
  return [dict(zip(cursor.column_names, row)) for row in rows]

@app.get('/data_ojso_asset_plan_new')
def get_data_ojso_asset_plan_new():
  cnx = get_db_connection()
  cursor = cnx.cursor()
  query = "SELECT * FROM data_ojso_asset_plan_new"
  cursor.execute(query)
  rows = cursor.fetchall()
  cursor.close()
  cnx.close()
  return [dict(zip(cursor.column_names, row)) for row in rows]

@app.get('/data_dcd_court_info')
def get_data_dcd_court_info():
  cnx = get_db_connection()
  cursor = cnx.cursor()
  query = "SELECT * FROM data_dcd_court_info"
  cursor.execute(query)
  rows = cursor.fetchall()
  cursor.close()
  cnx.close()
  return [dict(zip(cursor.column_names, row)) for row in rows]