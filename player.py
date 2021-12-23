import random
import items
import world
import os
import sounds


class Player():
    def __init__(self):
        # Inventory on startup
        self.inventory = [
            items.Lunarglasses(50), items.BowAndArrow(), items.Axe(), items.AntidoteLeaves()]
        self.hp = 100  # Health Points
        self.maxHp = 200
        self.location_x, self.location_y = world.the_capitol  # (0, 0)
        self.victory = False  # no victory on start up
        self.experience = 0
        self.level = 0
        self.money = 30
        self.attackPower = 100
        self.nextLevelUp = 10
        self.chosenWpn = None
        self.password = 'oakes'
        self.armor = False
        self.armorHits = 0
        self.currentwpn = self.inventory[1]

    def flee(self, tile):
        """Moves the player randomly to an adjacent tile"""
        available_moves = tile.adjacent_moves()
        r = random.randint(0, len(available_moves) - 1)
        self.do_action(available_moves[r])

    # is_alive method
    def is_alive(self):
        return self.hp > 0  # Greater than zero value then you are still alive

    def print_inventory(self):
        for item in self.inventory:
            print(item, '\n')

    def choseTransport(self):
        nmode = int(input("choose speed of transport in km/h : "))
        return items.Transport().RailorHovercraft(nmode)

    def move(self, dx, dy):
        self.location_x += dx
        self.location_y += dy
        self.transport = self.choseTransport()
        print(world.tile_exists(self.location_x, self.location_y).intro_text())

    def move_north(self):
        self.move(dx=0, dy=-1)

    def move_south(self):
        self.move(dx=0, dy=1)

    def move_east(self):
        self.move(dx=1, dy=0)

    def move_west(self):
        self.move(dx=-1, dy=0)

    def lockpass(self):
        yourpwd = input('enter the 5 digit password to start the game:')
        if(yourpwd == self.password):
            sounds.GodzillaSound()
            print('----Hurray! welcome to world of panem $$$$$')

        else:
            print('### you have entered wrong password.try again for the entry ###')
            return self.lockpass()

    def level_up(self):
        self.hp += 50
        self.experience += 60
        self.level += 1
        self.inventory.append(items.Knives())
        print("**you have reached level {}.** your hp is increased to {} and XP to {}**.##knife is awarded to you".format(
            self.level, self.hp, self.experience))

    def attack(self, enemy):
        best_weapon = None
        max_dmg = 0
        for i in self.inventory:
            if isinstance(i, items.Weapon):
                if i.damage > max_dmg:
                    max_dmg = i.damage
                    best_weapon = i

        print("You use {} against {}!".format(best_weapon.name, enemy.name))
        enemy.hp -= best_weapon.damage
        if not enemy.is_alive():
            self.experience += 30
            print(
                "You killed {}!,** your xp increased to {} ".format(enemy.name, self.experience))
        elif self.experience > 50:
            self.hp += 50
            self.maxHp += 50
            self.attackPower += 30
            print("you have reached level 1.** your hp is now {}/n ** your attackPower is {}.".format(
                self.hp, self.attackPower))
        else:
            print("{} HP is {}.".format(enemy.name, enemy.hp))

    def heal(self):
        print("\n these are the antidotes you currently posses.\n")
        antidote_list = []
        for antidote in self.inventory:
            if isinstance(antidote, items.AntidoteLeaves):
                if antidote.amt <= 0:
                    self.inventory.remove(antidote)
                    continue
                else:
                    antidote_list.append(antidote)
        i = 1
        for antidote in antidote_list:
            print(i, ". ", antidote.name, sep='')
            i += 1
        while True:
            if len(antidote_list) == 0:
                print("you have no antidote.")
                os.system("pause")
                return None

            itemChoice = int(input("""\nSelect a antidote: """))

            if itemChoice not in range(0, len(antidote_list)):
                print("\nInvalid choice")
                continue
            break
        self.healToPlayer(itemChoice, antidote_list)

    def healToPlayer(self, itemChoice, antidotelist):
        chosenantidote = antidotelist[itemChoice]
        self.hp = self.hp + chosenantidote.health
        chosenantidote.amt = chosenantidote.amt - 1
        if chosenantidote.amt == 0:
            self.inventory.remove(chosenantidote)

        if self.maxHp < self.hp:
            self.hp = self.maxHp

    def equip(self):
        print("\n These are the weapons you currently posses.\n")

        weapon_list = []
        for item in self.inventory:
            if isinstance(item, items.Weapon):
                weapon_list.append(item)

        i = 1
        for weapon in weapon_list:
            print(i, ". ", weapon.name, sep='')
            i += 1

        while True:
            itemChoice = int(input(
                """\nSelect the weapon you want to equip: """)) - 1

            if itemChoice not in range(0, len(weapon_list)):
                print("\nInvalid weapon choice")
                continue
            break
        print('\n')
        print(weapon_list[itemChoice].name, "equipped.\n")
        self.currentwpn = weapon_list[itemChoice]

    def status(self):
        print("you are level {}\n".format(self.level))
        print(" ** Current HP: {} /".format(self.hp), "{}\n".format(self.maxHp))
        print(" ** attack power: {}\n".format(self.attackPower))
        print(" ** XP until next level up: {}\n".format(self.nextLevelUp - self.experience))
        os.system("pause")

    def do_action(self, action, **kwargs):
        action_method = getattr(self, action.method.__name__)
        if action_method:
            action_method(**kwargs)
