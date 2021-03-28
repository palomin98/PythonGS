#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Entrenador.py
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

# Importamos la clase Persona
from Clases.Personas.persona import Persona as persona

class Entrenador(persona):
    """Creamos la clase que hereda de Persona"""

    def __init__(self, nombre, dni, tipoEntrenador):
        """Constructor"""
        super().__init__(nombre, dni)
        self.tipoEntrenador = tipoEntrenador

    def get_tipoEntrenador(self):
        """Get de tipoEntrenador"""
        return self.tipoEntrenador

    def set_tipoEntrenador(self, tipoEntrenador):
        """Set de tipoEntrenador"""
        self.tipoEntrenador = tipoEntrenador

    def __str__(self):
        """Convierte todas el objeto a un string"""
        cadena = super().__str__() + ", " + str(self.tipoEntrenador)
        return cadena
