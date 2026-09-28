"""Shared helpers used across the game."""

import math
import os
import random
import subprocess

from colorama import Fore, Style

from combat import format_prediction
from constants import (
    COURSE_BASE_COST,
    COURSE_COST_INCREASE,
    COURSE_GROWTH_DEFAULT,
    COURSE_STATS,
    ENABLE_BATTLE_PREDICTIONS,
    INITIAL_MISSIONS,
    MAX_COURSES_PER_STAT,
    POWER_CLASSES,
    POWER_CODES,
    POWER_COLORS,
    POWER_GROWTHS,
    PWR_BASE,
    PWR_GROWTH_DEFAULT,
    SEMESTERS,
    START_YEAR,
    SUPERPOWERS,
    TURNS_PER_YEAR,
)
from models import Mission, Student, Villain
from names import (
    COURSE_NAMES,
    POWER_COURSE_NAMES,
    generate_country_and_city,
    generate_nation,
    generate_real_name,
    generate_superhero_name,
    generate_supervillain_name,
)

# ==========================================
# HELPERS
# ==========================================
rand = random.Random()

def get_int_input(prompt, min_val=None, max_val=None):
    while True:
        try:
            val = int(input(prompt))
            if min_val is not None and val < min_val:
                print(f"Value must be at least {min_val}")
                continue
            if max_val is not None and val > max_val:
                print(f"Value must be at most {max_val}")
                continue
            return val
        except ValueError:
            print("Please enter a valid integer.")

def format_immunities(immunities):
    if not immunities:
        return "None"
    res = "["
    for p in immunities:
        res += POWER_COLORS[p] + POWER_CODES[p] + Style.RESET_ALL
    res += "]"
    return res

def semester_label(turn: int) -> str:
    """'Fall 2040' for the 1st turn, 'Spring 2040' for the 2nd, and so on."""
    year = START_YEAR + turn // TURNS_PER_YEAR
    return f'{SEMESTERS[turn % TURNS_PER_YEAR]} {year}'

def display_study_progress(s) -> str:
    if s.can_graduate():
        return f'{Style.BRIGHT}{Fore.GREEN}can graduate{Style.RESET_ALL}'
    return f'graduates in {s.turns_to_graduate()} more semester(s)'

def display_final_score(n_of_graduated_students: int, n_of_dead_students: int) -> None:
    """Final score: students graduated minus students lost."""
    score = n_of_graduated_students - n_of_dead_students
    print(f"\nGraduated students: {n_of_graduated_students} | Dead students: {n_of_dead_students}")
    if score >= 0:
        score_str = f'{Style.BRIGHT}{Fore.GREEN}{score}{Style.RESET_ALL}'
    else:
        score_str = f'{Style.BRIGHT}{Fore.RED}{score}{Style.RESET_ALL}'
    print(f'FINAL SCORE: {n_of_graduated_students} graduated - {n_of_dead_students} dead = {score_str}')

# ==========================================
# STUDENT GENERATION
# ==========================================
def generate_stats(gender, power, rand):
    """Generate base (zero-course) stats for a student."""
    hp = (50 if gender == 'male' else 90) + 10 * rand.randint(0, 6)
    mp = rand.randint(0, 3)
    dmg = rand.randint(8, 24) if gender == 'male' else rand.randint(1, 10)
    pwr = rand.randint(1, PWR_BASE[POWER_CLASSES[power]] // 5) * 5
    defense = rand.random() / 2 + 1
    agl = rand.random() / 2 + 1
    return hp, mp, dmg, pwr, defense, agl

def generate_candidate(rand):
    """Create a prospective student (no uni_id yet)."""
    nation = generate_nation(rand)
    gender = rand.choice(['male', 'female'])
    real_name = generate_real_name(nation, gender, rand)
    power = rand.choice(SUPERPOWERS)
    hero_name = generate_superhero_name(gender, power, rand)
    hp, mp, dmg, pwr, defense, agl = generate_stats(gender, power, rand)
    return Student(nation, gender, real_name, hero_name, None, power, hp, mp, dmg, pwr, defense, agl)

def _generate_uni_id(s, students, rand):
    used_fids = set(st.uni_id for st in students)
    hero_name_split = s.superhero_name.split(' ')
    candidate_fids = list(reversed([
        *[arg[:2].upper() for arg in sorted(hero_name_split, key=lambda arg: -len(arg)) if len(arg) >= 2 and arg[:2].isalpha()],
        *([''.join(it[0].upper() for it in s.real_name.split(' ')[:2])] if ' ' in s.real_name else [s.real_name[:2].upper()]),
        *[(s.superhero_name[0] + s.superhero_name[i]).upper() for i in range(1, len(s.superhero_name)) if s.superhero_name[i].isalpha()]
    ]))
    if len(hero_name_split) > 1:
        candidate_fids.insert(len(candidate_fids) - 1, (hero_name_split[0][0] + hero_name_split[1][0]).upper())
    while True:
        if len(candidate_fids) > 0:
            fid = candidate_fids.pop()
        else:
            fid = chr(ord('A') + rand.randint(0, 25)) + chr(ord('A') + rand.randint(0, 25))
        if fid not in used_fids:
            return fid

def accept_candidate(rand, candidate, students):
    if candidate.uni_id is None:
        candidate.uni_id = _generate_uni_id(candidate, students, rand)
    students.append(candidate)

def display_candidate(candidate, index, cost):
    power = POWER_COLORS[candidate.power] + candidate.power + Style.RESET_ALL
    print(f"{index}. {Style.BRIGHT}{candidate.superhero_name}{Style.RESET_ALL} ({candidate.real_name}) | {candidate.nation} | {power}")
    print(f"   HP: {candidate.max_hp} | MP: {candidate.max_mp} | DMG: {candidate.dmg} | "
          f"PWR: {candidate.pwr} | DEF: {candidate.defense:.2f} | AGL: {candidate.agl:.2f} | "
          f"Gender: {candidate.gender}")

def recruit_cost(students, n_of_dead_students):
    from constants import STUDENT_BASE_COST, STUDENT_COST_INCREASE
    return STUDENT_BASE_COST + STUDENT_COST_INCREASE * (len(students) + n_of_dead_students)

# ==========================================
# COURSES
# ==========================================
def course_growth(power, stat):
    if stat == 'PWR':
        return POWER_GROWTHS.get(power, {}).get(
            'PWR', PWR_GROWTH_DEFAULT[POWER_CLASSES[power]])
    return POWER_GROWTHS.get(power, {}).get(stat, COURSE_GROWTH_DEFAULT[stat])

def can_take_course(student, stat):
    """True if the student still has room for one more course of this kind."""
    return student.courses_taken[stat] < MAX_COURSES_PER_STAT

def course_cost(student, stat):
    """Price of the next course of this kind for this student."""
    return COURSE_BASE_COST + COURSE_COST_INCREASE * student.courses_taken[stat]

def course_price_for(students, stat):
    """Total price of buying this course for every student who can still take it."""
    return sum([course_cost(s, stat) for s in students if can_take_course(s, stat)])

def take_course(student, stat):
    if not can_take_course(student, stat):
        return False
    growth = course_growth(student.power, stat)
    if stat == 'HP':
        student.hp += growth
        student.max_hp += growth
    elif stat == 'MP':
        student.mp += growth
        student.max_mp += growth
    elif stat == 'DMG':
        student.dmg += growth
    elif stat == 'PWR':
        student.pwr += growth
    elif stat == 'DEF':
        student.defense += growth
    elif stat == 'AGL':
        student.agl += growth
    student.courses_taken[stat] += 1
    return True

def generate_course_names(rand):
    """Return (defaults, overrides) mapping course stats to display names."""
    defaults = {stat: rand.choice(COURSE_NAMES[stat]) for stat in COURSE_STATS}
    overrides = {}
    for power, stat_override in POWER_COURSE_NAMES.items():
        for stat, names in stat_override.items():
            overrides[(power, stat)] = rand.choice(names)
    return defaults, overrides

def get_course_name(course_names, stat, power):
    defaults, overrides = course_names
    return overrides.get((power, stat), defaults[stat])

# ==========================================
# DISPLAY
# ==========================================
def print_student_stats(s):
    power = POWER_COLORS[s.power] + s.power + Style.RESET_ALL
    print(f"   HP: {s.max_hp} | MP: {s.max_mp} | DMG: {s.dmg} | PWR: {s.pwr} | "
          f"DEF: {s.defense:.2f} | AGL: {s.agl:.2f} | Power: {power}")

def display_student(s):
    name = Style.BRIGHT + s.superhero_name + Style.RESET_ALL
    power = POWER_COLORS[s.power] + s.power + Style.RESET_ALL
    print(f"[{s.uni_id}] {name} ({s.real_name}) | {s.nation} | {power}")
    print(f"   HP: {s.max_hp} | MP: {s.max_mp} | DMG: {s.dmg} | PWR: {s.pwr} | "
          f"DEF: {s.defense:.2f} | AGL: {s.agl:.2f}")
    print(f"   Studied: {s.turns_studied} semester(s) | {display_study_progress(s)}")

def display_students(students, assignments={}):
    print("\n--- STUDENTS ---")
    if not students:
        print("No students enrolled.")
        return
    for s in students:
        display_student(s)
        if s.uni_id in assignments:
            m: Mission = assignments[s.uni_id]
            print(f'   {Fore.LIGHTRED_EX}On mission in {m.city} against {Style.BRIGHT}{m.villain.name}{Style.RESET_ALL}')

def display_missions(missions, assignments, predictions):
    print("\n--- MISSIONS ---")
    for i, m in enumerate(missions):
        v = m.villain
        v_name = Style.BRIGHT + v.name + Style.RESET_ALL
        print(f"{i+1}. {m.city}, {m.country} - Villain: {v_name}{v.vehicle_name}")
        print(f"   Villain: HP {v.hp} | MDMG {v.mdmg} | RDMG {v.rdmg} | "
              f"Immunities: {format_immunities(v.immunities)}", end='')
        assigned = sum([1 for s in assignments if assignments[s] == m])
        if assigned > 0:
            print(' ' + format_prediction(predictions[i], assigned), end='')
        print()
        if v.minions:
            max_hp = max(mn.hp for mn in v.minions)
            max_mdmg = max(mn.mdmg for mn in v.minions)
            max_rdmg = max(mn.rdmg for mn in v.minions)
            print(f"   Minions ({len(v.minions)}): HP {max_hp} | MDMG {max_mdmg} | RDMG {max_rdmg}")
        else:
            print(f"   Minions: None")
        print(f"   Prize: ${m.prize}")

# ==========================================
# MISSIONS
# ==========================================
MAX_MINIONS = 10
def generate_missions(turn, rand):
    missions = []

    turns_passed = turn
    max_hp = 50 + 50 * turns_passed
    max_mdmg = 4 + 4 * turns_passed
    max_rdmg = 4 + 4 * turns_passed
    max_nm = turns_passed // 3
    max_k = turns_passed // 4

    for _ in range(INITIAL_MISSIONS):
        country, city = generate_country_and_city(rand)
        v_name, vehicle_name = generate_supervillain_name(rand)

        v_hp = rand.randint(max_hp // 5, max_hp)
        v_mdmg = rand.randint(max_mdmg // 4, max_mdmg)
        v_rdmg = rand.randint(max_rdmg // 4, max_rdmg)
        nm = min(MAX_MINIONS, rand.randint(0, max_nm))

        k = min(len(SUPERPOWERS) - 1, rand.randint(0, max_k))
        immunities = [SUPERPOWERS[p_i] for p_i in sorted(rand.sample(list(range(len(SUPERPOWERS))), k))]

        divisor_hp = rand.randint(2, 5)
        divisor_mdmg = rand.randint(2, 5)
        divisor_rdmg = rand.randint(2, 5)
        m_hp = math.ceil(v_hp / divisor_hp)
        m_mdmg = math.ceil(v_mdmg / divisor_mdmg)
        m_rdmg = math.ceil(v_rdmg / divisor_rdmg)

        villain = Villain(v_name, vehicle_name, v_hp, v_mdmg, v_rdmg, nm, immunities, m_hp, m_mdmg, m_rdmg)

        total_hp = v_hp + m_hp * nm
        prize = rand.randint(round(v_hp / 3), round(v_hp * 2))

        missions.append(Mission(country, city, villain, prize))

    return missions

def clear_screen():
    subprocess.run("cls" if os.name == "nt" else "clear")
