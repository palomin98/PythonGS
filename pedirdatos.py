# -*- coding: utf-8 -*-

from Clases.Competiciones.carrera import Carrera as carrera
from Clases.Competiciones.peso import Peso as peso
from Clases.Competiciones.salto import Salto as salto
from Clases.Personas.Alumno import Alumno as alumno
from Clases.Personas.entrenador import Entrenador as entrenador
from Clases.Personas.trabajador import Trabajador as trabajador

def datosEntrenador():
    """Pedimos los datos del entrenador"""
    # Pido los datos
    dniEntrenador = pedirDni()
    nombreEntrenador = input("Dame el nombre del entrenador: ")

    # Declaro e inicializo variables
    tipoCompeticionEntrenador = ""

    # Mientras el tipo de comprecion sea diferente a carreras, peso, salto
    while tipoCompeticionEntrenador != "carreras" and tipoCompeticionEntrenador != "peso" and tipoCompeticionEntrenador != "salto":
        # Pido los datos
        tipoCompeticionEntrenador = input("Dame la competicion del entrenador: ")
        # Lo paso a minusculas
        tipoCompeticionEntrenador = tipoCompeticionEntrenador.lower()

        # Si el tipo de comprecion sea diferente a carreras, peso, salto
        if tipoCompeticionEntrenador != "carreras" and tipoCompeticionEntrenador != "peso" and tipoCompeticionEntrenador != "salto":
            # Mensaje de error
            print("No existe esta competicion")

    # Creo un entrenador
    mister = entrenador(nombreEntrenador, dniEntrenador, tipoCompeticionEntrenador)

    return mister

def datosAlumnos():
    """Pedimos los datos del alumnos"""
    # Declaro e inicializo variables
    tipoCompeticionAlumno = ""

    # Pido los datos
    dniAlumno = pedirDni()
    nombreAlumno = input("Dame el nombre del alumno: ")

    # Mientras el tipo de comprecion sea diferente a carreras, peso, salto
    while tipoCompeticionAlumno != "carreras" and tipoCompeticionAlumno != "peso" and tipoCompeticionAlumno != "salto":
        # Pido los datos
        tipoCompeticionAlumno = input("Dame la competicion del alumno: ")
        # Lo paso a minusculas
        tipoCompeticionAlumno = tipoCompeticionAlumno.lower()

        # Si el tipo de comprecion sea diferente a carreras, peso, salto
        if tipoCompeticionAlumno != "carreras" and tipoCompeticionAlumno != "peso" and tipoCompeticionAlumno != "salto":
            # Mensaje de error
            print("No existe esta competicion")

    # Creo un alumno
    alum = alumno(nombreAlumno, dniAlumno, tipoCompeticionAlumno)

    return alum

def datosTrabajador():
    """Pedimos datos del trabajador"""
    # Pido los datos
    dniTrabajador = pedirDni()
    nombreTrabajador = input("Dame el nombre del trabajador: ")
    tipoTrabajador = input("Dame el tipo del trabajador: ")

    # Creo un entrenador
    currante = trabajador(nombreTrabajador, dniTrabajador, tipoTrabajador)

    return currante

def datosCarrera():
    """Pedimos la carrera"""
    # Pido los datos
    idCarrera = input("Id de la carrera: ")
    nombreCarrera = input("Nombre de la carrera: ")
    distaciaCarrera = input("Distancia de la carrera: ")

    #Creo un objeto de tipo carrera y la actualizo
    run = carrera(idCarrera, nombreCarrera, distaciaCarrera)

    return run

def datosPeso():
    """Pedimos los dattos de una competicion de peso"""
    # Pido los datos
    idPeso = input("Id de la competicion de peso: ")
    nombrePeso = input("Nombre de la competicion de peso: ")
    tipoPeso = input("Dame el tipo de peso que se va a utilizar:")
    pesoTotal = input("Dame el peso de la competicion: ")

    #Creo un objeto de tipo carrera y la actualizo
    pesos = peso(idPeso, nombrePeso, tipoPeso, pesoTotal)

    return pesos

def datosSalto():
    """Pedimos datos de la competicion de salto"""
    # Pido los datos
    idSalto = input("Id de la competicion de salto: ")
    nombreSalto = input("Nombre de la competicion de salto: ")
    tipoSalto = input("Tipo de la competicion de salto: ")

    #Creo un objeto de tipo carrera y la actualizo
    jump = salto(idSalto, nombreSalto, tipoSalto)

    return jump


def pedirDni():
    """Pedimos los datos del dni"""
    # Declaro e inicializo variables
    dni = False
    dniNum = ""
    dniLetr = ""

    # Mientras el dni no sea correcto
    while not dni:
        # Pido el numero del dni
        dniNum = dniNumero()
        # Pido la letra del dni
        dniLetr = dniLetra()

        # Compruebo al dni
        dni = comprobarDni(dniNum, dniLetr)

        # Si no es correcto
        if not dni:
            # Mensaje de error
            print("El dni no es real")

    # Junto el numero y la letra del dni
    dni = str(dniNum) + dniLetr

    return dni


def dniNumero():
    """Comprobamos el dni"""
    # Declaro e inicializo variables
    dniNumero = ""

    # Mientras es diferente a 8
    while len(dniNumero) != 8:
        # Pido los datos
        dniNumero = input("Dame el numero del dni del miembro:")

        # Si es diferente a 8
        if len(dniNumero) != 8:
            # Mensaje de error
            print("No es un numero correcto. ")

    return int(dniNumero)


def dniLetra():
    """Compobamos la letra"""
    # Declaro e inicializo variables
    dniLetra = ""

    # Mientras la letra sea un numero de 0 al 9
    while len(dniLetra) != 1 or dniLetra == "0" or dniLetra == "1" or dniLetra == "2" or dniLetra == "3" or dniLetra == "4" or dniLetra == "5" or dniLetra == "6" or dniLetra == "7" or dniLetra == "8" or dniLetra == "9":
        dniLetra = input("Dame la letra del dni del miembro:")

        # Si la letra sea un numero de 0 al 9
        if len(dniLetra) != 1 or dniLetra == "0" or dniLetra == "1" or dniLetra == "2" or dniLetra == "3" or dniLetra == "4" or dniLetra == "5" or dniLetra == "6" or dniLetra == "7" or dniLetra == "8" or dniLetra == "9":
            # Mensaje de error
            print("No es una letra correcto. ")

        #Convierto la letra a minnusculas
        dniLetra = dniLetra.lower()

    return dniLetra


def comprobarDni(dniNum, dniLetra):
    """Comprobamos si el dni es correcto"""
    # Declaro e inicializo variables
    resto = 0
    correcto = False

    # Hago el resto del dni para comprobarlo
    resto = dniNum % 23

    # Copruebo que la letra dni es correcta
    if resto == 0:
        correcto = dniLetra == "t"
    elif resto == 1:
        correcto = dniLetra == "r"
    elif resto == 2:
        correcto = dniLetra == "w"
    elif resto == 3:
        correcto = dniLetra == "a"
    elif resto == 4:
        correcto = dniLetra == "g"
    elif resto == 5:
        correcto = dniLetra == "m"
    elif resto == 6:
        correcto = dniLetra == "y"
    elif resto == 7:
        correcto = dniLetra == "f"
    elif resto == 8:
        correcto = dniLetra == "p"
    elif resto == 9:
        correcto = dniLetra == "d"
    elif resto == 10:
        correcto = dniLetra == "x"
    elif resto == 11:
        correcto = dniLetra == "b"
    elif resto == 12:
        correcto = dniLetra == "n"
    elif resto == 13:
        correcto = dniLetra == "j"
    elif resto == 14:
        correcto = dniLetra == "z"
    elif resto == 15:
        correcto = dniLetra == "s"
    elif resto == 16:
        correcto = dniLetra == "q"
    elif resto == 17:
        correcto = dniLetra == "v"
    elif resto == 18:
        correcto = dniLetra == "h"
    elif resto == 19:
        correcto = dniLetra == "l"
    elif resto == 20:
        correcto = dniLetra == "c"
    elif resto == 21:
        correcto = dniLetra == "k"
    elif resto == 22:
        correcto = dniLetra == "e"

    return correcto