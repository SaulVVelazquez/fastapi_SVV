from fastapi import FastAPI
import sqlite3
from typing import List
from pydantic import BaseModel
from pydantic import EmailStr
from fastapi import HTTPException
from fastapi import status
from fastapi.responses import JSONResponse

class Mensaje(BaseModel):
    mensaje: str

class Contactos(BaseModel):
    id_contacto: int
    nombre: str
    email: str
    telefono: str

class ContactosIN(BaseModel):
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
    response_model=Mensaje,
    status_code=status.HTTP_202_ACCEPTED,
    summary="Endpoint principal",
    description=" Regresa un mensaje de bienvenida",
)

async def read_root ():
    response = {"mensaje": "version 0.1"}
    return response

@app.get (
    "/contactos/{id_contacto}",
    response_model=Contactos,
    status_code=status.HTTP_202_ACCEPTED,
    summary="Contacto a obtener",
    description="Endpoint que regresa un array con el id de un solo contactos",
)

async def get_contactos(id_contacto:int):
    try:
        with sqlite3.connect("API/sql/contactos.db") as connection:
            connection.row_factory = sqlite3.Row
            cursor = connection.cursor()
            sql="SELECT id_contacto, nombre, email, telefono FROM contactos WHERE id_contacto = ? ;"
            values=(id_contacto,)
            cursor.execute(sql,values)
            response= cursor.fetchone()
            if response == None:
                return JSONResponse(status_code = 404, content ={"mensaje":"id_contacto no existente"})
            else:
                return response    
    except Exception as error:
        print(f"Error interno: {error.args}")
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST,
            detail = "Error al consultar los datos",
        ) 	

@app.get (
    "/contactos/",
    response_model = List[Contactos],
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

@app.post(
    "/contactos/",
    response_model = Mensaje,
    summary ="Ingresa un nuevo contacto",
    description = "Endpoint para ingresar un Contacto nuevo"
)

async def post_contactos(contacto: ContactosIN):
    try:
        with sqlite3.connect("sql/contactos.db") as connection:
            connection.row_factory = sqlite3.Row
            cursor = connection.cursor()
            consult=("SELECT email FROM contactos;")
            existent_emails = cursor.fetchall()
            print(existent_emails)
            if contacto.email in existent_emails:
                response = {"mensaje":"Email del contacto duplicado, por favor ingrese otro"}
                return response
            else:
                sql="INSERT INTO contactos VALUES (NULL, ?, ?, ?);"
                values = contacto.nombre, contacto.email, contacto.telefono
                cursor.execute(sql, values)
                response = {"mensaje":"Contacto registrado con éxito"}
                return response
    except Exception as error:
        print(f"Error al ingresar un dato{error.args}")
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST,
            detail="No se pudo ingresar el registro, intente de nuevo"
        )

@app.put(
    "/contactos/{id_contacto}",
    response_model = Mensaje,
    status_code = status.HTTP_202_ACCEPTED,
    description="Endpoint para actualizar un contacto"
)
async def put_contactos(id_contacto: int, contacto: ContactosIN):
    try:
        with sqlite3.connect("sql/contactos.db") as connection:
            connection.row_factory = sqlite3.Row
            cursor = connection.cursor()
            sql="UPDATE contactos SET nombre = ?, email = ?, telefono = ? WHERE id_contacto = ?;"
            values = contacto.nombre, contacto.email, contacto.telefono, id_contacto
            cursor.execute(sql, values)
            response = {"mensaje":"Contacto actualizado con éxito"}
            return response
    except Exception as error:
        print(f"Error al actualizar un dato{error.args}")
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST,
            detail="No se pudo actualizar el registro, intente de nuevo"
        )

@app.delete(
    "/contactos/{id_contacto}",
    response_model = Mensaje,
    status_code = status.HTTP_202_ACCEPTED,
    description="Endpoint para eliminar un contacto"
)
async def delete_contactos(id_contacto: int):
    try:
        with sqlite3.connect("sql/contactos.db") as connection:
            connection.row_factory = sqlite3.Row
            cursor = connection.cursor()
            sql="DELETE FROM contactos WHERE id_contacto = ?;"
            values = id_contacto
            cursor.execute(sql, values)
            response = {"mensaje":"Contacto eliminado con éxito"}
            return response
    except Exception as error:
        print(f"Error al eliminar un dato{error.args}")
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST,
            detail="No se pudo eliminar el registro, intente de nuevo"
        )