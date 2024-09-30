import random

# Clase que crea unidades 
class Unidad:
    def __init__(self, nombre, salud, ataque, defensa):
        self.nombre = nombre
        self.salud = salud
        self.ataque = ataque
        self.defensa = defensa

    #vida de la unidad
    def esta_vivo(self):
        return self.salud > 0

#-----------------------------------------------------------------------------------------------

#UNIDADES

#Clase arquero
class Arquero(Unidad):
    def __init__(self):
        super().__init__(nombre="Arquero", salud=100, ataque=10, defensa=5)

#Clase infanteria
class Infanteria(Unidad):
    def __init__(self):
        super().__init__(nombre="Infanteria", salud=150, ataque=15, defensa=10)

#Clase caballeria
class Caballeria(Unidad):
    def __init__(self):
        super().__init__(nombre="Caballeria", salud=200, ataque=20, defensa=15)

#-----------------------------------------------------------------------------------------------

#Ejercito

class Ejercito:
    def __init__(self, nombre):
        self.nombre = nombre
        self.unidades = []

    def reclutar_unidad(self, unidad):
        self.unidades.append(unidad)

    def tiene_unidades(self):
        return any([unidad.esta_vivo() for unidad in self.unidades])

#-----------------------------------------------------------------------------------------------

#Funciones de combate

def combate(unidad1, unidad2):
    print(f"{unidad1.nombre} ({unidad1.salud} HP) vs {unidad2.nombre} ({unidad2.salud} HP)")
    #unidad 1 ataca a unidad 2
    daño1 = max(0, unidad1.ataque - unidad2.defensa)
    unidad2.salud -= daño1
    print(f"{unidad1.nombre} hace {daño1} de daño a {unidad2.nombre}")

    if unidad2.esta_vivo():
        #unidad 2 ataca a unidad 1
        daño2 = max(0, unidad2.ataque - unidad1.defensa)
        unidad1.salud -= daño2
        print(f"{unidad2.nombre} hace {daño2} de daño a {unidad1.nombre}")
        
        if not unidad1.esta_vivo():
            print(f"{unidad1.nombre} ha muerto")
    
    else :
        print(f"{unidad2.nombre} ha muerto")

#funciones de batalla
def batalla (ejercito1, ejercito2):
    ronda = 1
    while ejercito1.tiene_unidades() and ejercito2.tiene_unidades():
        print(f"Ronda {ronda}")
        unidad1 = random.choice([unidad for unidad in ejercito1.unidades if unidad.esta_vivo()])
        unidad2 = random.choice([unidad for unidad in ejercito2.unidades if unidad.esta_vivo()])
        combate(unidad1, unidad2)
        ronda += 1

    if ejercito1.tiene_unidades():
        print(f"{ejercito1.nombre} ha ganado")
    else:
        print(f"{ejercito2.nombre} ha ganado")

#-----------------------------------------------------------------------------------------------
#crear ejercitos
ejercito1 = Ejercito("Ejército Rojo")
ejercito2 = Ejercito("Ejército Azul")


#reclutar unidades
for _ in range(30):
    ejercito1.reclutar_unidad(Arquero())
for _ in range(30):    
    ejercito1.reclutar_unidad(Infanteria())
for _ in range(30):    
    ejercito1.reclutar_unidad(Caballeria())

for _ in range(30):
    ejercito2.reclutar_unidad(Arquero())
for _ in range(30):    
    ejercito2.reclutar_unidad(Infanteria())
for _ in range(30):    
    ejercito2.reclutar_unidad(Caballeria())
#-----------------------------------------------------------------------------------------------
#guardar en un log el resultado de la batalla
import logging
logging.basicConfig(filename='batalla.log', level=logging.DEBUG)
logging.info('Batalla iniciada')
logging.info('Ejercito 1: ')
for unidad in ejercito1.unidades:
    logging.info(f"{unidad.nombre} ({unidad.salud} HP)")
logging.info('Ejercito 2: ')
for unidad in ejercito2.unidades:
    logging.info(f"{unidad.nombre} ({unidad.salud} HP)")
#-----------------------------------------------------------------------------------------------
#iniciar batalla
batalla(ejercito1, ejercito2)