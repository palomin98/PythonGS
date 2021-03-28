#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Carrera.py
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

# Importamos la clase competicion
from Clases.Competiciones.competicion import Competicion as compe

class Carrera(compe):
    """Creamos la clase que hereda de competicion"""

    def __init__(self, idCompeticion, nombre, distancia):
        """Constructor"""
        super().__init__(idCompeticion, nombre)
        self.distancia = distancia

    def get_distancia(self):
        """Get de distancia"""
        return self.distancia

    def set_distancia(self, distancia):
        """Set de distancia"""
        self.distancia = distancia

    def __str__(self):
        """Convierte todas el objeto a un string"""
        cadena = super().__str__() + ", " + str(self.distancia)
        return cadena
