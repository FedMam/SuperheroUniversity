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
    "Sonic", "Nuclear", "Portal",
]

POWER_CLASSES = {
    "Strength": "Attack", "Flight": "Attack", "Speed": "Splash",
    "Fire": "Splash", "Slash": "Attack", "Electric": "Attack",
    "Laser": "Attack", "Tech": "Attack", "Solar": "Attack",
    "Weather": "Splash", "Nature": "Heal", "Shield": "Heal",
    "Elastic": "Attack", "Energy": "Heal", "Water": "Heal",
    "Ice": "Attack", "Acid": "Splash", "Mind": "Attack",
    "Gravity": "Splash", "Time": "Heal", "Cyber": "Splash",
    "Sonic": "Splash", "Nuclear": "Splash", "Portal": "Attack",
}

# Unique two-letter codes used to display powers in the immunities list.
POWER_CODES = {
    "Strength": "St", "Flight": "Fl", "Speed": "Sp", "Fire": "Fi",
    "Slash": "Sl", "Electric": "Ec", "Laser": "La", "Tech": "Te",
    "Solar": "So", "Weather": "We", "Nature": "Na", "Shield": "Sh",
    "Elastic": "El", "Energy": "En", "Water": "Wa", "Ice": "Ic",
    "Acid": "Ac", "Mind": "Mi", "Gravity": "Gr", "Time": "Ti",
    "Cyber": "Cy", "Sonic": "Sn", "Nuclear": "Nu", "Portal": "Po",
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
    "Nuclear": Fore.LIGHTYELLOW_EX,
    "Portal": Fore.MAGENTA,
}

# Power class defaults for PWR.
PWR_BASE = {"Attack": 20, "Heal": 20, "Splash": 5}
PWR_GROWTH_DEFAULT = {"Attack": 10, "Heal": 10, "Splash": 4}

# Default per-course stat growth (PWR depends on class, handled separately).
COURSE_GROWTH_DEFAULT = {"HP": 25, "MP": 1, "DMG": 4, "DEF": 0.2, "AGL": 0.2}

# Per-power overrides for per-course growth.
POWER_GROWTHS = {
    "Strength": {"DMG": 8, 'PWR': 12, "AGL": 0.1},
    "Speed": {"AGL": 1.0, "DMG": 2, "DEF": 0.1},
    "Flight": {"DEF": 1.0, "DMG": 2, "AGL": 0.1},
    "Fire": {"PWR": 6},
    "Slash": {"DMG": 6},
    "Laser": {"PWR": 15},
    "Tech": {"HP": 30, "DEF": 0.3, 'AGL': 0.15},
    "Solar": {"PWR": 30, "HP": 10},
    "Nature": {"HP": 50},
    "Shield": {"DEF": 0.5},
    "Elastic": {"AGL": 0.5},
    "Nuclear": {"PWR": 15, "HP": 10},
}

# Story-wise and gameplay-wise descriptions shown in the Superpower Encyclopedia.
POWER_DESCRIPTIONS = {
    "Strength": {
        "story": "Raw muscle that can lift tanks and level buildings.",
        "gameplay": "Super-attack deals PWR damage to the weakest enemy. Courses boost DMG (+8), PWR (+12) and AGL (+0.1) per buy.",
    },
    "Flight": {
        "story": "Soars above the battlefield on wings of light.",
        "gameplay": "Super-attack deals PWR damage to the weakest enemy. Courses boost DEF (+1.0), DMG (+2) and AGL (+0.1) per buy.",
    },
    "Speed": {
        "story": "Moves faster than the eye can follow.",
        "gameplay": "Super-attack deals PWR damage to ALL enemies. Courses boost AGL (+1.0), DMG (+2) and DEF (+0.1) per buy.",
    },
    "Fire": {
        "story": "Engulfs the field in roaring flame.",
        "gameplay": "Super-attack deals PWR damage to ALL enemies. Courses boost PWR (+6) per buy.",
    },
    "Slash": {
        "story": "Razor claws and blade arcs that cut through armor.",
        "gameplay": "Super-attack deals PWR damage to the weakest enemy. Courses boost DMG (+6) per buy.",
    },
    "Electric": {
        "story": "Channels lightning through every nerve.",
        "gameplay": "Super-attack deals PWR damage to the weakest enemy. TEAM BUFF: +25% PWR to all heroes at mission start.",
    },
    "Laser": {
        "story": "Fires focused beams of coherent light.",
        "gameplay": "Super-attack deals PWR damage to the weakest enemy. Courses boost PWR (+15) per buy.",
    },
    "Tech": {
        "story": "An arsenal of gadgets, drones and improvised devices.",
        "gameplay": "Super-attack deals PWR damage to the weakest enemy. Courses boost HP (+30), DEF (+0.3) and AGL (+0.15) per buy.",
    },
    "Solar": {
        "story": "Draws on the blinding power of the sun.",
        "gameplay": "Super-attack deals PWR damage to the weakest enemy. Courses boost PWR (+30) and HP (+10) per buy.",
    },
    "Weather": {
        "story": "Commands storm, wind and rain at will.",
        "gameplay": "Super-attack deals PWR damage to ALL enemies. TEAM BUFF: +50% MP to all heroes at mission start.",
    },
    "Nature": {
        "story": "Commune with living things; their energy mends flesh.",
        "gameplay": "Super-attack heals a teammate by PWR. Courses boost HP (+50). TEAM BUFF: +25% HP to all heroes at mission start.",
    },
    "Shield": {
        "story": "Projects barriers of solid force.",
        "gameplay": "Super-attack heals a teammate by PWR. Courses boost DEF (+0.5). TEAM BUFF: +25% DEF to all heroes at mission start.",
    },
    "Elastic": {
        "story": "Stretches and reshapes the body at will.",
        "gameplay": "Super-attack deals PWR damage to the weakest enemy. Courses boost AGL (+0.5). TEAM BUFF: +25% AGL to all heroes at mission start.",
    },
    "Energy": {
        "story": "Channels pure life force into allies.",
        "gameplay": "Super-attack heals a teammate by PWR. TEAM BUFF: +10% to ALL stats of every hero at mission start.",
    },
    "Water": {
        "story": "Bends the tides to wash away the enemy's strength.",
        "gameplay": "Super-attack heals a teammate by PWR. ENEMY DEBUFF: -25% melee damage to all enemies at mission start.",
    },
    "Ice": {
        "story": "Freezes foes to the bone.",
        "gameplay": "Super-attack deals PWR damage to the weakest enemy and halves the victim's melee and ranged damage (once per target).",
    },
    "Acid": {
        "story": "Dissolves armor and flesh alike.",
        "gameplay": "Super-attack deals PWR damage to ALL enemies. ENEMY DEBUFF: -25% HP to all enemies at mission start.",
    },
    "Mind": {
        "story": "Telepathic control over weaker wills.",
        "gameplay": "Super-attack deals PWR damage to the weakest enemy. SPECIAL: each Mind hero has a 20% chance per minion to make it defect and fight for the heroes.",
    },
    "Gravity": {
        "story": "Crushes enemies under their own weight.",
        "gameplay": "Super-attack deals PWR damage to ALL enemies. ENEMY DEBUFF: -25% ranged damage to all enemies at mission start.",
    },
    "Time": {
        "story": "Rewinds a hero's final moment.",
        "gameplay": "Super-attack heals a teammate by PWR. SPECIAL: each Time hero grants the team one revival at half HP (defected minions are not revived).",
    },
    "Cyber": {
        "story": "Hacks villain technology in real time.",
        "gameplay": "Super-attack deals PWR damage to ALL enemies. ENEMY DEBUFF: -10% to ALL stats of every enemy at mission start.",
    },
    "Sonic": {
        "story": "Unleashes deafening shockwaves.",
        "gameplay": "Super-attack deals PWR damage to ALL enemies. TEAM BUFF: +25% DMG to all heroes at mission start.",
    },
    "Nuclear": {
        "story": "Unleashes controlled atomic blasts.",
        "gameplay": "Super-attack deals PWR damage to ALL enemies. Courses boost PWR (+15) and HP (+10) per buy.",
    },
    "Portal": {
        "story": "Opens gateways through space.",
        "gameplay": "Super-attack deals PWR damage to the weakest enemy. SPECIAL: the super-attack strikes the main villain directly, bypassing minions.",
    },
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
