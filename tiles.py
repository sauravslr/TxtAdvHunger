import items
import enemies
import actions
import world
import sounds
import player


class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def intro_text(self):
        raise NotImplementedError()

    def modify_player(self, player):
        raise NotImplementedError()

    def adjacent_moves(self):
        """Returns all move actions for adjacent tiles."""
        moves = []
        if world.tile_exists(self.x + 1, self.y):
            moves.append(actions.MoveEast())
        if world.tile_exists(self.x - 1, self.y):
            moves.append(actions.MoveWest())
        if world.tile_exists(self.x, self.y - 1):
            moves.append(actions.MoveNorth())
        if world.tile_exists(self.x, self.y + 1):
            moves.append(actions.MoveSouth())
        return moves

    def available_actions(self):
        """Returns all of the available actions in this room."""
        moves = self.adjacent_moves()
        moves.append(actions.ViewInventory())
        moves.append(actions.Equip())
        moves.append(actions.Heal())
        moves.append(actions.Status())

        return moves


class TheCapitol(MapTile):
    # override the intro_text method in the superclass
    def intro_text(self):
        return """
         __  .__             .__                                                                             
_/  |_|  |__   ____   |  |__  __ __  ____    ____   ___________     _________    _____   ____   ______
\   __\  |  \_/ __ \  |  |  \|  |  \/    \  / ___\_/ __ \_  __ \   / ___\__  \  /     \_/ __ \ /  ___/
 |  | |   Y  \  ___/  |   Y  \  |  /   |  \/ /_/  >  ___/|  | \/  / /_/  > __ \|  Y Y  \  ___/ \___ \ 
 |__| |___|  /\___  > |___|  /____/|___|  /\___  / \___  >__|     \___  (____  /__|_|  /\___  >____  >
           \/     \/       \/           \//_____/      \/        /_____/     \/      \/     \/     \/ 
        welcome to the 75th edition of hunger game. this is the country of panem with 
        13 districts.You are currently into the capital city of panem. In order to meet the
        tributes from other districts please visit other districts
        """

    def modify_player(self, player):
        # Room has no action on player
        # sounds.intro()
        return player.lockpass()


class LootRoom(MapTile):
    def __init__(self, x, y, item):
        self.item = item
        super().__init__(x, y)

    def add_loot(self, player):
        player.inventory.append(self.item)

    def modify_player(self, player):
        self.add_loot(player)


class EnemyRoom(MapTile):
    def __init__(self, x, y, enemy):
        self.enemy = enemy
        super().__init__(x, y)

    def modify_player(self, the_player):
        if self.enemy.is_alive():
            the_player.hp = the_player.hp - self.enemy.damage
            print("Enemy does {} damage. You have {} HP remaining.".format(
                self.enemy.damage, the_player.hp))

    def available_actions(self):
        if self.enemy.is_alive():
            return [actions.Flee(tile=self), actions.Attack(enemy=self.enemy)]
        else:
            return self.adjacent_moves()


class WolfRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Wolf())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
             A wolf jumps down in front of you!
             """
        else:
            return """
             The corpse of a dead wolf is on the ground.
             """


class FindDaggerRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Dagger())

    def intro_text(self):
        return """
        Your notice something shiny in the corner.
        It's a dagger! You pick it up.
        """


class GodzillaRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Godzilla())

    def intro_text(self):
        if self.enemy.is_alive():
            sounds.GodzillaSound()
            return """
             A giant Godzilla is coming to attack you.
             """
        else:
            return """
             Hurray! you have knocked down godzilla
             """


class SnakeRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Snake())

    def intro_text(self):
        if self.enemy.is_alive():
            sounds.snakeSound()
            return """
             A King Cobra is waiting for u
             """
        else:
            return """
             you have escaped from the bite of snake.
             """


class Livestock(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Wolfmuttations())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
            District 10 specializes in livestock.***WOLFMUTTATIONS are on the way to attack you***.Katniss does 
            not note any major tributes from District 10, except one boy with a crippled leg who is mentioned several times
            """
        else:
            return """
            *** you have killed WOLFMUTTATIONS. Its time to move on to the next District"""


class Textiles(LootRoom):
    def __init__(self, x, y, ):
        super().__init__(x, y, items.Spear())

    def intro_text(self):
        return """
            **get the spear which is special weapon useful in other districts to fight against enemies***
            District 8 specializes in textiles, including at least one factory in which
            Peacekeeper uniforms are made. Along with Districts 7 and 11, it was one of the first districts to rebel. 
            *** Peacekeepers are coming to Torture the people. As a Tribute save the people from them ****"""


class Lumber(EnemyRoom):
    def __init__(self, x, y, ):
        super().__init__(x, y, enemies.MonkeyMutts())

    def intro_text(self):
        if self.enemy.is_alive():
            return """$$$$$ Incoming MONKEYMUTTS
            District 7 specializes in forestry, lumber and paper. Its two tributes in the 74th Hunger Games die in the initial bloodbath.
            In the 75th Hunger Games, the tributes selected are Blight, who protests his inclusion, and Johanna Mason,
            a strong-willed yet somewhat abrasive woman who has no qualms with killing with her axe, a signature weapon from her district.
            """
        else:
            return """$$$ monkeymutt finished.lets keep going!"""


class Fishing(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.BowAndArrow())

    def intro_text(self):
        return """
        District 4 is a coastal district that specializes in aquaculture and wild fisheries. It is another wealthy district in which 
        children often train for the Hunger Games. It is said that District 4 has the most "decent-looking" people.
        The most popular bread baked in this District is a salty, fish-shaped loaf tinted green by seaweed.
        The most common tools in District 4 are fishing nets, tridents and fishing rods.
        """


class Technology(MapTile):

    def intro_text(self):
        return """
        here you can heal yourself up.
        District 3 specializes in the production of technology and electronics.
        Most of its inhabitants work in factories and are good at engineering, which helps its tributes in the Games.
        In the Seventy-Fourth Hunger Games, the male tribute from District 3 manages to reactivate the land mines
        surrounding the Cornucopia to protect the supplies of the Careers. One of the previous victors from 
        District 3, Beetee Latier, won his Games by setting a trap that electrocuted six tributes at once. 
        He uses his skills after being chosen to compete in the Seventy-fifth Hunger Games in Catching Fire.
        Although District 3 seems to have technological advantages over other districts, 
        it is the poorest of the wealthy districts and typically does not do well in the Games.
        """

    def modify_player(self, player):
        # Room has no action on player
        return player.heal()


class Power(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.LizardMuttations())

    def intro_text(self):
        if self.enemy.is_alive():

            return """
            *** Beware of LizardMuttations ***
            District 5 specializes in electrical power, Caesar Flickerman refers to them as the "Power Plant Workers"
            in the first film. The district is dotted by 
            dams that provide the Capitol with electricity; this fact is exploited by the rebels, who destroy the dams,
            briefly cutting off electricity within the Capitol and allowing District 13 to rescue the captured Victors.
            """
        else:
            """Lets go and meet the tribute in next district"""


class Grain(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.SnakeMutts())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
            District 9 specializes in producing grain and salts.
            It is the least mentioned district in the series; no named character from the district has appeared in the series
            """
        else:
            return """
            killed"""


class Masonry(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Trident())

    def intro_text(self):
        return """** Trident is one of the most powerful weapons.Well done***
        District 2 is in charge of stone cutting, supplying Peacekeepers, and weapons manufacturing. 
        It is also a center of training for the Capitol's army of Peacekeepers. 
        District 2 is a large district in the mountains, not far from the Capitol itself. 
        Its citizens have better living conditions than most other districts, and support for Capitol control is stronger there than in any other district. 
        Some citizens of District 2 name their children in Ancient Roman or Greek style, like those common in the Capitol. 
        District 2 tributes often volunteer for the Games even when not selected in the drawing, which makes reapings very difficult. 
        As such, their tributes often train for the games and are among those referred to as "careers."
        """


class Luxury(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Sword)

    def intro_text(self):
        return """
        Welcome to the district.HERE the tribute are offering you Sword as a Gift.
        District 1 specializes in producing 
        luxury items like jewelry. Children living there take pride in representing District 1 in the Games and
        are often among the group of tributes nicknamed "Careers" who illegally train for the Games from a young age.
        Along with District 2, District 1 is heavily favored by the Capitol and is wealthier than the rest of the
        districts
        """


class Agriculture(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Lunarglasses(50))

    def intro_text(self):
        return """
        District 11 specializes in agriculture.So use Lunarglasses to roam around the places. It is located somewhere in the South and is very large, possibly
        occupying nearly all the Deep South. The people live in small shacks, and there is a harsh force of Peacekeepers.
        """


class Transition(MapTile):

    def intro_text(self):
        return """
           __   ___   ____    ____  ____    ____  ______  __ __  _       ____  ______  ____  ___   ____   _____ __ 
   /  ] /   \ |    \  /    ||    \  /    ||      ||  |  || |     /    ||      ||    |/   \ |    \ / ___/|  |
  /  / |     ||  _  ||   __||  D  )|  o  ||      ||  |  || |    |  o  ||      | |  ||     ||  _  (   \_ |  |
 /  /  |  O  ||  |  ||  |  ||    / |     ||_|  |_||  |  || |___ |     ||_|  |_| |  ||  O  ||  |  |\__  ||__|
/   \_ |     ||  |  ||  |_ ||    \ |  _  |  |  |  |  :  ||     ||  _  |  |  |   |  ||     ||  |  |/  \ | __ 
\     ||     ||  |  ||     ||  .  \|  |  |  |  |  |     ||     ||  |  |  |  |   |  ||     ||  |  |\    ||  |
 \____| \___/ |__|__||___,_||__|\_||__|__|  |__|   \__,_||_____||__|__|  |__|  |____|\___/ |__|__| \___||__|
                                                                                                            
        
        """

    def modify_player(self, player):
        # Room has no action on player
        sounds.level()
        return player.level_up()


class NuclearPower(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Jabberjay())

    def intro_text(self):
        if self.enemy.is_alive():
            return """ Jabberjay are powerful. You need to use everything to beat him***
            Before the Dark Days war, District 13 specialized in nuclear technology and the development of emerging technologies for use by Panem's military.
            """
        else:
            return """$$$$ you have defeated president snows challenge $$$"""


class Transportation(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Trackerjackers())

    def intro_text(self):
        if self.enemy.is_alive():
            return """### Tracker jackers Beware####
            District 6 specializes in transportation, serving as a hub for Panem's transport network.
            """
        else:
            return """We are almost there!Dont give up"""


class Coal(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Grooslings())

    def intro_text(self):
        if self.enemy.is_alive():
            return """Grooslings Incoming
            District 6 specializes in transportation, serving as a hub for Panem's transport network.
            """
        else:
            return """Vamos! Grooslings dead!"""
