# Project lab-data-vikings
import random


# Soldier (constructor, ataque y daño)
class Soldier:
    def  __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength

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
            return self.name + " has received " + str(dmg) + " points of damage"
        else:
            return self.name + " has died in act of combat"

    def battle_cry(self):
        return "Odin Owns You All!"


# Saxon
class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)

    def receive_damage(self, dmg):
        self.health -= dmg
        if self.health > 0:
            return "A Saxon has received " + str(dmg) + " points of damage"
        else:
            return "A Saxon has died in combat"


# War
class War:
    def __init__(self):
        self.viking_army = []
        self.saxon_army = []

    def add_viking(self, viking):
        self.viking_army.append(viking)

    def add_saxon(self, saxon):
        self.saxon_army.append(saxon)

    def viking_attack(self):
        viking = random.choice(self.viking_army)
        saxon = random.choice(self.saxon_army)

        vikingAttack = saxon.receive_damage(viking.strength)

        if saxon.health <= 0:
            self.saxon_army.remove(saxon)

        return vikingAttack

    def saxon_attack(self):
        saxon = random.choice(self.saxon_army)
        viking = random.choice(self.viking_army)

        saxonAttack = viking.receive_damage(saxon.strength)

        if viking.health <= 0:
            self.viking_army.remove(viking)

        return saxonAttack

    def show_status(self):
        if len(self.saxon_army) == 0:
            return "Vikings have won the war of the century!"
        elif len(self.viking_army) == 0:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."