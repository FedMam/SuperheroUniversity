"""Core game entities: students, minions, villains and missions."""

# ==========================================
# CLASSES
# ==========================================
class Student:
    def __init__(self, nation, gender, real_name, superhero_name, uni_id, power,
                 hp, mp, dmg, pwr, defense, agl):
        self.nation = nation
        self.gender = gender
        self.real_name = real_name
        self.superhero_name = superhero_name
        self.uni_id = uni_id
        self.power = power
        self.hp = hp
        self.max_hp = hp
        self.mp = mp
        self.max_mp = mp
        self.dmg = dmg
        self.pwr = pwr
        self.defense = defense
        self.agl = agl
        self.courses_taken = {
            "HP": 0,
            "MP": 0,
            "DMG": 0,
            "PWR": 0,
            "DEF": 0,
            "AGL": 0
        }

    def clone(self):
        clone = Student(self.nation, self.gender, self.real_name,
                        self.superhero_name, self.uni_id, self.power,
                        self.hp, self.mp, self.dmg, self.pwr, self.defense, self.agl)
        clone.courses_taken = dict(self.courses_taken)
        return clone

class Minion:
    def __init__(self, hp, mdmg, rdmg, immunities, index):
        self.name = f"Minion {index}"
        self.hp = hp
        self.max_hp = hp
        self.mdmg = mdmg
        self.rdmg = rdmg
        self.immunities = immunities

class Villain:
    def __init__(self, name, vehicle_name, hp, mdmg, rdmg, nm, immunities, m_hp, m_mdmg, m_rdmg):
        self.name = name
        self.vehicle_name = vehicle_name
        self.hp = hp
        self.max_hp = hp
        self.mdmg = mdmg
        self.rdmg = rdmg
        self.nm = nm
        self.immunities = immunities
        self.minions = []
        self.m_hp = m_hp
        self.m_mdmg = m_mdmg
        self.m_rdmg = m_rdmg
        for index in range(nm):
            self.minions.append(Minion(m_hp, m_mdmg, m_rdmg, immunities, index + 1))

    def clone(self):
        return Villain(self.name, self.vehicle_name, self.hp, self.mdmg,
                       self.rdmg, self.nm, self.immunities, self.m_hp, self.m_mdmg, self.m_rdmg)

class Mission:
    def __init__(self, country, city, villain, prize):
        self.country = country
        self.city = city
        self.villain = villain
        self.prize = prize

    def clone(self):
        return Mission(self.country, self.city, self.villain.clone(), self.prize)
