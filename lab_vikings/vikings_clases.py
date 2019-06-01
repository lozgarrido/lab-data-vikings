# Project lab-data-vikings
import random


# Soldier (constructor, ataque y daño)
class Soldier:
    def  __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def attack(self):
        return(self.strength)

    def receive_damage(self, dmg):
        self.health -= dmg


# Viking
class Viking(Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        self.name = name

    def receive_damage(self, dmg):
        self.health -= dmg
        if self.health > 0:
            return (self.name + " has received " + str(dmg) + " points of damage")
        else:
            return (self.name + " has died in act of combat")

    def battle_cry(self):
        return("Odin Owns You All!")


# Saxon
class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)

    def receive_damage(self, dmg):
        self.health -= dmg
        if self.health > 0:
            return ("A Saxon has received " + str(dmg) + " points of damage")
        else:
            return ("A Saxon has died in combat")


# War
class War:
    def __init__(self):
        self.viking_army = []
        self.saxon_army = []

    def add_viking(self, Viking):
        self.viking_army.append(Viking)

    def add_saxon(self, Saxon):
        self.saxon_army.append(Saxon)

    def viking_attack(self):
        viking = random.choice(self.viking_army)
        viking_damage = viking.strength
        saxon = random.choice(self.saxon_army)

        saxon.receive_damage(viking_damage)

        if saxon.health <= 0:
            self.saxon_army.remove(saxon)

    def saxon_attack(self):
        saxon = random.choice(self.saxon_army)
        saxon_damage = saxon.strength
        viking = random.choice(self.viking_army)

        viking.receive_damage(saxon_damage)

        if viking.health <= 0:
            self.viking_army.remove(viking)

    def show_status(self):
        if len(self.saxon_army) == 0:
            return("Vikings have won the war of the century!")
        elif len(self.viking_army) == 0:
            return("Saxons have fought for their lives and survive another day...")
        else:
            return("Vikings and Saxons are still in the thick of battle.")
