#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  tester.py
#
#  Copyright 2018 Ruben Palomo <Ruben Palomo@RUBENCOMPU>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#

from Ejecucion.guardarcargar import GuardarCargar as guardar
from Clases.Entrenamientos.entrenamiento import Entrenamiento as entrena
from Ejecucion.SportCompanyTraining import SportCompanyTraining as compa
from Ejecucion.menus import menus as menu
import pedirdatos as datos

if __name__ == '__main__':

    # Variables de los menus
    respuestaMenuCargar = "0"
    respuestaMenuSalir = "0"
    respuestaMenuInicial = "1"
    respuestaMenuAlumnos = "1"
    respuestaMenuEntrenadores = "1"
    respuestaMenuTrabajadores = "1"
    respuestaMenuEntrenamientos = "1"
    respuestaMenuCompeticiones = "1"

    # Creamos una nueva empresa
    sport = compa("Empresa")

    # Menu de carga
    while respuestaMenuCargar != "1" and respuestaMenuCargar != "2":
        # Mostramos el menu
        menu.menuCargar()
        # Preguntamos al usuario
        respuestaMenuCargar = input("Desea cargar los datos: ")

        # Si la respuesta es 1
        if respuestaMenuCargar == "1":
            respuestaMenuCargar = "1"
            # Cargamos los datos
            sport = guardar.cargar_datos()
        # Si la respuesta es 2
        elif respuestaMenuCargar == "2":
            respuestaMenuCargar = "2"
        else:
            # Mensaje de error
            print("Opcion incorrecta.")

    # Menu inicial
    while respuestaMenuInicial != "0":
        # Mostramos el menu
        menu.menuInicial()
        respuestaMenuInicial = input("Elige una ocion: ")

        # Menu de salida
        if respuestaMenuInicial == "0":
            respuestaMenuInicial = "0"
            while respuestaMenuSalir != "1" and respuestaMenuSalir != "2":
                # Mostramos el menu
                menu.menuSalir()
                # Preguntamos al usuario
                respuestaMenuSalir = input("Elige una ocion: ")
                # Si la opcion es 1
                if respuestaMenuSalir == "1":
                    respuestaMenuSalir = "1"
                    print ()
                    print ("Salir")
                    # Llamamos a metodo que guarda los datos en binario
                    guardar.guardar_datos(sport)
                    print ()
                # Si la opcion es 2
                elif respuestaMenuSalir == "2":
                    respuestaMenuSalir = "2"
                    print ()
                    print ("Salir")
                print("Has salido del programa.")

        # Menu de alumnos
        elif respuestaMenuInicial == "1":
            respuestaMenuInicial = "1"
            while respuestaMenuAlumnos != "0":
                # Mostramos el menu
                menu.menuAlumnos()
                # Preguntamos al usuario
                respuestaMenuAlumnos = input("Elige una ocion: ")
                # Si la respuesta es 0
                if respuestaMenuAlumnos == "0":
                    respuestaMenuAlumnos = "0"
                    print("Atras.")

                # Si la respuesta es 1
                elif respuestaMenuAlumnos == "1":
                    respuestaMenuAlumnos = "1"
                    print("Añadir un nuevo alumno: ")
                    # Creo un alumno
                    alum = datos.datosAlumnos()
                    # Inserto el alumno
                    sport.agregarAlumnos(alum)

                # Si la respuesta es 2
                elif respuestaMenuAlumnos == "2":
                    respuestaMenuAlumnos = "2"
                    print("Borrar un alumno: ")
                    # Llamamos al metodo para borrar un alumno
                    sport.borrarAlumno()

                # Si la respuesta es 3
                elif respuestaMenuAlumnos == "3":
                    respuestaMenuAlumnos = "3"
                    print("Ver alumnos: ")
                    try:
                        # Llamamos al metodo para mostrar todos los alumnos
                        sport.mostrarAlumnos()
                    except AttributeError:
                        # Mensaje de error
                        print("Ups... No hay ningun alumno.")

                # Si la respuesta es 4
                elif respuestaMenuAlumnos == "4":
                    print("Ver un alumno: ")
                    try:
                        # Declaramos e inicializamos variable
                        correcto = False
                        # Recorro mientras no sea correcto
                        while not correcto:
                            # Pido el dni
                            dni = input("Dame el DNI del alumno: ")
                            # Compruebo el dni
                            if len(dni) == 9:
                                # Actualizo variable
                                correcto = True
                            else:
                                # Mensaje de error
                                print("Dni erroneo.")
                        # Mostamos el alumno por dni
                        sport.mostrarUnAlumno(dni)
                    except AttributeError:
                        # Mensaje de error
                        print("Ups... No hay ningun alumno.")

                # Si la respuesta es 5
                elif respuestaMenuAlumnos == "5":
                    respuestaMenuAlumnos = "5"
                    # Llamamos al metodo te muestra todos los alumnos por tipo
                    sport.mostrarNumAlumnosTipo()

                else:
                    # Mensaje de error
                    print("Opcion incorrecta.")

        # Menu de Entrenadores
        elif respuestaMenuInicial == "2":
            respuestaMenuInicial = "2"

            # Mientras que sea diferente a 0
            while respuestaMenuEntrenadores != "0":
                # Mostramos el menu
                menu.menuEntrenadores()
                # Preguntamos al usuario
                respuestaMenuEntrenadores = input("Elige una ocion: ")
                # Si la respuesta es 0
                if respuestaMenuEntrenadores == "0":
                    respuestaMenuEntrenadores = "0"
                    print("Atras.")

                # Si la respuesta es 1
                elif respuestaMenuEntrenadores == "1":
                    respuestaMenuEntrenadores = "1"
                    print("Añadir un nuevo entrenador: ")
                    # Creo un entrenador
                    mister = datos.datosEntrenador()
                    # Inserto el entrenador
                    sport.agregarEntrenador(mister)

                # Si la respuesta es 2
                elif respuestaMenuEntrenadores == "2":
                    respuestaMenuEntrenadores = "2"
                    print("Borrar un entrenador: ")
                    # Llamamos al metodo que te borrar el entrenador
                    sport.borrarEntrenador()

                # Si la respuesta es 3
                elif respuestaMenuEntrenadores == "3":
                    respuestaMenuEntrenadores = "3"
                    print("Ver entrenadores: ")
                    try:
                        # Llamamos al metodo que te muestra todos los entrena
                        sport.mostrarEntrenadores()
                    except AttributeError:
                        # Mensaje de error
                        print("Ups... No hay ningun entrenador.")

                # Si la respuesta es 4
                elif respuestaMenuEntrenadores == "4":
                    respuestaMenuEntrenadores = "4"
                    print("Ver un entrenador: ")
                    try:
                        # Declaramos e inicializamos variable
                        correcto = False
                        # Mientras no sea correcto
                        while not correcto:
                            # Pido el dni
                            dni = input("Dame el DNI del entrenador: ")
                            # Compruebo el dni
                            if len(dni) == 9:
                                # Actualizo variable
                                correcto = True
                            else:
                                # Mensaje de error
                                print("Dni erroneo.")
                        # Llamo al metodo para mostrar el entrenador
                        sport.mostrarUnEntrenador(dni)
                    except AttributeError:
                        # Mensaje de error
                        print("Ups... No hay ningun entrenador.")

                # Si la respuesta es 5
                elif respuestaMenuEntrenadores == "5":
                    respuestaMenuEntrenadores = "5"
                    # Mostramos todos los entrenadores por tipo
                    sport.mostrarNumEntrenadoresTipo()

                else:
                    # Mensaje de error
                    print("Opcion incorrecta.")

        # Menu de Trabajadores
        elif respuestaMenuInicial == "3":
            respuestaMenuInicial = "3"

            # Mientras que la respuesta sea diferente a 0
            while respuestaMenuTrabajadores != "0":
                # Mostramos el menu
                menu.menuTrabajadores()
                # Preguntamos al usuario
                respuestaMenuTrabajadores = input("Elige una ocion: ")

                # Si la respuesta es 0
                if respuestaMenuTrabajadores == "0":
                    respuestaMenuTrabajadores = "0"
                    print("Atras.")

                # Si la respuesta es 1
                elif respuestaMenuTrabajadores == "1":
                    respuestaMenuTrabajadores = "1"
                    print("Añadir un nuevo trabajador: ")
                    # Creo un trabajador
                    currante = datos.datosTrabajador()
                    # Inserto el trabajador
                    sport.agregartrabajador(currante)

                # Si la respuesta es 2
                elif respuestaMenuTrabajadores == "2":
                    respuestaMenuTrabajadores = "2"
                    print("Borrar un trabajador: ")
                    # Llamamos al metodo que te borra un trabajador
                    sport.borrarTrabajador()

                # Si la respuesta es 3
                elif respuestaMenuTrabajadores == "3":
                    respuestaMenuTrabajadores = "3"
                    print("Ver trabajadores: ")
                    try:
                        # Llamamos al metodo que muestra todos los trabajadores
                        sport.mostrarTrabajadores()
                    except AttributeError:
                        # Mensaje de error
                        print("Ups... No hay ningun trabajador.")

                # Si la respuesta es 4
                elif respuestaMenuTrabajadores == "4":
                    respuestaMenuTrabajadores = "4"
                    print("Ver un trabajador: ")
                    try:
                        # Declaramos e inicializamos variable
                        correcto = False
                        # Mientras no sea correcto
                        while not correcto:
                            # Preguntamos el dni
                            dni = input("Dame el DNI del trabajador: ")
                            # Comprobamos el dni
                            if len(dni) == 9:
                                # Actualizamos variable
                                correcto = True
                            else:
                                # Mensaje de error
                                print("Dni erroneo.")
                        sport.mostrarUnTrabajador(dni)
                    except AttributeError:
                        # Mensaje de error
                        print("Ups... No hay ningun trabajador.")

                else:
                    # Mensaje de error
                    print("Opcion incorrecta.")

        # Menu de Entrenamientos
        elif respuestaMenuInicial == "4":
            respuestaMenuInicial = "4"
            # Mientras que la respuesta sea diferente a 0
            while respuestaMenuEntrenamientos != "0":
                menu.menuEntrenamientos()
                # Preguntamos al usuario
                respuestaMenuEntrenamientos = input("Elige una ocion: ")
                if respuestaMenuEntrenamientos == "0":
                    respuestaMenuEntrenamientos = "0"
                    print("Atras.")

                # Si la respuesta es 1
                elif respuestaMenuEntrenamientos == "1":
                    respuestaMenuEntrenamientos = "1"
                    print("Añadir un nuevo entrenamiento: ")
                    # Pido los datos
                    nombreEntrenamiento = input("Dame el nombre del entrenamiento: ")
                    # Creo un entrenador
                    sesion = entrena(nombreEntrenamiento)
                    # Inserto el entrenador
                    sport.agregarentrenamiento(sesion)

                # Si la respuesta es 2
                elif respuestaMenuEntrenamientos == "2":
                    respuestaMenuEntrenamientos = "2"
                    print("Borrar un entrenamiento: ")
                    # Llamamos al metodo que te borra el entrenamiento
                    sport.borrarEntrenamiento()

                # Si la respuesta es 3
                elif respuestaMenuEntrenamientos == "3":
                    respuestaMenuEntrenamientos = "3"
                    print("Ver entrenamientos: ")
                    try:
                        # Llamamos al metodo para mostrar todos los entreneas
                        sport.mostrarEntrenamientos()
                    except AttributeError:
                        # Mensaje de error
                        print("Ups... No hay ningun entrenamiento.")

                # Si la respuesta es 4
                elif respuestaMenuEntrenamientos == "4":
                    respuestaMenuEntrenamientos = "4"
                    print("Ver un entrenamiento: ")
                    try:
                        # Pedimos el nombre del entrenamiento
                        nombre = input("Dame el nombre del entrenamiento: ")
                        # Mostramos el entrenamiento por nombre
                        sport.mostrarUnEntrenamiento(nombre)
                    except AttributeError:
                        # Mensaje de error
                        print("Ups... No hay ningun entrenamiento.")

                else:
                    # Mensaje de error
                    print("Opcion incorrecta.")

        # Menu de Competiciones
        elif respuestaMenuInicial == "5":
            respuestaMenuInicial = "5"
            # Mientras que la respuesta sea diferente a 0
            while respuestaMenuCompeticiones != "0":
                menu.menuCompeticiones()
                # Preguntamos al usuario
                respuestaMenuCompeticiones = input("Elige una ocion: ")

                # Si la respuesta es 0
                if respuestaMenuCompeticiones == "0":
                    respuestaMenuCompeticiones = "0"
                    print("Atras.")

                # Si la respuesta es 1
                elif respuestaMenuCompeticiones == "1":
                    respuestaMenuCompeticiones = "1"
                    try:
                        print("Realizar competicion de carreras: ")
                        #Creo un objeto de tipo carrera y la actualizo
                        run = datos.datosCarrera()
                        # Llamo al metodo que realiza la carrera
                        sport.realizarCarrera(run)
                    except AttributeError:
                        # Mensaje de error
                        print("Ups... No hay ningun alumno.")

                # Si la respuesta es 2
                elif respuestaMenuCompeticiones == "2":
                    respuestaMenuCompeticiones = "2"
                    try:
                        print("Realizar competicion de peso: ")
                        #Creo un objeto de tipo carrera y la actualizo
                        pesos = datos.datosPeso()
                        # Llamo al metodo que realiza la compe de peso
                        sport.realizarPeso(pesos)
                    except AttributeError:
                        # Mensaje de error
                        print("Ups... No hay ningun alumno.")

                # Si la respuesta es 3
                elif respuestaMenuCompeticiones == "3":
                    respuestaMenuCompeticiones = "3"
                    try:
                        print("Realizar competicion de salto: ")
                        #Creo un objeto de tipo carrera y la actualizo
                        jump = datos.datosSalto()
                        # Llamo al metodo que realiza la compe de salto
                        sport.realizarSalto(jump)
                    except AttributeError:
                        # Mensaje de error
                        print("Ups... No hay ningun alumno.")

                # Si la respuesta es 4
                elif respuestaMenuCompeticiones == "4":
                    respuestaMenuCompeticiones = "4"
                    print("Ver el historial de los ganadores.")
                    # Llamo al metodo que te muestra todas las victorias
                    sport.verVictorias()

                # Si la respuesta es 5
                elif respuestaMenuCompeticiones == "5":
                    respuestaMenuCompeticiones = "5"
                    print("Ver el historial de un ganador.")
                    # Llamo al metodo que muestra las victorias de un jugador
                    sport.historialUnGanador()

                else:
                    # Mensaje de error
                    print("Opcion incorrecta.")

        # Si la respuesta es 6
        elif respuestaMenuInicial == "6":
            respuestaMenuInicial = "6"
            # Mostramos todo el programa
            print(sport)

        # Si la respuesta es 7
        elif respuestaMenuInicial == "7":
            respuestaMenuInicial = "7"
            # Mostramos el enunciado
            print("Una empresa de deportes me pidio una aplicacion en python para que pudiera manejar sus alumnos,")
            print("sus trabajadores, sus competiciones y entrenamientos, con esta informacion realice el programa")
            print("para llevar una empresa, donde se guarda en un fichero binario cuando se sale y en uno txt las victorias.")

        else:
            # Mensaje de error
            print("Opcion incorrecta.")