# roomMap = {
#     '1': {'left': '2', 'right': '4'},
#     '2': {'right': '1'},
#     '4': {'left': '1'}
# }
from time import sleep


class Character:
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense

    def loiter(self):
        print(f'{self.name} is idling..')
        sleep(1)
        print('Idling is done.')


class Monster(Character):
    def __init__(self, name, health, attack, defense, ability):
        super().__init__(name, health, attack, defense)
        self.ability = ability

    def crawl(self):
        print("The monster is crawling nearby.")

    def inspect(self):
        print(f"Stats for {self.name}: Health is {self.health}. Attack is {self.attack}. "
              f"Defense is {self.defense}. Ability is {self.ability}.")

    def monitor_hp(self):
        if not self.health:
            print(f'The {self.name} is gone with the wind.')


class Player(Character):
    def __init__(self, name, health, attack, defense, skill):
        super().__init__(name, health, attack, defense)
        self.skill = skill

    def hit(self, monster):
        print(f"{self.name} attacks the {monster.name}.")
        sleep(1)
        monster.health = monster.health - self.attack
        print(f"It's hp is now at {monster.health}.")
        monster.monitor_hp()

    def weight_training(self):
        print('Player does the weight training.')

    def toture_room(self):
        print('Player goes into the torture room. Gain +5 def')


one_eyed_bat = Monster('one-eyed Bat', 30, 5, 3, "screech")
one_eyed_bat.inspect()

mage = Player('Mage', 100, 15, 20, "heal")
# mage.loiter()
mage.hit(one_eyed_bat)
mage.hit(one_eyed_bat)
