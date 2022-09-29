
from fastapi import FastAPI
import sqlite3
from typing import list
from pydantic import BaseModel
from fastapi import HTTPException,status


class Mensaje(Base Model):
	mensaje:str

class Contactos(Base Model):
	id_contacto:int
	nombre:str
	email:str
	telefono:str

description= """
	#Contactos Api REST
	API para crar un CRUD
	de la tabla contactos
	"""
app= Fast API(
	title="contactos API REST",
	description=description,
	version= "0.1",
	contact= {"name":"Jesus Yael",
		"email":"1721110698@utectulancingo.edu.mx"
	}
			
)

@app.get(
	"/",
	response_model= Mensaje,
	status_code= status.HTTP_202_ACCEPTED,
	summary="endpoint principal",
	description="regresar mensaje de bienvenida",
)
async dif read_root():
	response={"mensaje":"version 0.1"}
	return response

@app.get(
	"/contactos/",
	response_model= List[contactos],
	status_code= status.HTTP_202_ACCEPTED,
	summary="lista de contactos",
	description="endpoint que regresara un array con todos los contactos",
)
async dif get_contactos():
	try:
		with sqlite3.connect("API/sql/contactos.db") as connection:
		connection.row_factory=sqlite3.Row
		cursor=connection.cursor()
		cursor.execute(SELECT id_contacto,nombre,email,telefono FROM contactos;")
		response=cursor.Fetchall()
		return response
	exept Exeception as error:
		print (f "Error en get_cotactos {error.asgs}")
		raise HTTPException(
		status_code=status.HTTP_400_BAD_REQUEST,
		detail="Error al consultar los datos"
		)
