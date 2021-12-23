import sounds
# Base class for all items


class Item():
    # __init__ is the contructor method
    def __init__(self, name, description, value):
        self.name = name   # attribute of the Item class and any subclasses
        self.description = description  # attribute of the Item class and any subclasses
        self.value = value  # attribute of the Item class and any subclasses

    # __str__ method is used to print the object
    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description, self.value)

# Extend the Items class
# Gold class will be a child or subclass of the superclass Item


class Lunarglasses(Item):
    # __init__ is the contructor method
    def __init__(self, Zoom):
        self.Zoom = Zoom  # attribute of the lunarglass class
        super().__init__(name="Lunarglasses",
                         description="the glases with {} zoom for night vision. Night Vision devices".format(
                             self.Zoom),
                         value=self.Zoom)


class Transport:
    def __init__(self):
        self.name = 'walk'
        self.description = 'walking to other districts'

    def RailorHovercraft(self, speed):
        if(speed <= 500 and speed >= 20):
            sounds.Jetsound()
            self.name = "Highspeedrail"
            self.description = "you are travelling via high speed bullet train"
            print("{} === {} at speed {} km/h".format(
                self.name, self.description, speed))

        elif(speed > 500):
            self.name = "Hovercraft"
            self.description = "this is the super fast hovercraft"
            print("{} === {} at speed {} km/h".format(
                self.name, self.description, speed))
        else:
            self.name = "HorseRide"
            self.description = "horse ride to other districts with amazing views of monuments history and countryside"
            print("{} === {} at speed {} km/h".format(
                self.name, self.description, speed))

    def __str__(self):
        return "{}\n=====\n{}\n speed: ".format(self.name, self.description)


class Weapon(Item):
    def __init__(self, name, description, value, damage):
        self.damage = damage
        super().__init__(name, description, value)

    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nDamage: {}".format(self.name, self.description, self.value, self.damage)


class Axe(Weapon):
    def __init__(self):
        super().__init__(name=" Axe",
                         description="You have the axe weapon.use it to kill the birds and fight the tribute ",
                         value=0,
                         damage=15)


class BowAndArrow(Weapon):
    def __init__(self):
        super().__init__(name="BowAndArrow",
                         description="Use bow and Arrow as precise as katniss.damages snake mutation",
                         value=10,
                         damage=10)


class Trident(Weapon):
    def __init__(self):
        super().__init__(name="Trident",
                         description="you have chosen favourite weapon of katniss.",
                         value=0,
                         damage=25)


class Sword(Weapon):
    def __init__(self):
        super().__init__(name="Sword",
                         description="Use sword to combat with the tribute from the other districts",
                         value=1,
                         damage=20)


class Knives(Weapon):
    def __init__(self):
        super().__init__(name="Knives",
                         description="use it to combat with enemies. the sharf edges will low down the enemys health",
                         value=2,
                         damage=25)


class Spear(Weapon):
    def __init__(self):
        super().__init__(name="Spear",
                         description="throw the spear like a javelin thrower to kill far distant enemies",
                         value=5,
                         damage=20)


class Antidote(Item):
    def __init__(self, name, description, value, amt, health):
        self.amt = amt
        self.health = health
        super().__init__(name, description, value)


class AntidoteLeaves(Antidote):
    def __init__(self):
        super().__init__(name='AntidoteLeaves',
                         description='A small potion', value=5, amt=5, health=30)
