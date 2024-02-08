from classes.player import Player
        # Ninja
            # What is specific to Ninja? (ie evasion stat)
            # higher evasion
            # higher speed
            # lower hp & defense
            
            # Attacks


        # uniaue abilities
            # Invisibility
                # 2 secs duration, increases evasion
            # Shadow Clone
                # guarentee dodge
            # Bleed Damage
                #damage over time

# @classmethod
# def 


class Ninja(Player):

    def __init__( self, name, attack = 20, defense =5, health_points = 100, speed = 15, evasion = 20):
        super().__init__(attack, defense, health_points, speed, evasion)
        self.name = name




    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack( self , pirate ):
        super().turn_speed(pirate)
        return self
    
    def evasion(self):
        pass


ninja = Ninja('Ninja')
