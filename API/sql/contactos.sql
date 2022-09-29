

CREATE TABLE contactos(
	id_contacto integer PRIMARY KEY AUTOINCREMENT,
	nombre varchar (30),
	email varchar (50),
	telefono varchar (50)
);

INSERT INTO contactos (nombre,email,telefono) VALUES ("Jose","jose@email.com","462342524");
INSERT INTO contactos (nombre,email,telefono) VALUES ("Luis","luis@email.com","563242526");