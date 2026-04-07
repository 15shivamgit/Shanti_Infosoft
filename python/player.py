class Player:
    game_name = "Dragon slayer"
    total_player = 0

    def __init__(self):
        self.name = "abhishek"
        self.__health = 100
        self.__life_line = 3
        self.__level = 1
        self.__Inventory = ""
        self.total_player += 1

    def create_new_player(self, name):
        self.__name = name

        print(f"""
new player {self.__name} has joined.
health = {self.__health}
life_life = {self.__life_line}
level = {self.__level}
""")

    def run(self):
        pass

    def jump(self):
        pass

    def attack(self):
        pass

    def defence(self):
        pass

    def take_damage(self, amount):
        self.__health -= amount

# Types of player
class Warrior:
    def attack(self): print("Sword Swing!")

class Mage:
    def attack(self): print("Fireball!")




# Types of Enemy
class Enemy(Player):
    def abc(self):
        return self.name

class FlyingEnemy(Enemy):
    def fly(self): print("Flying!")

obj1=Enemy()
print(obj1.abc())