#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  sportCompanyTraining.py
#
#  Copyright 2018 fp <fp@bachilllerato-07>
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

import random
import pedirdatos as datos

class SportCompanyTraining:

    def __init__(self, nombre):
        """Constructor"""
        self.nombre = nombre
        self.entrenadores = []
        self.alumnos = []
        self.trabajadores = []
        self.entrenamientos = []
        self.carrera = ""
        self.peso = ""
        self.salto = ""

    def get_nombre(self):
        """Get de nombre"""
        return self.nombre

    def set_nombre(self, nombre):
        """Set de nombre"""
        self.nombre = nombre

    def get_entrenadores(self):
        """Get de entrenadores"""
        return self.entrenadores

    def set_entrenadores(self, entrenadores):
        """Set de entrenadores"""
        self.entrenadores = entrenadores

    def get_alumnos(self):
        """Get de alumnos"""
        return self.alumnos

    def set_alumnos(self, alumnos):
        """Set de alumnos"""
        self.alumnos = alumnos

    def get_trabajadores(self):
        """Get de trabajadores"""
        return self.trabajadores

    def set_trabajadores(self, trabajadores):
        """Set de trabajadores"""
        self.trabajadores = trabajadores

    def get_entrenamientos(self):
        """Get de entrenamientos"""
        return self.entrenamientos

    def set_entrenamientos(self, entrenamientos):
        """Set de entrenamientos"""
        self.entrenamientos = entrenamientos

    def get_carrera(self):
        """Get de carrera"""
        return self.carrera

    def set_carrera(self, carrera):
        """Set de carrera"""
        self.carrera = carrera

    def get_peso(self):
        """Get de peso"""
        return self.peso

    def set_peso(self, peso):
        """Set de peso"""
        self.peso = peso

    def get_salto(self):
        """Get de salto"""
        return self.salto

    def set_salto(self, salto):
        """Set de salto"""
        self.salto = salto

    def agregarEntrenador(self, entrenador2):
        """Agregamos un nuevo entrenador"""
        # Declaramos e inicializamos variables
        encontrado = False

        # Recorremos todos los entrenadores
        for entrenador in self.entrenadores:
            # Si se encuentra uno igual
            if entrenador.get_dni() == entrenador2.get_dni():
                # Actualizamos variables
                encontrado = True

        # Si no se ha encontrado
        if not encontrado:
            # Agregamos un nuevo entrenador
            self.entrenadores.append(entrenador2)
            # Mensaje correcto
            print("Se ha agregado un nuevo entrenador.")
        else:
            # Mensaje de error
            print("Ya existe este entrenador.")

    def agregarAlumnos(self, alumno2):
        """Agregamos un nuevo alumno"""
        # Declaramos e inicializamos variables
        encontrado = False

        # Recorremos todos los alumnos
        for alumno in self.alumnos:
            # Si encontramos uno igual
            if alumno.get_dni() == alumno2.get_dni():
                # Actualizamos variables
                encontrado = True

        # Si no se ha encontrado
        if not encontrado:
            # Agregamos un nuevo alumno
            self.alumnos.append(alumno2)
            # Mensaje correcto
            print("Se ha agregado un nuevo alumno.")
        else:
            # Mensaje de error
            print("Ya existe este alumno.")

    def agregartrabajador(self, trabajador2):
        """Agreamos un nuevo trabajador"""
        # Declaramos e inicializamos variables
        encontrado = False

        # Recorremos todos los trabajadores
        for trabajador in self.trabajadores:
            # Si encontramos uno igual
            if trabajador.get_dni() == trabajador2.get_dni():
                # Actualizamos variables
                encontrado = True

        # Si no se ha encontrado
        if not encontrado:
            # Agregamos un nuevo trabajador
            self.trabajadores.append(trabajador2)
            # Mensaje correcto
            print("Se ha agregado un nuevo trabajador.")
        else:
            # Mensaje de error
            print("Ya existe este trabajador.")

    def agregarentrenamiento(self, entrenamiento2):
        """Añadimos un nuevo entrenamiento"""
        # Declaramos e inicializamos variables
        encontrado = False
        alumno2 = ""
        entrenador2 = ""
        pedirAlumnos = "s"
        encontradoEntrenador = False
        encontradoAlumno = False

        # Recorremos todos los entrenamientos
        for entrenamiento in self.entrenamientos:
            # Si se encuentra uno igual
            if entrenamiento.get_nombre() == entrenamiento2.get_nombre():
                # Actualizamos la variable
                encontrado = True

        print("Añadir entrenador: ")
        # Si no se ha encontrado
        if not encontrado:
            # Pedimos el entrenador para el entrenamiento
            entrenador2, encontradoEntrenador = self.anadirEntrenadorEntrenamiento()
            # Mientras no se encuentre el entrenador
            while not encontradoEntrenador:
                # Si no se encuentra
                if not encontradoEntrenador:
                    # Mensaje de error
                    print("No se ha añadido el entrenador al entrenamiento")
                # Pedimos el entrenador para el entrenamiento
                entrenador2, encontradoEntrenador = self.anadirEntrenadorEntrenamiento()

            # Si se encuentra el entrenador
            if encontradoEntrenador:
                # Agregamos el entrenador al entrenamiento
                entrenamiento2.set_entrenador(entrenador2)
                # Mensaje correcto
                print("Se ha añadido el entrenador al entrenamiento")
            else:
                # Mensaje de error
                print("No se ha añadido el entrenador al entrenamiento")

            print("Añadir alumnos: ")
            #Mientras que sea diferente a n
            while pedirAlumnos != "n":
                # Pedimos el alumno
                alumno2, encontradoAlumno = self.anadirAlumnoEntrenaCompe()
                # Si se encuentra
                if encontradoAlumno:
                    # Mensaje correcto
                    print("Se ha añadido el alumno al entrenamiento")
                    # Se agrega el alumno al entrenamiento
                    entrenamiento2.agregarAlumnos(alumno2)
                    # Preguntamos que si quiere algun alumno
                    pedirAlumnos = input("¿Quieres añadir un alumno mas?s/n")
                else:
                    # Mensaje de error
                    print("No se ha añadido el alumno al entrenamiento")

            # Añadimos el entrenamiento
            self.entrenamientos.append(entrenamiento2)
            # Mensaje correcto
            print("Se ha agregado un nuevo entrenamiento.")
        else:
            # Mensaje de error
            print("Ya existe este entrenamiento.")

    def borrarAlumno(self):
        """Borrar un alumno"""
        # Declaramos e inicializamos variables
        borrado = False
        dniAlumno = datos.pedirDni()

        # Recorro todos los alumnos
        for alumno in self.alumnos:
            # Si el dni es igual
            if dniAlumno == alumno.get_dni():
                # Borramos este alumno
                self.alumnos.remove(alumno)
                # Actualizamos variables
                borrado = True

        # Si se ha borrado
        if borrado:
            # Mensaje correcto
            print("Se ha borrado correctamente.")
        else:
            # Mensaje de error
            print("No se ha borrado correctamente.")

    def borrarEntrenador(self):
        """Borrar un entrenador"""
        # Declaramos e inicializamos variables
        borrado = False
        dniEntrenadores = datos.pedirDni()

        # Recorremos todos los entrenadores
        for entrenador in self.entrenadores:
            # Si el dni es igual
            if dniEntrenadores == entrenador.get_dni():
                # Se borra el entrenador
                self.entrenadores.remove(entrenador)
                # Actualizamos variable
                borrado = True

        # Si se ha borrado
        if borrado:
            # Mensaje correcto
            print("Se ha borrado correctamente.")
        else:
            # Mensaje de error
            print("No se ha borrado correctamente.")

    def borrarTrabajador(self):
        """Borrar un trabajador"""
        # Declaramos e inicializamos variables
        borrado = False
        dniTrabajador = datos.pedirDni()

        # Recorremos todos los trabajadores
        for trabajador in self.trabajadores:
            # Si el dni es igual
            if dniTrabajador == trabajador.get_dni():
                # Se borra el trabajador
                self.trabajadores.remove(trabajador)
                # Actualizamos variable
                borrado = True

        # Si se ha borrado
        if borrado:
            # Mensaje correcto
            print("Se ha borrado correctamente.")
        else:
            # Mensaje de error
            print("No se ha borrado correctamente.")

    def borrarEntrenamiento(self):
        """Borrar un entrenamiento"""
        # Declaramos e inicializamos variables
        borrado = False
        nombreEntrenamiento = input("Dame el nombre del Entrenamiento: ")

        # Recorremos todos los entrenamientos
        for entrenamiento in self.entrenamientos:
            # Si el nombre es igual
            if nombreEntrenamiento == entrenamiento.get_nombre():
                # Borramos el entrenamiento
                self.entrenamientos.remove(entrenamiento)
                # Actualizamos variable
                borrado = True

        # Si se ha borrado
        if borrado:
            # Mensaje correcto
            print("Se ha borrado correctamente.")
        else:
            # Mensaje de error
            print("No se ha borrado correctamente.")

    def anadirAlumnoEntrenaCompe(self):
        """Se añade un alumno a una competicion o un entrenamiento"""
        # Declaramos e inicializamos variables
        alumno2 = ""
        encontrado = False

        # Mientras no se encuentre
        while not encontrado:
            # Mensaje de informacion
            print("Escribe exit para salir.")
            # Pedimos el dni
            dniAlumno = datos.pedirDni()
            # Recorremos todos los alumnos
            for alumno in self.alumnos:
                # Si tienen igual dni
                if dniAlumno == alumno.get_dni():
                    # Actualizamos el objeto
                    alumno2 = alumno
                    # Actualizamos la varible
                    encontrado = True

            # Si ha escrito exit
            if dniAlumno == "exit":
                # Actualizamos la varible
                encontrado = True

            # Si no se encuentra
            if not encontrado:
                # Mensaje de error
                print("Este alumno no existe o no pertenece a esta competicion")

        return alumno2, encontrado

    def anadirEntrenadorEntrenamiento(self):
        """Añadimos un entrenador al entrenamiento"""
        # Declaramos e inicializamos variables
        entrenador2 = ""
        encontrado = False
        # Pedimos el dni
        dniEntrenador = datos.pedirDni()

        # Recorremos todos los entrenadores
        for entrenador in self.entrenadores:
            # Si el dni es igual
            if dniEntrenador == entrenador.get_dni():
                # Actualizamos el objeto
                entrenador2 = entrenador
                # Actualizamos la varible
                encontrado = True

        return entrenador2, encontrado

    def realizarCarrera(self, carrera):
        """Se realiza una competicion de carrera"""
        # Declaramos e inicializamos variables
        pedirAlumnos = "s"
        competicion = ""
        encontradoAlumno = False
        alumnosParticipantes = ""

        # Mientras que no pulse n
        while pedirAlumnos != "n":
            # Pedimos el alumno
            alumno2, encontradoAlumno = self.anadirAlumnoEntrenaCompe()
            # Cogemos el tipo de competicion del alumno
            competicion = alumno2.get_tipoCompeticion()
            # Si se ha encontrado y es de tipo carreras
            if encontradoAlumno and competicion == "carreras":
                # Mensaje correcto
                print("Se ha añadido el alumno a la competicion de carreras.")
                # Se añade el alumno
                carrera.agregarAlumnosParticipantes(alumno2)
                # Pregunta si quiere añadir uno mas
                pedirAlumnos = input("¿Quieres añadir un alumno mas?s/n")
            else:
                # Mensaje de error
                print("No se ha añadido el alumno a la competicion de carreras")

        # Ponemos la carrera
        self.set_carrera(carrera)

        # Cogemos los alumnos que participan
        alumnosParticipantes = carrera.get_alumnosParticipantes()
        # Genero un numero random
        num1 = random.randint(0, len(alumnosParticipantes))
        # Cogemos el alumno ganador al azar
        carrera.set_ganador(alumnosParticipantes[num1 - 1])
        # Mostramos quien ha ganador
        print("El ganador de la competicion con id ", carrera.get_idCompeticion(), " es ", alumnosParticipantes[num1 - 1].get_dni())

        # Lo guardamos una variable
        ganador = "El ganador de la competicion con id ", carrera.get_idCompeticion(), " es ", alumnosParticipantes[num1 - 1].get_dni()
        # Lo guarda en un fichero
        self.historialGanadores(ganador)

    def realizarPeso(self, peso):
        """Se realiza una competicion de peso"""
        # Declaramos e inicializamos variables
        pedirAlumnos = "s"
        competicion = ""
        encontradoAlumno = False

        # Mientras que no pulse n
        while pedirAlumnos != "n":
            # Pedimos el alumno
            alumno2, encontradoAlumno = self.anadirAlumnoEntrenaCompe()
            # Cogemos el tipo de competicion del alumno
            competicion = alumno2.get_tipoCompeticion()
            # Si se ha encontrado y es de tipo peso
            if encontradoAlumno and competicion == "peso":
                # Mensaje correcto
                print("Se ha añadido el alumno a la competicionde peso.")
                # Se añade el alumno
                peso.agregarAlumnosParticipantes(alumno2)
                # Pregunta si quiere añadir uno mas
                pedirAlumnos = input("¿Quieres añadir un alumno mas?s/n")
            else:
                # Mensaje de error
                print("No se ha añadido el alumno a la competicion de peso.")

        # Ponemos la competicion de peso
        self.set_peso(peso)

        # Cogemos los alumnos que participan
        alumnosParticipantes = peso.get_alumnosParticipantes()
        # Genero un numero random
        num1 = random.randint(0, len(alumnosParticipantes))
        # Cogemos el alumno ganador al azar
        peso.set_ganador(alumnosParticipantes[num1 - 1])
        # Mostramos quien ha ganador
        print("El ganador de la competicion con id ", peso.get_idCompeticion(), " es ", alumnosParticipantes[num1 - 1].get_dni())

        # Lo guardamos una variable
        ganador = "El ganador de la competicion con id ", peso.get_idCompeticion(), " es ", alumnosParticipantes[num1 - 1].get_dni()
        # Lo guarda en un fichero
        self.historialGanadores(ganador)

    def realizarSalto(self, salto):
        """Se realiza una competicion de salto"""
        # Declaramos e inicializamos variables
        pedirAlumnos = "s"
        competicion = ""
        encontradoAlumno = False

        # Mientras que no pulse n
        while pedirAlumnos != "n":
            # Pedimos el alumno
            alumno2, encontradoAlumno = self.anadirAlumnoEntrenaCompe()
            # Cogemos el tipo de competicion del alumno
            competicion = alumno2.get_tipoCompeticion()
            # Si se ha encontrado y es de tipo salto
            if encontradoAlumno and competicion == "salto":
                # Mensaje correcto
                print("Se ha añadido el alumno a la competicion de salto.")
                # Se añade el alumno
                salto.agregarAlumnosParticipantes(alumno2)
                # Pregunta si quiere añadir uno mas
                pedirAlumnos = input("¿Quieres añadir un alumno mas?s/n")
            else:
                # Mensaje de error
                print("No se ha añadido el alumno a la competicion de salto.")

        # Ponemos la competicion de salto
        self.set_salto(salto)

        # Cogemos los alumnos que participan
        alumnosParticipantes = salto.get_alumnosParticipantes()
        # Genero un numero random
        num1 = random.randint(0, len(alumnosParticipantes))
        # Cogemos el alumno ganador al azar
        salto.set_ganador(alumnosParticipantes[num1 - 1])
        # Mostramos quien ha ganador
        print("El ganador de la competicion con id ", salto.get_idCompeticion(), " es ", alumnosParticipantes[num1 - 1].get_dni())

        # Lo guardamos una variable
        ganador = "El ganador de la competicion con id ", salto.get_idCompeticion(), " es ", alumnosParticipantes[num1 - 1].get_dni()
        # Lo guarda en un fichero
        self.historialGanadores(ganador)

    def historialGanadores(self, ganador):
        """Añadimos un nuevo ganador"""
        try:
            # Abrimos el fichero en modo lectura
            victorias = open("vicorias.txt")
            guardar = ""
            # Leemos la primera linea
            leerVictorias = victorias.readline()
            # Mientras no llegue al final
            while leerVictorias != "":
                # Guardamos todas las victorias
                guardar = guardar + leerVictorias
                # Leemos la siguiente linea
                leerVictorias = victorias.readline()
        except:
            # Mensaje de error
            print("No hay victorias, se van a crear")

        # Lo abrimos en modo escritura
        victorias = open("vicorias.txt", "w")
        # Guardamos todos los ganadores y el ultimo
        victorias.write(str(guardar) + "\n" + str(ganador))

    def historialUnGanador(self):
        """Vemos el historial de un ganador"""
        # Declaramos e inicializamos variables
        jugadorId = input("Dame el id del jugador para ver su historial: ")
        victorias = open("vicorias.txt")
        encontrado = 0

        # Leemos la primera linea
        leerVictorias = victorias.readline()
        # Mientras que no llegue al final
        while leerVictorias != "":
            # Buscamos el jugador en la linea
            encontrado = leerVictorias.find(jugadorId)
            # Si se encuentra
            if encontrado != -1:
                # Muetra la linea
                print(leerVictorias)
            # Leemos la siguiente linea
            leerVictorias = victorias.readline()

    def verVictorias(self):
        """Vemos todas la victorias"""
        try:
            # Abrimos el fichero en modo lectura
            victorias = open("vicorias.txt")
            # Leemos la primera linea
            leerVictorias = victorias.readline()
            # Mientras que no llegue al final
            while leerVictorias != "":
                # Mostramos la linea
                print(leerVictorias)
                # Leemos la siguiente linea
                leerVictorias = victorias.readline()
        except:
            # Mensaje de error
            print("No hay victorias, se van a crear")

    def mostrarAlumnos(self):
        """Mostramos todos los alumnos"""
        cadena = "Alumnos: "
        for alumno in self.alumnos:
            cadena = cadena + "\n\t" + str(alumno)
        print(cadena)

    def mostrarEntrenadores(self):
        """Mostramos todos los entrenadores"""
        cadena = "Entrenadores: "
        for entrenador in self.entrenadores:
            cadena = cadena + "\n\t" + str(entrenador)
        print(cadena)

    def mostrarTrabajadores(self):
        """Mostramos todos los trabajadores"""
        cadena = "Trabajadores: "
        for trabajador in self.trabajadores:
            cadena = cadena + "\n\t" + str(trabajador)
        print(cadena)

    def mostrarEntrenamientos(self):
        """Mostramos todos los entrenamientos"""
        cadena = "Entrenamientos: "
        for entrenamiento in self.entrenamientos:
            cadena = cadena + "\n\t" + str(entrenamiento)
        print(cadena)

    def mostrarUnAlumno(self, dni):
        """Mostramos un alumno por dni"""
        cadena = "Alumno: "
        for alumno in self.alumnos:
            if dni.lower() == alumno.get_dni():
                cadena = cadena + "\n\t" + str(alumno)
        print(cadena)

    def mostrarUnEntrenador(self, dni):
        """Mostramos un entrenador por dni"""
        cadena = "Entrenadores: "
        for entrenador in self.entrenadores:
            if dni.lower() == entrenador.get_dni():
                cadena = cadena + "\n\t" + str(entrenador)
        print(cadena)

    def mostrarUnTrabajador(self, dni):
        """Mostramos un trabajador por dni"""
        cadena = "Trabajadores: "
        for trabajador in self.trabajadores:
            if dni.lower() == trabajador.get_dni():
                cadena = cadena + "\n\t" + str(trabajador)
        print(cadena)

    def mostrarUnEntrenamiento(self, nombre):
        """Mostramos un entrenamiento por nombre"""
        cadena = "Entrenamientos: "
        for entrenamiento in self.entrenamientos:
            if nombre == entrenamiento.get_nombre():
                cadena = cadena + "\n\t" + str(entrenamiento)
        print(cadena)

    def mostrarNumAlumnosTipo(self):
        """Se muestran los alumnos segun su tipo"""
        # Declaro e inicializo variables
        contarTipoCarrera = 0
        contarTipoSalto = 0
        contarTipoPeso = 0

        # Recorremos todos los alumnos
        for alumno in self.alumnos:
            # Depende de la competicion
            if alumno.get_tipoCompeticion() == "carreras":
                # Sumo un alumno mas
                contarTipoCarrera = contarTipoCarrera + 1
            elif alumno.get_tipoCompeticion() == "salto":
                # Sumo un alumno mas
                contarTipoSalto = contarTipoSalto + 1
            elif alumno.get_tipoCompeticion() == "peso":
                # Sumo un alumno mas
                contarTipoPeso = contarTipoPeso + 1

        # Muestro todos los tipos de alumnos
        print("Hay ", contarTipoCarrera, " Alumnos de carreras")
        print("Hay ", contarTipoSalto, " Alumnos de salto")
        print("Hay ", contarTipoPeso, " Alumnos de peso")

        # Comparo cual predomina mas y lo muestro
        if(contarTipoCarrera>=contarTipoSalto and contarTipoCarrera>=contarTipoPeso):
            print("Los alumnos de carreras predominan en nuestra empresa")
        if(contarTipoSalto>=contarTipoCarrera and contarTipoSalto>=contarTipoPeso):
            print("Los alumnos de salto predominan en nuestra empresa")
        if(contarTipoPeso>=contarTipoCarrera and contarTipoPeso>=contarTipoSalto):
            print("Los alumnos de peso predominan en nuestra empresa")

    def mostrarNumEntrenadoresTipo(self):
        """Se muestran los entrenadores segun su tipo"""
        # Declaro e inicializo variables
        contarTipoCarrera = 0
        contarTipoSalto = 0
        contarTipoPeso = 0

        # Recorremos todos los entrenadores
        for entrenador in self.entrenadores:
            # Depende de la competicion
            if entrenador.get_tipoEntrenador() == "carreras":
                # Sumo un entrenador mas
                contarTipoCarrera = contarTipoCarrera + 1
            elif entrenador.get_tipoEntrenador() == "salto":
                # Sumo un entrenador mas
                contarTipoSalto = contarTipoSalto + 1
            elif entrenador.get_tipoEntrenador() == "peso":
                # Sumo un entrenador mas
                contarTipoPeso = contarTipoPeso + 1

        # Muestro todos los tipos de entrenadores
        print("Hay ", contarTipoCarrera, " Entrenadores de carreras")
        print("Hay ", contarTipoSalto, " Entrenadores de salto")
        print("Hay ", contarTipoPeso, " Entrenadores de peso")

        # Comparo cual predomina mas y lo muestro
        if(contarTipoCarrera>=contarTipoSalto and contarTipoCarrera>=contarTipoPeso):
            print("Los Entrenadores de carreras predominan en nuestra empresa")
        if(contarTipoSalto>=contarTipoCarrera and contarTipoSalto>=contarTipoPeso):
            print("Los Entrenadores de salto predominan en nuestra empresa")
        if(contarTipoPeso>=contarTipoCarrera and contarTipoPeso>=contarTipoSalto):
            print("Los Entrenadores de peso predominan en nuestra empresa")

    def __str__(self):
        """Convierte todas el objeto a un string"""

        cadena = str(self.nombre) + "\nEntrenadores: "
        for entrenador in self.entrenadores:
            cadena = cadena + "\n\t" + str(entrenador)

        cadena = cadena + "\nTrabajadores"
        for trabajador in self.trabajadores:
            cadena = cadena + "\n\t" + str(trabajador)

        cadena = cadena + "\nAlumnos"
        for alumno in self.alumnos:
            cadena = cadena + "\n\t" + str(alumno)

        cadena = cadena + "\nEntrenamientos"
        for entrenamiento in self.entrenamientos:
            cadena = cadena + "\n\t" + str(entrenamiento)

        cadena = cadena + "\nCarrera: " + str(self.carrera) + "\nPeso: " + str(self.peso) + "\nSalto: " + str(self.salto)
        return cadena