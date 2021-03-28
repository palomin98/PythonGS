#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Competicion.py
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

class Competicion:

    def __init__(self, idCompeticion, nombre):
        """Constructor"""
        self.nombre = nombre
        self.idCompeticion = idCompeticion
        self.alumnosParticipantes = []
        self.ganador = ""

    def get_nombre(self):
        """Get de nombre"""
        return self.nombre

    def set_nombre(self, nombre):
        """Set de nombre"""
        self.nombre = nombre

    def get_idCompeticion(self):
        """Get de idCompeticion"""
        return self.idCompeticion

    def set_idCompeticion(self, idCompeticion):
        """Set de idCompeticion"""
        self.idCompeticion = idCompeticion

    def get_alumnosParticipantes(self):
        """Get de alumnosParticipantes"""
        return self.alumnosParticipantes

    def set_alumnosParticipantes(self, alumnosParticipantes):
        """Set de alumnosParticipantes"""
        self.alumnosParticipantes = alumnosParticipantes

    def agregarAlumnosParticipantes(self, alumnosParticipantes):
        """Añadimos alumnos a la competicion"""
        self.alumnosParticipantes.append(alumnosParticipantes)

    def get_ganador(self):
        """Get de ganador"""
        return self.ganador

    def set_ganador(self, ganador):
        """Set de ganador"""
        self.ganador = ganador

    def __str__(self):
        """Convierte todas el objeto a un string"""
        cadena = str(self.nombre) + ", " + str(self.idCompeticion)
        for i in self.alumnosParticipantes:
            cadena = cadena + ", " + str(i)
        return cadena