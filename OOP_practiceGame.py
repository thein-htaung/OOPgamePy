# roomMap = {
#     '1': {'left': '2', 'right': '4'},
#     '2': {'right': '1'},
#     '4': {'left': '1'}
# }
from time import sleep


class Character:
    """ Create base stats for characters"""
    alive = True

    def __init__(self, name, health, atk_stat, def_stat):
        self.name = name
        self.health = health
        self.atk_stat = atk_stat
        self.def_stat = def_stat

    def loiter(self):
        print(f'{self.name} is idling..')
        sleep(1)
        print('Idling is done.')

    def inflict_damage(self, other):
        return (self.atk_stat - other.def_stat * 0.5) if self.atk_stat > other.def_stat * 0.5 else 0

    def print_hp(self):
        if self.health < 0:
            self.health = 0
            print(f'HP of {self.name} is now {self.health}')


class Monster(Character):
    def __init__(self, name, health, atk_stat, defense, ability):
        super().__init__(name, health, atk_stat, defense)
        self.ability = ability

    def attack(self, player):
        print("The monster attacks!")
        player.health = player.health - self.inflict_damage(player)
        print(f"Dealt {self.inflict_damage(player)} damage.")

    def inspect(self):
        print(f"Stats for {self.name}: Health is {self.health}. Attack is {self.atk_stat}. "
              f"Defense is {self.def_stat}. Ability is {self.ability}.")

    def monitor_hp(self):
        if self.health <= 0:
            self.alive = False
            print(f'The {self.name} is gone with the wind.')


class Player(Character):
    causeOfDeath = []

    def __init__(self, name, health, attack, defense, skill):
        super().__init__(name, health, attack, defense)
        self.skill = skill

    def hit(self, monster):
        if monster.alive:
            print(f"{self.name} attacks the {monster.name}.")
            sleep(1)
            monster.health = monster.health - self.inflict_damage(monster)
            monster.print_hp()
            monster.monitor_hp()
        else:
            print('The monster is already dead.')

    def weight_training(self):
        print('Player does the weight training.')
        sleep(2)
        self.atk_stat = self.atk_stat + 1
        print("Gained +1 Atk")

    def toture_room(self):
        print('Player goes into the torture room')
        sleep(2)
        self.def_stat = self.def_stat + 3
        self.health = self.health - 10
        print("Gained +3 Def. Lost 10 health.")
        if self.health <= 0:
            self.alive = False
            self.causeOfDeath.append("Torture room defenseTraining")


def dead(player):
    if player.health <= 0:
        print('You are dead..for now. Game over.')
        gameover = True
        return gameover


one_eyed_bat = Monster('one-eyed Bat', 30, 25, 10, "screech")
one_eyed_bat.inspect()

mage = Player('Mage', 100, 15, 15, "heal")
# mage.loiter()


while True:
    one_eyed_bat.attack(mage)
    mage.weight_training()
    mage.toture_room()
    mage.print_hp()

    if dead(mage):
        print("Cause of Death is " + mage.causeOfDeath[-1])
        break
