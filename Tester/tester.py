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
from Clases.Competiciones.Carrera import Carrera as carrera
from Clases.Competiciones.Peso import Peso as peso
from Clases.Competiciones.Salto import Salto as salto
from Clases.Personas.Alumno import Alumno as alumno
from Clases.Personas.Entrenador import Entrenador as entrenador
from Clases.Personas.Trabajador import Trabajador as trabajador
from Clases.Entrenamientos.Entrenamiento import Entrenamiento as entrena

if __name__ == '__main__':

    ca1 = carrera(1, "Carrera1", 200)
    print(ca1)

    pe1 = peso(2, "Peso1", 400, 200)
    print(pe1)

    sa1 = salto(3, "Salto1", 500)
    print(sa1)

    al1 = alumno("Ruben", "393333333", "Carrera")
    print(al1)

    en1 = entrenador("Alex", "393343333", "Peso")
    print(en1)

    tra1 = trabajador("Nalo", "393335333", "Informatico")
    print(tra1)

    ent1 = entrena("GTM", en1)
    ent1.agregarAlumnos(al1)
    ent1.agregarAlumnos(al1)
    print(ent1)

