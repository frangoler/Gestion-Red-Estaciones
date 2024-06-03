import mysql.connector
from mysql.connector import Error, connect, OperationalError
from datetime import date
import datetime
import random
from random import randrange
from datetime import timedelta
from datetime import datetime


class BaseDeDatos:
 
    def __init__(self, host_name, user_name, user_password,database):
        """Contructor y crea la conexion con la base de datos."""
        self.connection = None
        try:
            self.connection = connect(
                host=host_name,
                user=user_name,
                passwd=user_password,
                database=database
            )
            print("Connection to MySQL DB successful")
        except Error as e:
            print(f"The error '{e}' occurred")

    def cerrar_conexion(self):
        """Corta la conexion con la base de datos."""
        self.connection.close()

    def execute_query(self, query):
        """Ejecuta una consulta en la base de datos de escritura"""
        self.connection.autocommit = True
        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
            print("Query executed successfully")
            self.connection.commit()
        except OperationalError as e:
            print(f"The error '{e}' occurred")

    def execute_read_query(self, query):
        """Ejecuta una consulta en la base de datos de lectura"""
        cursor = self.connection.cursor()
        result = None
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except Error as e:
            print(f"The error '{e}' occurred")
    def listar_id_estaciones(self):
        """Lista las estaciones existentes en la base de datos"""
        lista=self.execute_read_query("SELECT e.ID FROM estacion e ")
        estaciones=[]
        for x in range(len(lista)):
            estaciones.append(lista[x][0])
        return estaciones   
    def listar_legajos(self):
        """Lista los legajos de los profesionales existentes en la base de datos"""
        lista=self.execute_read_query("SELECT p.legajo FROM profesional p ")
        profesionales=[]
        for x in range(len(lista)):
            profesionales.append(lista[x][0])
        return profesionales  
##--------------------------Consultas pedidas:-------------------------------------------------------
##--------------------------Ingreso de una estacion-------------------------------------------------------
    def ingresar_estacion(self):
        """Ingresa una estacion con su respectivas conexiones si las tiene"""
        nombre=input("Ingrese el nombre de la estacion: ")
        latitud=input("Ingrese Latitud: ")
        longitud=input("Ingrese longitud: ")
        a_start=input("Ingrese el año de inicio: ")
        m_start=input("Ingrese el mes de inicio: ")
        d_start=input("Ingrese el dia de inicio: ")
        fecha_instalacion=f"{a_start}-{m_start}-{d_start}"
        ID_instalador=input("Ingrese el ID del instalador existente: ")

        while(int(ID_instalador) not in self.listar_legajos()):
            ID_instalador=input("Ingrese el ID del instalador existente: ")

        str_ingreso_estacion_1=f"""INSERT INTO Estacion(nombre, latitud, longitud,fecha_instalacion,ID_instalador)
        VALUES("{nombre}",{latitud},{longitud},"{fecha_instalacion}",{ID_instalador})"""
        self.execute_query(str_ingreso_estacion_1)

        id_estacion=self.execute_read_query("SELECT MAX(ID) FROM estacion e ")[0][0]

        opcion = input("¿Desea agregar una conexion? (S/N): ")
        while (opcion.lower()=="s"):
            estacion_2=input("Ingrese el ID de la estacion a la que desea conectar: ")
            while(int(estacion_2) not in self.listar_id_estaciones()):
                estacion_2=input("ID no existe, ingrese un ID valido al cual conectar la estacion:")
            tipo=input("Ingese el tipo de conexion: 1.Radio , 2. Satelital: ")
            if (tipo=="1"):
                tipo="radio"
                str_conexion=f"""INSERT INTO conexion(tipo,ID_estacion_1,ID_estacion_2)
                            VALUES ("{tipo}",{id_estacion},{estacion_2})"""
                self.execute_query(str_conexion)
                opcion=input("¿Desea agregar otra conexion? (S/N): ")
            elif (tipo=="2"):
                tipo="satelital"    
                str_conexion=f"""INSERT INTO conexion(tipo,ID_estacion_1,ID_estacion_2)
                            VALUES ("{tipo}",{id_estacion},{estacion_2})"""
                self.execute_query(str_conexion)
                opcion=input("¿Desea agregar otra conexion? (S/N): ")
            else:
                tipo="Error"
                print("Error al cargar conexion, intente nuevamente")


##--------------------------Ingreso de una revision-------------------------------------------------------
    def ingresar_revision(self):
        """Ingresa una revision con el personal que estuvo involucrado"""
        fecha_rev=date.today()

        desc_breve=input("Breve descripcion del trabajo realizado: ")
        ID_estacion=input("Ingrese un ID de una estacion existente: ")
        lista_estaciones=self.listar_id_estaciones()

        while(int(ID_estacion) not in lista_estaciones):
            ID_estacion=input("Ingrese un ID de una estacion existente: ")

        str_ingreso_revision=f"""INSERT INTO Revision(fecha,descripcion,ID_estacion) 
                                VALUES ("{fecha_rev}","{desc_breve}",{ID_estacion})"""

        self.execute_query(str_ingreso_revision)

        #Chequeo cual es la ultima revision
        ultima_revision=self.execute_read_query("SELECT MAX(ID) FROM revision r")[0][0]
        ID_instalador=self.execute_read_query(f"""SELECT e.ID_instalador 
                                              FROM estacion e WHERE e.ID={ID_estacion}""")[0][0]
        str_ingreso_profesional=f"""INSERT INTO grupos_profesionales(ID_profesional,ID_revision)
                                VALUES ({ID_instalador},{ultima_revision})"""
        
        self.execute_query(str_ingreso_profesional)
        #Ingreso los profesionales involucrados
        opcion = input("¿Desea agregar otro profesional involucrado?Ya fue ingresado el instalador:(S/N)")
        while opcion.lower()=="s" :
            ID_prof=input("Ingrese el ID del profesional: ")
            
            str_ingreso_profesional=f"""INSERT INTO grupos_profesionales(ID_profesional,ID_revision)
                                VALUES ({ID_prof},{ultima_revision})"""
            self.execute_query(str_ingreso_profesional)
            opcion=input("¿Desea agregar otro profesional? (S/N): ")
##--------------------------Listar conexiones--------------------------------------------------------------
    def lista_conexiones(self):
        """Lista las conexiones entre estaciones existentes"""
        str_conexiones="""SELECT c.ID_estacion_1 ,c.ID_estacion_2 
                        FROM conexion c """
        return self.execute_read_query(str_conexiones)
##--------------------------Generar Metricas---------------------------------------------------------------
    def generar_metricas_agua_random(self,cantidad,estacion):
        """Genera metricas aleatorias simuladas de temperatura de agua por N cantidad en X estacion"""
        for x in range(cantidad): 
            medicion = round(random.uniform(2,15),2)
            if(random.randint(1,2)==1):
                unidad = "°C"
            else:
                unidad="°K"
                medicion=medicion+273
            ID_estacion=estacion
            str_consulta_fecha_instalacion=f"""SELECT e.fecha_instalacion 
                                            FROM estacion e
                                            WHERE  e.ID={ID_estacion}"""
            start_date = self.execute_read_query(str_consulta_fecha_instalacion)[0][0]
            end_date= datetime.today()
            fecha = start_date + (end_date - start_date) * random.random()
            str_insert_metrica_agua=f""" INSERT INTO metricaagua(medicion,unidad,tiempo,ID_estacion)
                                        VALUES ({medicion},"{unidad}","{str(fecha)}",{ID_estacion})"""
            self.execute_query(str_insert_metrica_agua)

    def generar_metricas_viento_random(self,cantidad,estacion):
        """Genera metricas aleatorias simuladas de viento por N cantidad en X estacion"""
        for x in range(cantidad): 
            velocidad = random.randint(5,40)
            booleano_direccion=random.randint(1,8)
            match booleano_direccion:
                case 1: 
                    direccion="N"
                case 2: 
                    direccion="S"
                case 3: 
                    direccion="E"
                case 4: 
                    direccion="O"
                case 5: 
                    direccion="NO"
                case 6: 
                    direccion="NE"
                case 7: 
                    direccion="SO"
                case 8: 
                    direccion="SE"
            ID_estacion=estacion
            str_consulta_fecha_instalacion=f"""SELECT e.fecha_instalacion 
                                            FROM estacion e
                                            WHERE  e.ID={ID_estacion}"""
            start_date = self.execute_read_query(str_consulta_fecha_instalacion)[0][0]
            end_date= datetime.today()
            fecha = start_date + (end_date - start_date) * random.random()
            str_insert_metrica_viento=f""" INSERT INTO metricaviento(velocidad,direccion,tiempo,ID_estacion)
                                        VALUES ({velocidad},"{direccion}","{str(fecha)}",{ID_estacion})"""
            self.execute_query(str_insert_metrica_viento)

##--------------------------Obtener registros--------------------------------------------------------------
    def registro_metricas_agua(self,start_date,end_date,estacion):
        """Devuelve una lista de registros de agua en cierto rango de fechas"""
        str_registro=f"""SELECT *
        FROM metricaagua ma
        WHERE ma.tiempo>"{start_date}" AND ma.tiempo<"{end_date}" AND ma.ID_estacion={estacion} """
        return self.execute_read_query(str_registro)## bien, hay que hacer una funcion para el print

    def registro_metricas_viento(self,start_date,end_date,estacion):
        """Devuelve una lista de registros de viento en cierto rango de fechas"""
        str_registro=f"""SELECT *
        FROM metricaviento mv
        WHERE mv.tiempo>"{start_date}" AND mv.tiempo<"{end_date}" AND mv.ID_estacion={estacion} """
        return self.execute_read_query(str_registro)## bien, hay que hacer una funcion para el print

###--------------------------Estacion con mayor temperatura promedio----------------------------------------
    def max_t_prom(self):
        """Obtenemos la estacion y mes con mayor temperatura promedio mensual"""
        str_mtp=f"""
                SELECT *
                FROM    ((SELECT ma1.ID_estacion , month(ma1.tiempo) as Mes, year(ma1.tiempo) as Año , ma1.medicion as medicion
                        FROM metricaagua ma1 
                        WHERE ma1.unidad="°C" )
                        UNION 
                        (SELECT ma1.ID_estacion ,  month(ma1.tiempo) as Mes, year(ma1.tiempo) as Año , ma1.medicion-273 as medicion
                        FROM metricaagua ma1
                        WHERE ma1.unidad="°K")) AS t_d
                GROUP BY ID_estacion, MES, AÑO
                ORDER BY AVG(medicion) DESC
                LIMIT 1""" 
        return self.execute_read_query(str_mtp)
##-----------------------Ultimas 5 estaciones revisadas por empleado---------------------------------------
    def ult_cinco(self,empleado_id):
        """Lista las ultimas 5 revisiones de X empleado"""
        str_ulti_cinco=f"""select e.nombre, e.ID
        from estacion e, grupos_profesionales gp, revision r
        where (r.ID = gp.ID_revision) and (gp.ID_profesional = {empleado_id}) and (r.ID_estacion = e.ID) 
        order by (r.fecha) desc limit 5"""
        return self.execute_read_query(str_ulti_cinco) 
##----------Estaciones que están a distancia menor o igual a 2 en conexiones punto a punto.----------------  
    def get_pto_pto(self,id_estacion):
        """Obtenemos la lista de estaciones a menor o iguala dos conexiones punto a punto
        para X estacion"""
        str_get_pto=f"""
        select c.ID_estacion_2   
        from conexion c 
        where c.ID_estacion_1 = {id_estacion}
        union
        select c.ID_estacion_1   
        from conexion c 
        where c.ID_estacion_2 = {id_estacion}
        union
        select c2.ID_estacion_1 
        from conexion c2
        where c2.ID_estacion_2 in (select c.ID_estacion_2   
                                    from conexion c 
                                    where c.ID_estacion_1 = {id_estacion}
                                    union
                                    select c.ID_estacion_1   
                                    from conexion c 
                                    where c.ID_estacion_2 = {id_estacion})
        union
        select c2.ID_estacion_2
        from conexion c2
        where c2.ID_estacion_1 in (select c.ID_estacion_2   
                                    from conexion c 
                                    where c.ID_estacion_1 = {id_estacion}
                                    union
                                    select c.ID_estacion_1   
                                    from conexion c 
                                    where c.ID_estacion_2 ={id_estacion})
        """
        consult_list=self.execute_read_query(str_get_pto)
        lista=[]
        for estacion in consult_list:
            if (estacion[0] != int(id_estacion)):
                lista.append(estacion[0])
        return lista

##--------------------------------Distancia entre estaciones-----------------------------------------
    def menor_distancia_dada(self,id_estacion,r):
        """Dada una estacion y un radio la estaciones a una distancia menor dada"""
        str_get_id=f"""select e.latitud,e.longitud
        from estacion e
        where {id_estacion} = e.ID
        """
        tupla=self.execute_read_query(str_get_id)[0]

        str_dist_dada=f"""select heaversine({tupla[0]},{tupla[1]},e.latitud,e.longitud),e.ID
        from estacion e
        where (({tupla[0]}!=e.latitud) or ({tupla[1]}!=e.longitud)) AND 
        (heaversine({tupla[0]},{tupla[1]},e.latitud,e.longitud)<{r})
        """
        return self.execute_read_query(str_dist_dada)