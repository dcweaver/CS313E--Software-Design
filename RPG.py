h#  File: RPG.py
#  Description:
#  Student's Name: David Chase Weaver   
#  Student's UT EID:dcw2259
#  Course Name: CS 313E 
#  Unique Number: XXXXX
#
#  Date Created: February 12, 2019
#  Date Last Modified: February 15, 2019

class Weapon:

    def __init__(self,weapon):
        self.weapon = weapon
        if self.weapon == "dagger":
            self.damage = 4
        elif self.weapon == "axe":
            self.damage = 6
        elif self.weapon == "staff":
            self.damage = 6
        elif self.weapon == "sword":
            self.damage = 10
        else:
            self.damage = 1

    def __str__(self):
        
        return self.weapon
            
        
class Armor:

    def __init__(self,armor):
        self.armor = armor
        
        if self.armor == "plate":
            self.protection = 2
        elif self.armor == "chain":
            self.protection = 5
        elif self.armor == "leather":
            self.protection = 8
        else:
            self.protection = 10

    def __str__(self):
        return self.armor

    
    
    
class RPGCharacter:
    
    armorWorn = Armor("none")
    weaponWield = Weapon("none")

    def __str__(self):
        return "\n" + str(self.name) + "\n   Current Health: " + str(self.currentHealth) + "\n   Current Spell Points: " + \
               str(self.currentSP) + "\n   Wielding: " + str(self.weaponWield.weapon) + "\n   Wearing: " + str(self.armorWorn.armor) + \
               "\n   Armor class: " + str(self.armorWorn.protection) + "\n"

    def wield(self, weapon):
        #have game check if character is a fighter, if so, character can wield any weapon
        if isinstance(self,Fighter):
            self.weaponWield = Weapon(weapon)
            print(str(self.name), "is now wielding a(n)", str(weapon))

        #have game check if character is a wizard. If wizard, can only use dagger, staff, or no weapon(bare hands)
        elif isinstance(self,Wizard):

            if (weapon == "sword") or (weapon == "axe"):
                print("Weapon not allowed for this character class")
            else:
                self.weaponWield = Weapon(weapon)
                print(str(self.name), "is now wielding a(n)", str(weapon))

    def unwield(self):

        self.weaponWield = Weapon("none")
        return str(self.name) + "is no longer wielding anything"


    def putOnArmor(self, armorWorn):
        if isinstance(self, Fighter):
            self.armorWorn = Armor("plate")
            print(str(self.name), "is now wearing", str(armorWorn))

        elif isinstance(self, Wizard):
            armorWorn = Armor("none")
            print("Armor is not allowed for this class")

    def takeOffArmor(self):
        self.armorWorn = ("none")
        print(str(self.name), "is no longer wearing anything")

    def checkForDefeat(self,RPGCharacter):
        if RPGCharacter.currentHealth <= 0:
            print(str(RPGCharacter.name) + " has been defeated!")

    #Method for attacking another character in the game
    def fight(self, RPGCharacter):
        
        print(str(self.name) + " attacks " + str(RPGCharacter.name) + " with a(n) " + str(self.weaponWield.weapon))
        RPGCharacter.currentHealth -= self.weaponWield.weapon.damage
        print(str(self.name) + " does " + str(self.weaponWield.weapon.damage) + " damage to " + str(RPGCharacter.name))
        print(str(RPGCharacter.name) + " is now down to " + str(RPGCharacter.currentHealth) + " health")
        
        self.checkForDefeat(RPGCharacter)

        
    
        

        

class Fighter(RPGCharacter):
    
   def __init__(self, name):
        self.name = name
        self.maxHealth = 40
        self.currentHealth = self.maxHealth
        self.maxSP = 0
        self.currentSP = self.maxSP
        
class Wizard(RPGCharacter):

    def __init__(self, name):
        self.name = name
        self.maxHealth = 16
        self.currentHealth = self.maxHealth
        self.maxSP = 20
        self.currentSP = self.maxSP
        
    #Method to cast spell at other character
    def castSpell(self,spell, RPGCharacter):

        if spell == "Fireball":
            cost = 3
            effect = 5
            

        elif spell == "Lightning Bolt":
            cost = 10
            effect = 10
            

        elif spell == "Heal":
            cost = 6
            effect = -6
            
            
        else:
            print("Unknown spell name. Spell failed.")
            return


        #Spell is cast
        print(str(self.name) + " casts " + str(spell) + " at " + str(RPGCharacter.name))

        #result of healing spell
        if spell == "Heal":
                if RPGCharacter.currentHealth <= RPGCharacter.maxHealth + 6:
                    RPGCharacter.currentHealth -= effect
                    print(str(self.name) + " heals " + str(RPGCharacter.name) + " for " + str(effect * -1) +
                          " health points.")
                    print(str(self.name) + " is now at " + str(RPGCharacter.currentHealth) + " health")
                elif ((RPGCharacter.currentHealth + 6) > RPGCharacter.maxHealth):
                    self.currentHealth = self.maxHealth
        #result of successful attack spell
        elif spell == "Fireball" or spell == "Lightning Bolt":
            
            RPGCharacter.currentHealth -= effect
            print(str(self.name) + " does " + str(effect) + " to " + str(RPGCharacter.name))
            print(str(RPGCharacter.name) + " is now down to " + str(RPGCharacter.currentHealth) + " health")


        #Not enough Spell Points to cast spell
        if self.currentSP - cost <= 0:
            print("Insufficient spell points")
            return
                
        self.currentSP -= cost 
            
            

    

def main():

    plateMail = Armor("plate")
    chainMail = Armor("chain")
    sword = Weapon("sword")
    staff = Weapon("staff")
    axe = Weapon("axe")

    gandalf = Wizard("Gandalf the Grey")
    gandalf.wield(staff)
    
    aragorn = Fighter("Aragorn")
    aragorn.putOnArmor(plateMail)
    aragorn.wield(axe)
    
    print(gandalf)
    print(aragorn)

    gandalf.castSpell("Fireball",aragorn)
    aragorn.fight(gandalf)

    print(gandalf)
    print(aragorn)
    
    gandalf.castSpell("Lightning Bolt",aragorn)
    aragorn.wield(sword)

    print(gandalf)
    print(aragorn)

    gandalf.castSpell("Heal",gandalf)
    aragorn.fight(gandalf)

    gandalf.fight(aragorn)
    aragorn.fight(gandalf)

    print(gandalf)
    print(aragorn)


main()
    

    
