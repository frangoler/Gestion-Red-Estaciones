from basededatos import BaseDeDatos

database=BaseDeDatos("localhost", "root", "", "RedEstaciones")

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Menu
while True:
    print("----- Tareas-----")
    print("1. Ingresar Estacion")
    print("2. Ingresar Revision")
    print("3. Listar conexiones")
    print("4. Generar N cantidad de Metricas")
    print("5. Registro metricas viento")
    print("6. Registro metricas agua")
    print("7. Ultimas revisiones de X empleado")
    print("8. Estacion con mayor temperatura promedio")
    print("9. Distancia entre estaciones")
    print("10. Estaciones a menos de 2 punto a punto")
    print("11. Salir")
    opcion_elegida = input("Ingrese el número de la opción deseada: ")
    match int(opcion_elegida):
            case 1: 
                database.ingresar_estacion()
            case 2: 
                database.ingresar_revision()
            case 3: 
                lista=database.lista_conexiones()
                print("Conexiones por ID")
                for x in lista:
                    print(str(x[0])+"<----->"+str(x[1]))
            case 4: 
                cantidad=int(input("Ingrese la cantidad de metricas por estacion que desea: "))
                for estacion in database.listar_id_estaciones():
                    database.generar_metricas_agua_random(cantidad,estacion)
                    database.generar_metricas_viento_random(cantidad,estacion)
                    print(f"Metricas Estacion {str(estacion)} generadas")
            case 5: 
                ID_estacion=input("Ingrese el ID de la estacion a la que desea conectar: ")
                while(int(ID_estacion) not in database.listar_id_estaciones()):
                    ID_estacion=input("ID no existe, ingrese un ID valido al cual conectar la estacion:")
                a_start=input("Ingrese el año de inicio: ")
                m_start=input("Ingrese el mes de inicio: ")
                d_start=input("Ingrese el dia de inicio: ")
                fecha_start=f"{a_start}-{m_start}-{d_start}"
#
                a_end=input("Ingrese el año de fin: ")
                m_end=input("Ingrese el mes de fin: ")
                d_end=input("Ingrese el dia de fin: ")
                fecha_end=f"{a_end}-{m_end}-{d_end}"
                ##EJECUCION
                lista=database.registro_metricas_viento(fecha_start,fecha_end,ID_estacion)
                print("ID_estacion|Fecha|Velocidad|Direccion")
                for i in range(len(lista)):
                    str_print=f"{lista[i][4]}|{str(lista[i][2])}|{lista[i][0]}|{lista[i][1]}"
                    print(str_print)
            case 6: 
                ID_estacion=input("Ingrese el ID de la estacion a la que desea conectar: ")
                while(int(ID_estacion) not in database.listar_id_estaciones()):
                    ID_estacion=input("ID no existe, ingrese un ID valido al cual conectar la estacion:")
                a_start=input("Ingrese el año de inicio: ")
                m_start=input("Ingrese el mes de inicio: ")
                d_start=input("Ingrese el dia de inicio: ")
                fecha_start=f"{a_start}-{m_start}-{d_start}"

                a_end=input("Ingrese el año de fin: ")
                m_end=input("Ingrese el mes de fin: ")
                d_end=input("Ingrese el dia de fin: ")
                fecha_end=f"{a_end}-{m_end}-{d_end}"
                lista=database.registro_metricas_agua(fecha_start,fecha_end,ID_estacion)
                print("ID_estacion|fecha|medicion|unidad")
                for i in range(len(lista)):
                    str_print=f"{lista[i][4]}|{str(lista[i][2])}|{lista[i][0]}|{lista[i][1]}"
                    print(str_print)
            case 7: 
                ID_profesional=input("Ingrese el ID del profesional a supervisar: ")
                while(int(ID_profesional) not in database.listar_legajos()):
                    ID_profesional=input("Error, ingrese un profesional valido: ")
                lista=database.ult_cinco(ID_profesional)
                for revision in lista:
                    str_print="Estación "+str(revision[0])+" , ID="+str(revision[1])
                    print(str_print)
            case 8: 
                #Estacion con mayor temperatura promedio
                print("La estacion "+str(database.max_t_prom()[0][0])+" en el mes "+ 
                      str(database.max_t_prom()[0][1])+" del año "+str(database.max_t_prom()[0][2])+" regitro una temperatura promedio maxima de "+
                      str(round(database.max_t_prom()[0][3],2))+" °C"
                      )
            case 9: 
                #Distancia entre estaciones
                ID_estacion=input("Ingrese el ID de la estacion : ")
                while(int(ID_estacion) not in database.listar_id_estaciones()):
                    ID_estacion=input("ID no existe, ingrese un ID valido :")
                distancia=input("Ingrese el radio detro del cual quiere registrar estaciones:")
                lista=database.menor_distancia_dada(ID_estacion,distancia)
                print("Estacion|Distancia")
                for medicion in lista:
                    print(str(medicion[1])+"|"+str(medicion[0]))               
            case 10: 
                #Estaciones a menos de 2 punto a punto 
                ID_estacion=input("Ingrese el ID de la estacion : ")
                while(int(ID_estacion) not in database.listar_id_estaciones()):
                    ID_estacion=input("ID no existe, ingrese un ID valido :")              
                lista=database.get_pto_pto(ID_estacion) 
                print("Las estaciones a menos de 2 punto a punto son: ")
                for estacion in lista:
                    print("Estacion "+str(estacion))
            case 11: 
                database.cerrar_conexion()
                print("Cerrando...")
                break



 