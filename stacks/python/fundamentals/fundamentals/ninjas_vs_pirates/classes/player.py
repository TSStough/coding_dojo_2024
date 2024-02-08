import random

#Player
    # to minimize work use Player as a parent class


    # What do we want in the Player class? (ie Atk, Def, HP)

class Player:
    def __init__(self, attack = 20, defense =5, health_points = 100,speed = 10, evasion = 10):
        # Attack
        self.attacks = attack
        # Def
        self.defense = defense
        # Health Points
            # reaches 0 player faints game over
        self.health_points = health_points
        # Speed
            # when character goes
        # higher speed goes first
        self.speed = speed
        # Evasion
            # probability of Doge]
            # Dodge funct
        self.evasion = evasion

    def turn_speed (self, target):
        # who goes first
        if random.random()*self.speed > random.random()*target.speed:
            self.attack(target)
        else:
            target.attack(self)

    def attack(self, target):
        if not Player.evade(target):
            target.health_points -= (self.attacks - target.defense)
            print('hit')
        else:
            print('Attack Dodged!')
        return self
    
    @staticmethod
    def evade (player):
        if random.random()*100 < player.evasion:
            return True
        else:
            return False
    

        # take an action

# pirate.ninja.turn.attack

        
        # return self

# user1 = Player()
# user2 = Player()
# # user1.attack(user2)
# # user1.evade()
# user1.turn_speed(user2)