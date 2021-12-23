class Enemy:
    def __init__(self, name, hp, damage, experience):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.experience = experience

    def is_alive(self):
        return self.hp > 0


class Peacekeepers(Enemy):
    def __init__(self):
        super().__init__(name="Peace keepers", hp=30, damage=40, experience=40)


class Jabberjay(Enemy):
    def __init__(self):
        super().__init__(name="Jabberjay", hp=15, damage=10, experience=15)


class Mockingjay(Enemy):
    def __init__(self):
        super().__init__(name="Mockingjay", hp=18, damage=15, experience=10)


class Trackerjackers(Enemy):
    def __init__(self):
        super().__init__(name="Tracker jackers", hp=20, damage=20, experience=12)


class Grooslings(Enemy):
    def __init__(self):
        super().__init__(name="Grooslings", hp=5, damage=10, experience=20)


class Wolfmuttations(Enemy):
    def __init__(self):
        super().__init__(name="Wolf muttations", hp=20, damage=20, experience=20)


class LizardMuttations(Enemy):
    def __init__(self):
        super().__init__(name="Lizard Muttations", hp=15, damage=15, experience=15)


class MonkeyMutts(Enemy):
    def __init__(self):
        super().__init__(name="Monkey Mutts", hp=15, damage=20, experience=20)


class Candypinkbirds(Enemy):
    def __init__(self):
        super().__init__(name="Candy-pink birds", hp=10, damage=5, experience=15)


class SnakeMutts(Enemy):
    def __init__(self):
        super().__init__(name="Snake Mutts", hp=20, damage=10, experience=15)


class Nightlock(Enemy):
    def __init__(self):
        super().__init__(name="Nightlock", hp=5, damage=50, experience=50)
