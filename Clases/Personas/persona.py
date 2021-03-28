#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  personas.py
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

class Persona:

    def __init__(self, nombre, dni):
        """Constructor"""
        self.nombre = nombre
        self.dni = dni

    def get_nombre(self):
        """Get de nombre"""
        return self.nombre

    def set_nombre(self, nombre):
        """Set de nombre"""
        self.nombre = nombre

    def get_dni(self):
        """Get de dni"""
        return self.dni

    def set_dni(self, dni):
        """Set de dni"""
        self.dni = dni

    def __str__(self):
        """Convierte todas el objeto a un string"""
        cadena = str(self.nombre) + ", " + str(self.dni)
        return cadena
