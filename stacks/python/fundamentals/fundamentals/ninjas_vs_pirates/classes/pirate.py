from classes.player import Player

class Pirate(Player):

    def __init__( self, name, attack = 25, defense =10, health_points = 125, speed = 10, evasion = 10):
        super().__init__(attack, defense, health_points, speed, evasion)
        self.name = name

    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack ( self , ninja ):
        super().turn_speed(self, ninja)
        return self

pirate = Pirate('Pirate')