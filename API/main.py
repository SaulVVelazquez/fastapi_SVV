from fastapi import FastAPI
import sqlite3
from typing import List
from pydantic import BaseModel
from pydantic import EmailStr
from fastapi import HTTPException
from fastapi import status

class mensaje(BaseModel):
	mensaje: str

class contactos(BaseModel):
	id_contacto: int
	nombre: str
	email: str
	telefono: str

class contactosIN(BaseModel):
	nombre: str
	email: str
	telefono: str

description = """
	# Contactos  API REST
	API para crear un CRUD de la tabla contactos 
	"""
app = FastAPI(
	tittle = "Contactos API REST",
	description = description,
	version = "0.0.1",
	terms_of_service="http://example.com/terms/",
	contact = {
		"name": "saul",
		"email": "saul_736@hotmail.com",
	},
	license_info={
		"name":"Apache 2.0",
		"url":"https://www.apache.org/licenses/LICENSE-2.0.html",
	},
)

@app.get (
	"/",
	response_model=mensaje,
	status_code=status.HTTP_202_ACCEPTED,
	summary="Endpoint principal",
	description=" Regresa un mensaje de bienvenida",
)

async def read_root ():
	response = {"mensaje": "version 0.1"}
	return response

@app.get (
	"/contactos/{id_contacto}",
	response_model=contactosIN,
	status_code=status.HTTP_202_ACCEPTED,
	summary="Contacto a obtener",
	description="Endpoint que regresa un array con el id de un solo contactos",
)

async def get_contactos(id_contacto:int):
	try:
		with sqlite3.connect("API/sql/contactos.db") as connection:
			connection.row_factory = sqlite3.Row
			cursor = connection.cursor()
			sql="SELECT nombre,email,telefono FROM contactos WHERE id_contacto=?;"
			values=(id_contacto, )
			cursor.execute(sql,values)
			response= cursor.fetchone()
			return response
	except Exception as error:
		print(f"Error interno: {error.args}")
		raise HTTPException(
			status_code = status.HTTP_400_BAD_REQUEST,
			detail = "Error al consultar los datos",
		) 	

@app.get (
	"/contactos/",
	response_model = List[contactos],
	status_code = status.HTTP_202_ACCEPTED,
	summary = "Lista de contactos",
	description = "Endpoint que regresa un array con todos los contactos",
)

async def get_contactos():
	try:
		with sqlite3.connect("API/sql/contactos.db") as connection:
			connection.row_factory = sqlite3.Row
			cursor = connection.cursor()
			cursor.execute("SELECT id_contacto, nombre, email, telefono FROM contactos;")
			response = cursor.fetchall()
			return response
	except Exception as error:
		print(f"Error interno: {error.args}")
		raise HTTPException(
			status_code = status.HTTP_400_BAD_REQUEST,
			detail = "Error al consultar los datos",
		) 				