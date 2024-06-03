##Respetar el orden de ejecucion
##para que respete el orden de conexion explicado en el informe

##Esto es necesario si o si								  
INSERT INTO Profesional(nombre,apellido,legajo) VALUES("Francisco", "Aller",3000);
INSERT INTO Profesional(nombre,apellido) VALUES("Raamis","Daher");
INSERT INTO Profesional(nombre,apellido) VALUES("Fermin","Prat");							  
INSERT INTO Profesional(nombre,apellido) VALUES("Sebastian","Amoroso");
INSERT INTO Profesional(nombre,apellido) VALUES("Amparo","Martinez Sonaglioni");	
INSERT INTO Profesional(nombre,apellido) VALUES("Joaquin","Petruf");


#Si se hace esta carga mediante python no es necesario esto, pero si es necesario para cumplir con 
el orden de las conexiones explicado en el informe
INSERT INTO Estacion(nombre, latitud, longitud,fecha_instalacion,ID_instalador)
VALUES ("Narnia",38.97,64.11,"2020-09-04",3000)

INSERT INTO Estacion(nombre, latitud, longitud,fecha_instalacion,ID_instalador)
VALUES ("Estacion KM40",39.96,64.14,"2014-03-01",3001)
						  
INSERT INTO Estacion(nombre, latitud, longitud,fecha_instalacion,ID_instalador)
VALUES ("Disney",39.94,64.18,"2022-12-18",3002)

INSERT INTO Estacion(nombre, latitud, longitud,fecha_instalacion,ID_instalador)
VALUES ("Disney 2",38.99,64.06,"2021-09-05",3003)

INSERT INTO Estacion(nombre, latitud, longitud,fecha_instalacion,ID_instalador)
VALUES ("Disney +",38.99,64.06,"2005-08-04",3003)

INSERT INTO Estacion(nombre, latitud, longitud,fecha_instalacion,ID_instalador)
VALUES ("Estacion X",39.00,64.01,"2023-05-01",3004)

INSERT INTO Estacion(nombre, latitud, longitud,fecha_instalacion,ID_instalador)
VALUES ("Estacion Y",40.00,64.01,"2023-05-01",3005)

INSERT INTO Estacion(nombre, latitud, longitud,fecha_instalacion,ID_instalador)
VALUES ("Estacion Vieja",41.00,64.01,"2000-03-25",3005)



INSERT INTO conexion(tipo,ID_estacion_1,ID_estacion_2)
VALUES ("radio",1,2)

INSERT INTO conexion(tipo,ID_estacion_1,ID_estacion_2)
VALUES ("radio",2,3)

INSERT INTO conexion(tipo,ID_estacion_1,ID_estacion_2)
VALUES ("radio",8,7)

INSERT INTO conexion(tipo,ID_estacion_1,ID_estacion_2)
VALUES ("radio",6,7)

INSERT INTO conexion(tipo,ID_estacion_1,ID_estacion_2)
VALUES ("satelital",5,6)

INSERT INTO conexion(tipo,ID_estacion_1,ID_estacion_2)
VALUES ("satelital",1,5)

INSERT INTO conexion(tipo,ID_estacion_1,ID_estacion_2)
VALUES ("satelital",5,4)

INSERT INTO conexion(tipo,ID_estacion_1,ID_estacion_2)
VALUES ("satelital",2,4)

INSERT INTO conexion(tipo,ID_estacion_1,ID_estacion_2)
VALUES ("satelital",3,4)

