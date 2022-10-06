
 
CREATE TABLE contactos(
	id_contacto integer PRIMARY KEY AUTOINCREMENT,
	nombre varchar (30) not null,
	email varchar (50) not null unique,
	telefono varchar (50) not null
);

INSERT INTO contactos (nombre,email,telefono) VALUES ("Saul","saul_736@hotmail.com","5584485068");
INSERT INTO contactos (nombre,email,telefono) VALUES ("Itzel","itzelpv@email.com","555476021");

SELECT * FROM  contactos;