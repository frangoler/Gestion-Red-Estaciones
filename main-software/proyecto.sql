CREATE DATABASE RedEstaciones


CREATE TABLE Profesional(nombre CHAR(20),
						 apellido CHAR(20),
						 legajo INT AUTO_INCREMENT,
						 PRIMARY KEY (legajo))

CREATE TABLE Estacion(nombre CHAR(20),
					  latitud DOUBLE,
					  longitud DOUBLE,
					  fecha_instalacion DATETIME NOT NULL,
					  ID INT AUTO_INCREMENT,
					  ID_instalador INT,
					  FOREIGN KEY(ID_instalador) REFERENCES Profesional(legajo),
					  PRIMARY KEY (ID))
					  
					 
					  
CREATE TABLE MetricaAgua(medicion FLOAT NOT NULL,
						  unidad CHAR(5),
						  tiempo DATETIME,
						  ID INT AUTO_INCREMENT,
						  ID_estacion INT,
						  PRIMARY KEY (ID),
						  FOREIGN KEY (ID_estacion) REFERENCES Estacion(ID))
						  
						  
CREATE TABLE MetricaViento(velocidad FLOAT NOT NULL,
						  direccion CHAR(5) NOT NULL,
						  tiempo DATETIME,
						  ID INT AUTO_INCREMENT,
						  ID_estacion INT,
						  PRIMARY KEY (ID),
						  FOREIGN KEY (ID_estacion) REFERENCES Estacion(ID))
						  
						  				 
						 
CREATE TABLE Conexion(tipo CHAR(20),
                      ID_estacion_1 INT,
                      ID_estacion_2 INT,
                      PRIMARY KEY (ID_estacion_1,ID_estacion_2),
					  FOREIGN KEY (ID_estacion_1) REFERENCES Estacion(ID),
					  FOREIGN KEY (ID_estacion_2) REFERENCES Estacion(ID)
                      )
                      

						 
CREATE TABLE Revision(fecha DATE,
					  descripcion TINYTEXT,#TINYTEXT tiene como maximo 255 caracteres creo que estaria bien 
					  ID INT AUTO_INCREMENT,
					  ID_estacion INT,
					  PRIMARY KEY (ID),
					  FOREIGN KEY (ID_estacion) REFERENCES Estacion(ID)
					  )	

					  
##Relacion entre profesional y estaciones;
CREATE TABLE Grupos_Profesionales(ID_profesional INT,
								  ID_revision INT,
								  PRIMARY KEY (ID_profesional, ID_revision),
								  FOREIGN KEY (ID_profesional) REFERENCES Profesional(legajo),
								  FOREIGN KEY (ID_revision) REFERENCES Revision(ID)
								  )			
##Funcion 
create function heaversine(lat1 float, long1 float, lat2 float, long2 float)
returns float
begin
	 DECLARE r float;
 	 SET r = 6371; -- Radio de la Tierra en kilómetros
	 SET lat1 = RADIANS(lat1);
	 SET long1 = RADIANS(long1);
	 SET lat2 = RADIANS(lat2);
	 SET long2 = RADIANS(long2);
RETURN r * 2 * ASIN(SQRT(POWER(SIN((lat2 - lat1) / 2), 2) + COS(lat1) * COS(lat2) * POWER(SIN((long2 - long1) / 2), 2)));
end								  
	












