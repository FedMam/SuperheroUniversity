"""Constants and game balance values."""

from colorama import Fore, init

init(autoreset=True)

# ==========================================
# CONSTANTS (Easily adjustable for balance)
# ==========================================
START_YEAR = 2040                     # the first semester of the game is Fall 2040
TOTAL_TURNS = 48                      # 24 years, two semesters per year
TURNS_PER_YEAR = 2                    # each turn is one semester: Fall or Spring
SEMESTERS = ['Fall', 'Spring']
END_YEAR = START_YEAR + (TOTAL_TURNS - 1) // TURNS_PER_YEAR  # 2063: year of the last semester
MIN_TURNS_TO_GRADUATE = 8             # a student needs 8 semesters (4 years) of study
INITIAL_MONEY = 100
INITIAL_STUDENTS = 3
INITIAL_MISSIONS = 3                  # missions are always 3 now
MAX_STUDENTS = 21                     # dormitory capacity
MAX_MISSION_FAILS = 5

STUDENT_BASE_COST = 25
STUDENT_COST_INCREASE = 25

COURSE_BASE_COST = 10
COURSE_COST_INCREASE = 10             # courses grow by $10 with each buy
MAX_COURSES_PER_STAT = 10             # a student cannot buy more than this many courses of the same kind

# Six stat courses (variable display names).
COURSE_STATS = ['HP', 'MP', 'DMG', 'PWR', 'DEF', 'AGL']

# ==========================================
# SUPERPOWERS
# ==========================================
SUPERPOWERS = [
    "Strength", "Flight", "Speed", "Fire", "Slash",
    "Electric", "Laser", "Tech", "Solar", "Weather",
    "Nature", "Shield", "Elastic", "Energy", "Water",
    "Ice", "Acid", "Mind", "Gravity", "Time", "Cyber",
    "Sonic",
]

POWER_CLASSES = {
    "Strength": "Attack", "Flight": "Attack", "Speed": "Splash",
    "Fire": "Splash", "Slash": "Attack", "Electric": "Attack",
    "Laser": "Attack", "Tech": "Attack", "Solar": "Attack",
    "Weather": "Splash", "Nature": "Heal", "Shield": "Heal",
    "Elastic": "Attack", "Energy": "Heal", "Water": "Heal",
    "Ice": "Attack", "Acid": "Splash", "Mind": "Attack",
    "Gravity": "Splash", "Time": "Heal", "Cyber": "Splash",
    "Sonic": "Splash",
}

# Unique two-letter codes used to display powers in the immunities list.
POWER_CODES = {
    "Strength": "St", "Flight": "Fl", "Speed": "Sp", "Fire": "Fi",
    "Slash": "Sl", "Electric": "Ec", "Laser": "La", "Tech": "Te",
    "Solar": "So", "Weather": "We", "Nature": "Na", "Shield": "Sh",
    "Elastic": "El", "Energy": "En", "Water": "Wa", "Ice": "Ic",
    "Acid": "Ac", "Mind": "Mi", "Gravity": "Gr", "Time": "Ti",
    "Cyber": "Cy", "Sonic": "Sn",
}
CODE_TO_POWER = {code: power for power, code in POWER_CODES.items()}

POWER_COLORS = {
    "Strength": Fore.LIGHTMAGENTA_EX,
    "Speed": Fore.LIGHTGREEN_EX,
    "Flight": Fore.CYAN,
    "Fire": Fore.LIGHTRED_EX,
    "Slash": Fore.RED,
    "Electric": Fore.LIGHTYELLOW_EX,
    "Laser": Fore.MAGENTA,
    "Tech": Fore.WHITE,
    "Solar": Fore.YELLOW,
    "Weather": Fore.LIGHTBLACK_EX,
    "Nature": Fore.GREEN,
    "Shield": Fore.CYAN,
    "Elastic": Fore.LIGHTMAGENTA_EX,
    "Energy": Fore.LIGHTYELLOW_EX,
    "Water": Fore.LIGHTBLUE_EX,
    "Ice": Fore.LIGHTCYAN_EX,
    "Acid": Fore.LIGHTGREEN_EX,
    "Mind": Fore.LIGHTRED_EX,
    "Gravity": Fore.LIGHTBLACK_EX,
    "Time": Fore.WHITE,
    "Cyber": Fore.LIGHTGREEN_EX,
    "Sonic": Fore.LIGHTCYAN_EX,
}

# Power class defaults for PWR.
PWR_BASE = {"Attack": 20, "Heal": 20, "Splash": 5}
PWR_GROWTH_DEFAULT = {"Attack": 10, "Heal": 10, "Splash": 4}

# Default per-course stat growth (PWR depends on class, handled separately).
COURSE_GROWTH_DEFAULT = {"HP": 25, "MP": 1, "DMG": 4, "DEF": 0.2, "AGL": 0.2}

# Per-power overrides for per-course growth.
POWER_GROWTHS = {
    "Strength": {"DMG": 8, "AGL": 0.1},
    "Speed": {"AGL": 1.0, "DMG": 2, "DEF": 0.1},
    "Flight": {"DEF": 1.0, "DMG": 2, "AGL": 0.1},
    "Fire": {"PWR": 6},
    "Slash": {"DMG": 6},
    "Laser": {"PWR": 15},
    "Tech": {"HP": 30, "DEF": 0.3},
    "Solar": {"PWR": 30, "HP": 10},
    "Nature": {"HP": 50},
    "Shield": {"DEF": 0.5},
    "Elastic": {"AGL": 0.5},
}

# Buffs applied to the whole hero team at mission start (stat, factor).
TEAM_BUFFS = {
    "Electric": ("pwr", 0.25),
    "Weather": ("mp", 0.5),
    "Nature": ("hp", 0.25),
    "Shield": ("def", 0.25),
    "Elastic": ("agl", 0.25),
    "Sonic": ("dmg", 0.25),
    "Energy": ("all", 0.10),
}

# Debuffs applied to the whole enemy team at mission start (stat, factor).
ENEMY_BUFFS = {
    "Acid": ("hp", 0.25),
    "Water": ("mdmg", 0.25),
    "Gravity": ("rdmg", 0.25),
    "Cyber": ("all", 0.10),
}

SHOW_BATTLE_PROGRESS = True

# Monte-Carlo battle outcome prediction is expensive: when False it is neither
# calculated nor displayed anywhere in the game.
ENABLE_BATTLE_PREDICTIONS = False

SAVE_FILE_NAME = 'superhero_university_state.txt'
