"""Save and load the game state."""

from constants import (
    COURSE_STATS,
    CODE_TO_POWER,
    INITIAL_MONEY,
    INITIAL_STUDENTS,
    POWER_CODES,
    SAVE_FILE_NAME,
    SUPERPOWERS,
)
from models import Mission, Student, Villain
from utils import accept_candidate, generate_candidate, generate_missions

def save_state(month, money, total_failed_missions, n_of_dead_students, students, missions, filename=SAVE_FILE_NAME):
    file = open(filename, 'w')

    file.write(f'{month} {money} {total_failed_missions} {n_of_dead_students}\n{len(students)}\n')
    for s in students:
        file.write(f'{s.uni_id},{s.superhero_name},{s.gender},{s.real_name},{s.nation},{s.power},'
                   f'{s.hp},{s.mp},{s.dmg},{s.pwr},{s.defense},{s.agl},')
        for i, stat in enumerate(COURSE_STATS):
            file.write(f'{s.courses_taken[stat]}')
            if i < len(COURSE_STATS) - 1:
                file.write(',')

        file.write('\n')

    file.write(f'{len(missions)}\n')
    for m in missions:
        m: Mission
        file.write(f'{m.city},{m.country},{m.villain.name},{m.villain.vehicle_name},{m.villain.hp},{m.villain.mdmg},{m.villain.rdmg},')
        file.write(''.join(POWER_CODES[im] for im in m.villain.immunities) + ',')
        if not m.villain.minions:
            file.write('0,0,0,0,')
        else:
            mi = m.villain.minions[0]
            file.write(f'{len(m.villain.minions)},{mi.hp},{mi.mdmg},{mi.rdmg},')
        file.write(f'{m.prize}\n')

    file.close()

def load_state(rand, filename=SAVE_FILE_NAME, default: bool=False):
    try:
        file = open(filename, 'r')
    except IOError:
        default = True

    students = []
    if default:
        # Generate initial students
        for _ in range(INITIAL_STUDENTS):
            accept_candidate(rand, generate_candidate(rand), students)
        # Generate initial missions
        missions = generate_missions(0, rand)
        return 0, INITIAL_MONEY, 0, students, missions, 0

    missions = []
    month, money, total_failed_missions, n_of_dead_students = map(int, file.readline().split(' '))
    n_students = int(file.readline())

    for i in range(n_students):
        line = file.readline().split(',')
        uni_id, hero_name, gender, real_name, nation, power = line[:6]
        hp, mp, dmg, pwr = map(int, line[6:10])
        defense = float(line[10])
        agl = float(line[11])
        s = Student(nation, gender, real_name, hero_name, uni_id, power, hp, mp, dmg, pwr, defense, agl)
        for i, stat in enumerate(COURSE_STATS):
            s.courses_taken[stat] = int(line[12 + i])
        students.append(s)

    n_missions = int(file.readline())
    for i in range(n_missions):
        line = file.readline().split(',')
        city, nation, v_name, vehicle_name = line[:4]
        v_hp, v_mdmg, v_rdmg = map(int, line[4:7])
        immunities_codes = line[7]
        nm, m_hp, m_mdmg, m_rdmg, prize = map(int, line[8:13])
        immunities = []
        for j in range(0, len(immunities_codes), 2):
            code = immunities_codes[j:j+2]
            if code in CODE_TO_POWER:
                immunities.append(CODE_TO_POWER[code])
        missions.append(Mission(
            nation, city, Villain(
                v_name, vehicle_name, v_hp, v_mdmg, v_rdmg, nm,
                immunities, m_hp, m_mdmg, m_rdmg,
            ), prize
        ))

    file.close()
    return month, money, total_failed_missions, students, missions, n_of_dead_students