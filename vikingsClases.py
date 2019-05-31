# Project lab-data-vikings
import random


# Soldier (constructor, ataque y daño)
class Soldier:

    # Constructor: contiene las propiedades self, health y strength
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    # Método 'attack' no recive ninguna variable aparte de self. Este método devuelve la propiedad 'strength'.
    def attack(self):
        return self.strength

    # Método 'receiveDamage' recibe la variable daño ('skadi') la cual afecta a la propiedad 'health'
    def receive_damage(self, skadi):
        self.health = self.health - skadi


# Viking
class Viking(Soldier):

    # Constructor: hereda de Soldier las propiedades health y strength e incorpora adicionalmente la propiedad name.
    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        self.name = name


    # Método 'receiveDamage' recibe la variable daño ('skadi') la cual afecta a la propiedad 'health'. Adicionalmente este método devuelve un mensaje en función del estado del vikingo (si 'health' <= 0 es que ha muerto).
    def receive_damage(self, skadi):
        self.health = self.health - skadi
        if self.health > 0:
            return ('{} has received {} points of damage').format(self.name, skadi)
        elif self.health <= 0:
            return ('{} has died in act of combat').format(self.name)

    # Método 'battleCry' devuelve el grito de guerra de los vikingos.
    def battle_cry(self):
        return 'Odin Owns You All!'


# Saxon
class Saxon(Soldier):

    # Constructor: hereda de Soldier las propiedades health y strength.
    def __init__(self, health, strength):
        super().__init__(health, strength)


    # Método 'receiveDamage' recibe la variable daño ('skadi') la cual afecta a la propiedad 'health'. Adicionalmente este método devuelve un mensaje en función del estado del sajón (si 'health' <= 0 es que ha muerto).
    def receive_damage(self, skadi):
        self.health = self.health - skadi
        if self.health > 0:
            saxon_alive = ('A Saxon has received {} points of damage').format(skadi)
            return saxon_alive
        else:
            saxon_dead = 'A Saxon has died in combat'
            return saxon_dead


# War
class War:

    # Se crea el constructor en el cual se crean 2 propiedades a las cuales se le asigna un array vacio a cada una
    def __init__(self):
        self.viking_army = []
        self.saxon_army = []

    # Se crea el método addViking el cual agrega un 'Viking' (con sus propiedades) al ejercito vikingo (vikingArmy)
    def add_viking(self, viking):
        self.viking_army.append(viking)

    # Se crea el método addSaxon el cual agrega un 'Saxon' (con sus propiedades) al ejercito sajón (saxonArmy)
    def add_saxon(self, saxon):
        self.saxon_army.append(saxon)

    # Se crea el método vikingAttack el cual define un ataque vikingo eligiendo de forma aleatoria un "vikingo" y un "sajón" de cada uno de los ejercitos.
    # Retorna el resultado (mensaje) según se ha definido en el método receiveDamage definido dentro de la clase Viking.
    def viking_attack(self):
        saxons = random.choice(self.saxon_army)
        vikings = random.choice(self.viking_army)
        r_vikings = saxons.receiveDamage(vikings.strength)
        if saxons.health <= 0:
            self.saxon_army.remove(saxons)
        return r_vikings

    # De forma equivalente se crea el método de ataque sajón.
    def saxon_attack(self):
        saxons = random.choice(self.saxon_army)
        vikings = random.choice(self.viking_army)
        r_saxons = vikings.receiveDamage(saxons.strength)
        if vikings.health <= 0:
            self.viking_army.remove(vikings)
        return r_saxons

    # Este método muestra el resultado de la batalla en función del estado de las propiedades definidas en esta clase.
    def show_status(self):
        if not self.viking_army:
            return "Saxons have fought for their lives and survive another day..."
        elif not self.saxon_army:
            return "Vikings have won the war of the century!"
        else:
            return "Vikings and Saxons are still in the thick of battle."
