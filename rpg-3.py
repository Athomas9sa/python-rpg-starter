"""
In this simple RPG game, the hero fights the goblin. He has the options to:

1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee

"""

#Creating Warrior Class
class Warrior: 
    #Construct for Warrior class
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power

    def __str__(self):
        return "%s has %d health and %d power." % (self.name, self.health, self.powers)


    def __str__(self):
        return""" 
        %s health: %d,
        %s power: %d,
        """ (self.name, self.health, self.powers)

hiro = Her(10, 5, "Hiro")
spike = Goblin(10, 2, "Spike")

#Creating Sub Class Hero
class Hero(Warrior):
    #Construct for Hero class‹‹
    def __init__(self, health, power):
      super().__init__(health, power)

class Goblin(Warrior):
    #Construct for Goblin class
    def __init__(self, health, power):
        super().__init__(health, power)

#Creating Instances
hiro = Hero(10,5)
spike = Goblin(6, 2)


def main():
# hiro.health = 10
# hiro.power = 5
# spike.health = 6
# spike.power = 2

    while spike.health > 0 and hiro.health > 0:
        #print("You have %d health and %d power." % (hiro.health, hiro.power))
        #print("The goblin has %d health and %d power." % (spike.health, spike.power))
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ",)
        user_input = input()
        if user_input == "1":
            # Hero attacks goblin
            spike.health -= hiro.power
            print("You do %d damage to the goblin." % hiro.power)
            if spike.health <= 0:
                print("The goblin is dead.")
        elif user_input == "2":
            pass
        elif user_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input %r" % user_input)

        if spike.health > 0:
            # Goblin attacks hero
            hiro.health -= spike.power
            print("The goblin does %d damage to you." % spike.power)
            if hiro.health <= 0:
                print("You are dead.")

main()