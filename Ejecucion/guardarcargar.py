# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import pickle
#import os.path as path

class GuardarCargar():
    def cargar_datos():
        """Cargamos datos"""
        try:
            # Abrimos el fichero en modo lectura
            with open("sport.dat", "rb") as f:
                # Mostamos un mensaje
                print('Cargado')
                # Devolvemos lo cargado
                return pickle.load(f)

        except (OSError, IOError) as e:
            # Mensaje
            print(e)
            return dict()


    def guardar_datos(sport):
        """Guardamos datos"""
        # Abrimos el fichero en modo escritura
        with open("sport.dat", "wb") as f:
            # Guardamos los datos
            pickle.dump(sport, f)
            # Mostamos un mensaje
            print('Guardado')
        return