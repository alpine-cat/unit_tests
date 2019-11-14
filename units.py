from random import Random
import functools
import operator



def geometric_mean(iterable):
    return (functools.reduce(operator.mul, iterable)) ** (1.0/len(iterable))

class Unit:
    def __init__(self, rand, hp=100, cool_down=None):
        self._hp = hp
        self._cool_down = cool_down
        self._rand = rand

    @property
    def is_active(self):
        pass

    @property
    def hp(self):
        pass

    @property
    def cool_down(self):
        pass

    def attack_chance(self):
        pass

    def attack(self, adversary):
        pass

    def damage(self):
        pass

    def get_damage(self, points):
        pass


class Soldier(Unit):
    def __init__(self,  xp=0, rand=Random()):
        super().__init__(rand)
        self._xp = xp

    @property
    def xp(self):
        return self._xp

    @xp.setter
    def xp(self, xp):
        if not isinstance(xp,int): 
            self._xp = 0
            return
        self._xp = min(xp,50)
        

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, hp):
        if not type(hp) == float and not type(hp)==int:
            return None
        self._hp = hp

    @property
    def cool_down(self):
        return self._cool_down

    @cool_down.setter
    def cool_down(self, cool_down):
        self._cool_down = cool_down

    @property
    def is_active(self):
        return not self._cool_down

    def attack_chance(self):
        return 0.5*(1 + self.hp/100) * self._rand.randrange(50+self.xp, 101)/100

    def damage(self) -> float:
        return 0.05 + self.xp

    def get_damage(self, points):
        self.hp = max(0, self.hp - points)

    def attack(self, adversary: Unit):
        if self.attack_chance() > 0.5:
            adversary.get_damage(self.damage())
            self.xp += 1
        self.cool_down = 1


class Vehicle(Unit):
    def __init__(self, operators, rand=Random()):
        super().__init__(rand)
        self._operators = operators

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, hp):
        self._hp = hp

    @property
    def cool_down(self):
        return self._cool_down

    @cool_down.setter
    def cool_down(self, cool_down):
        self._cool_down = cool_down

    @property
    def is_active(self):
        return not self._cool_down

    @property
    def operators(self):
        return self._operators

    @operators.setter
    def operators(self, operators):
        self._operators = operators

    def attack_chance(self):
        gavg = list()
        for operator in self.operators:
            gavg.append(operator.attack_chance())
        return 0.5*(1+self.hp/100) * geometric_mean(gavg)

    def damage(self):
        sum = 0.0
        for operator in self.operators:
            sum += operator.xp / 100
        return 0.1 + sum

    def get_damage(self, points):
        self.operators[self._rand.randint(0, len(self.operators) - 1)].get_damage(points)
        av = 0.0
        for operator in self.operators:
     
            if operator.hp == 0:
                self.operators.remove(operator)
                continue

            av += operator.hp
        av /= len(self.operators)
        self.hp = av

    def attack(self, adversary):
        if self.attack_chance() > 0.5:
            adversary.get_damage(self.damage())
            for operator in self.operators:
                operator.xp = min(50, operator.xp + 1)
        self.cool_down = 2


