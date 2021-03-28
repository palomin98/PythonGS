#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  menus.py
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

class menus:

    def menuCargar():
        """Menu nada mas iniciar que pregunta si carga o no los datos"""
        print("¿Quieres cargar los datos?")
        print("\t1. Si.")
        print("\t2. Empezar de nuevo.")

    def menuSalir():
        """Menu que sale antes de cerrar la aplicacion para guardar o no los datos"""
        print("¿Quieres salir guardando los datos?")
        print("\t1. Salir guardando.")
        print("\t2. Salir sin guardar.")

    def menuInicial():
        """Menu inicial del programa"""
        print("Menu inicial:")
        print("\t0. Salir.")
        print("\t1. Alumnos.")
        print("\t2. Entrenadores.")
        print("\t3. Trabajadores.")
        print("\t4. Entrenamientos.")
        print("\t5. Competiciones.")
        print("\t6. Ver toda la empresa.")
        print("\t7. Enunciado.")

    def menuAlumnos():
        """Menu de alumnos"""
        print("Menu de Alumnos:")
        print("\t0. Atras.")
        print("\t1. Añadir Alumno.")
        print("\t2. Borrar Alumno.")
        print("\t3. Mostrar Alumnos.")
        print("\t4. Mostrar un Alumno.")
        print("\t5. Mostrar el numero de alumnos por competicion.")

    def menuEntrenadores():
        """Menu de entrenadores"""
        print("Menu de Entrenadores:")
        print("\t0. Atras.")
        print("\t1. Añadir Entrenador.")
        print("\t2. Borrar Entrenador.")
        print("\t3. Mostrar Entrenadores.")
        print("\t4. Mostrar un Entrenador.")
        print("\t5. Mostrar el numero de Entrenadores por competicion.")

    def menuTrabajadores():
        """Menu de trabajadores"""
        print("Menu de Trabajadores:")
        print("\t0. Atras.")
        print("\t1. Añadir Trabajador.")
        print("\t2. Borrar Trabajador.")
        print("\t3. Mostrar Trabajadores.")
        print("\t4. Mostrar un Trabajador.")

    def menuEntrenamientos():
        """Menu de entrenamietnos"""
        print("Menu de Entrenamientos:")
        print("\t0. Atras.")
        print("\t1. Añadir Entrenamiento.")
        print("\t2. Borrar Entrenamiento.")
        print("\t3. Mostrar Entrenamientos.")
        print("\t4. Mostrar un Entrenamiento.")

    def menuCompeticiones():
        """Menu de competiciones"""
        print("Menu de Competiciones:")
        print("\t0. Atras.")
        print("\t1. Realizar competicion de carreras.")
        print("\t2. Realizar competicion de peso.")
        print("\t3. Realizar competicion de salto.")
        print("\t4. Ver el historial de los ganadores.")
        print("\t5. Ver el historial un de los ganadores.")