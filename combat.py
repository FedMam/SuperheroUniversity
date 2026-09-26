"""Combat resolution and win-probability prediction."""

import math
from typing import List

from colorama import Fore, Style

from constants import ENEMY_BUFFS, POWER_CLASSES, POWER_COLORS, TEAM_BUFFS, ENABLE_BATTLE_PREDICTIONS
from models import Mission, Student

def _apply_team_buffs(heroes: List[Student]):
    for teammate in heroes:
        power = teammate.power
        if power not in TEAM_BUFFS:
            continue
        stat, factor = TEAM_BUFFS[power]
        
        for hero in heroes:
            if stat == 'hp' or stat == 'all':
                hero.hp = math.floor(hero.hp * (1 + factor))
                hero.max_hp = math.floor(hero.max_hp * (1 + factor))
            if stat == 'mp' or stat == 'all':
                hero.mp = math.floor(hero.mp * (1 + factor))
                hero.max_mp = math.floor(hero.max_mp * (1 + factor))
            if stat == 'dmg' or stat == 'all':
                hero.dmg = math.floor(hero.dmg * (1 + factor))
            if stat == 'pwr' or stat == 'all':
                hero.pwr = math.floor(hero.pwr * (1 + factor))
            if stat == 'def' or stat == 'all':
                hero.defense *= (1 + factor)
            if stat == 'agl' or stat == 'all':
                hero.agl *= (1 + factor)

def _apply_enemy_buffs(villains, heroes: List[Student]):
    for h in heroes:
        if h.power not in ENEMY_BUFFS:
            continue
        
        stat, factor = ENEMY_BUFFS[h.power]
        
        
        for v in villains:
            if stat == 'hp' or stat == 'all':
                v.hp = math.floor(v.hp * (1 - factor))
                v.max_hp = math.floor(v.max_hp * (1 - factor))
            if stat == 'mdmg' or stat == 'all':
                v.mdmg = math.floor(v.mdmg * (1 - factor))
            if stat == 'rdmg' or stat == 'all':
                v.rdmg = math.floor(v.rdmg * (1 - factor))

def _apply_mind_defection(mission: Mission, heroes: List[Student], rand, verbose: bool=False):
    for _ in (h for h in heroes if h.power == 'Mind'):
        for mn in mission.villain.minions:
            if mn.hp > 0 and rand.random() < 0.20:
                mn.hp = 0
                if verbose:
                    print(f'{Style.BRIGHT}{mn.name}{Style.RESET_ALL} defects and leaves the battle!')

def _lowest_hp_enemy(mission: Mission):
    alive_minions = [m for m in mission.villain.minions if m.hp > 0]
    if alive_minions:
        return min(alive_minions, key=lambda m: m.hp)
    if mission.villain.hp > 0:
        return mission.villain
    return None

def _attack_uses_super(hero: Student, target, mission: Mission, heroes: List[Student]) -> bool:
    if hero.mp <= 0 or hero.power in mission.villain.immunities or hero.pwr <= hero.dmg:
        return False
    # Attacking the main villain, or the hero is in trouble.
    if target == mission.villain or hero.hp < hero.max_hp / 2:
        return True
    # Even spending 1 MP now, the remaining Attack-power burst of the team
    # (that the villain is not immune to) still out-damages the villain's HP.
    pool = sum(
        ((h.mp if h is not hero else hero.mp - 1) * h.pwr)
        for h in heroes
        if h.hp > 0 and POWER_CLASSES[h.power] == 'Attack'
        and h.power not in mission.villain.immunities
    )
    return pool > mission.villain.hp

def _heal_decision(hero: Student, mission: Mission, heroes: List[Student]):
    # Returns (should_heal, target) or (False, None).
    if hero.mp <= 0 or hero.power in mission.villain.immunities:
        return False, None
    injured = [h for h in heroes if h.hp > 0 and h.hp < h.max_hp - hero.pwr * 3 // 4]
    if not injured:
        return False, None
    only_villain_left = not [m for m in mission.villain.minions if m.hp > 0]
    anyone_critical = any(h.hp < h.max_hp // 2 for h in heroes if h.hp > 0)
    if not (only_villain_left or anyone_critical):
        return False, None
    critical = [h for h in injured if h.hp < h.max_hp // 2]
    if critical:
        target = min(critical, key=lambda h: h.hp)
    else:
        target = min(injured, key=lambda h: h.hp)
    return True, target

def run_mission(mission: Mission, heroes: List[Student], rand, verbose: bool=False):
    if not heroes:
        if verbose:
            print(f'--- Mission in {mission.city}! ---')
            print(f'--- No heroes assigned, mission FAILED! ---\n')
        return False, []

    villains = [mission.villain] + mission.villain.minions
    dead_heroes = []

    snapshot = {}
    for h in heroes:
        snapshot[h] = (h.hp, h.max_hp, h.mp, h.max_mp, h.dmg, h.pwr, h.defense, h.agl)

    _apply_team_buffs(heroes)
    _apply_enemy_buffs(villains, heroes)
    _apply_mind_defection(mission, heroes, rand, verbose)

    time_revives = sum(1 for h in heroes if h.power == 'Time')
    revived = set()

    if verbose:
        print(f'--- Mission in {mission.city}! ---')
        for h in heroes:
            print(f"{h.superhero_name}: HP {h.max_hp}, MP {h.max_mp}, DMG {h.dmg}, PWR {h.pwr}, DEF {h.defense:.2f}, AGL {h.agl:.2f}")
        print('--- VERSUS ---')
        print(f"{mission.villain.name}: HP {mission.villain.max_hp}")
        if len(mission.villain.minions) > 0:
            print(f"{len(mission.villain.minions)} minions: HP {mission.villain.minions[0].max_hp}")
        print('--- FIGHT! ---')

    turn = 0
    while True:
        alive_villains = [v for v in villains if v.hp > 0]
        alive_heroes = [h for h in heroes if h.hp > 0]

        if not alive_villains:
            for h in heroes:
                h.hp, h.max_hp, h.mp, h.max_mp, h.dmg, h.pwr, h.defense, h.agl = snapshot[h]
            if verbose:
                print(f'--- All villains are dead, mission SUCCESS! ---\n')
            return True, dead_heroes

        if not alive_heroes:
            for h in heroes:
                h.hp, h.max_hp, h.mp, h.max_mp, h.dmg, h.pwr, h.defense, h.agl = snapshot[h]
            if verbose:
                print(f'--- All heroes are dead, mission FAILED! ---\n')
            return False, dead_heroes

        # Heroes turn
        for hero in alive_heroes:
            if hero.hp <= 0:
                continue

            class_ = POWER_CLASSES[hero.power]
            hero_name = f'{Style.BRIGHT}{hero.superhero_name}{Style.RESET_ALL}'
            pwr_color = POWER_COLORS[hero.power]

            if class_ == 'Attack':
                target = _lowest_hp_enemy(mission)
                if target is None:
                    continue
                use_super = _attack_uses_super(hero, target, mission, heroes)
                if use_super:
                    if hero.power == 'Ice' and not getattr(target, 'iced', False):
                        target.mdmg = math.ceil(target.mdmg / 2)
                        target.rdmg = math.ceil(target.rdmg / 2)
                        target.iced = True
                    target.hp -= hero.pwr
                    hero.mp -= 1
                    t_name = f'{Style.BRIGHT}{target.name}{Style.RESET_ALL}'
                    if verbose:
                        print(f"{hero_name} uses {pwr_color}{hero.power}{Style.RESET_ALL} on {t_name} for {hero.pwr} damage! Remaining HP: {target.hp}")
                else:
                    target.hp -= hero.dmg
                    t_name = f'{Style.BRIGHT}{target.name}{Style.RESET_ALL}'
                    if verbose:
                        print(f"{hero_name} punches {t_name} for {hero.dmg} damage! Remaining HP: {target.hp}")

            elif class_ == 'Heal':
                should_heal, heal_target = _heal_decision(hero, mission, heroes)
                if should_heal:
                    healed = min(hero.pwr, heal_target.max_hp - heal_target.hp)
                    heal_target.hp += healed
                    hero.mp -= 1
                    t_name = f'{Style.BRIGHT}{heal_target.superhero_name}{Style.RESET_ALL}'
                    if verbose:
                        print(f"{hero_name} uses {pwr_color}{hero.power}{Style.RESET_ALL} to heal {t_name} for {healed} HP! Remaining HP: {heal_target.hp}")
                else:
                    target = _lowest_hp_enemy(mission)
                    if target is None:
                        continue
                    target.hp -= hero.dmg
                    t_name = f'{Style.BRIGHT}{target.name}{Style.RESET_ALL}'
                    if verbose:
                        print(f"{hero_name} punches {t_name} for {hero.dmg} damage! Remaining HP: {target.hp}")

            else:  # Splash
                use_super = hero.mp > 0 and hero.power not in mission.villain.immunities and (len(alive_villains) > 1 or hero.pwr > hero.dmg)
                if use_super:
                    targets = [v for v in villains if v.hp > 0]
                    for target in targets:
                        target.hp -= hero.pwr
                    hero.mp -= 1
                    if verbose:
                        print(f"{hero_name} uses {pwr_color}{hero.power}{Style.RESET_ALL} on ALL enemies for {hero.pwr} damage each!")
                else:
                    target = _lowest_hp_enemy(mission)
                    if target is None:
                        continue
                    target.hp -= hero.dmg
                    t_name = f'{Style.BRIGHT}{target.name}{Style.RESET_ALL}'
                    if verbose:
                        print(f"{hero_name} punches {t_name} for {hero.dmg} damage! Remaining HP: {target.hp}")

            if mission.villain.hp <= 0 and mission.villain in alive_villains:
                if verbose:
                    print(f'{Style.BRIGHT}{mission.villain.name}{Style.RESET_ALL} is dead!')
                alive_villains.remove(mission.villain)
            for mn in mission.villain.minions:
                if mn.hp <= 0 and mn in alive_villains:
                    if verbose:
                        print(f'{Style.BRIGHT}{mn.name}{Style.RESET_ALL} is dead!')
                    alive_villains.remove(mn)

        if not alive_villains:
            for h in heroes:
                h.hp, h.max_hp, h.mp, h.max_mp, h.dmg, h.pwr, h.defense, h.agl = snapshot[h]
            if verbose:
                print(f'--- All villains are dead, mission SUCCESS! ---\n')
            return True, dead_heroes

        # Villains turn
        for v in alive_villains:
            if v.hp <= 0:
                continue
            alive_heroes_now = [h for h in heroes if h.hp > 0]
            if not alive_heroes_now:
                break
            target = rand.choice(alive_heroes_now)

            v_name = f'{Style.BRIGHT}{v.name}{Style.RESET_ALL}'
            target_name = f'{Style.BRIGHT}{target.superhero_name}{Style.RESET_ALL}'

            if rand.choice([True, False]):  # Melee
                damage = math.ceil(v.mdmg / target.defense)
                target.hp -= damage
                if verbose:
                    print(f"{v_name} uses melee attack on {target_name} for {damage} damage! Remaining HP: {target.hp}")
            else:  # Ranged
                if rand.random() < 1 / target.agl:
                    target.hp -= v.rdmg
                    if verbose:
                        print(f"{v_name} uses ranged attack on {target_name} for {v.rdmg} damage! Remaining HP: {target.hp}")
                else:
                    if verbose:
                        print(f"{v_name} uses ranged attack on {target_name} but MISSES!")

            if target.hp <= 0:
                if time_revives > 0 and target not in revived:
                    revived.add(target)
                    time_revives -= 1
                    target.hp = target.max_hp / 2
                    if verbose:
                        print(f'{target_name} gains one more chance at half health ({round(target.hp)} HP)!')
                else:
                    if verbose:
                        print(f'{target_name} is dead!')
                    dead_heroes.append(target)

        if not [h for h in heroes if h.hp > 0]:
            for h in heroes:
                h.hp, h.max_hp, h.mp, h.max_mp, h.dmg, h.pwr, h.defense, h.agl = snapshot[h]
            if verbose:
                print(f'--- All heroes are dead, mission FAILED! ---\n')
            return False, dead_heroes

        turn += 1


MONTE_CARLO = 100
def monte_carlo_predict(mission: Mission, heroes: List[Student], rand, monte_carlo: int=MONTE_CARLO) -> float:
    if not heroes:
        return 0.0

    sum_results = 0
    for i in range(monte_carlo):
        success, dead = run_mission(mission.clone(), [h.clone() for h in heroes], rand, verbose=False)
        result = 0 if not success else (1.0 - len(dead) / len(heroes))

        sum_results += result

    return sum_results / monte_carlo

def format_prediction(chance: float, n_assigned: int) -> str:
    assigned_str = '1 hero' if n_assigned == 1 else f'{n_assigned} heroes'

    if ENABLE_BATTLE_PREDICTIONS:
        if chance < 0.1:
            return f'{Style.DIM}{Fore.RED}[{assigned_str}|{round(chance * 100)}% SUICIDAL]{Style.RESET_ALL}'
        elif chance < 0.25:
            return f'{Fore.RED}[{assigned_str}|{round(chance * 100)}% HOPELESS]{Style.RESET_ALL}'
        elif chance < 0.5:
            return f'{Style.DIM}{Fore.YELLOW}[{assigned_str}|{round(chance * 100)}% RISKY]{Style.RESET_ALL}'
        elif chance < 0.75:
            return f'{Style.DIM}{Fore.LIGHTYELLOW_EX}[{assigned_str}|{round(chance * 100)}% DECENT]{Style.RESET_ALL}'
        elif chance < 0.9:
            return f'{Fore.LIGHTYELLOW_EX}[{assigned_str}|{round(chance * 100)}% GOOD]{Style.RESET_ALL}'
        else:
            return f'{Fore.LIGHTGREEN_EX}[{assigned_str}|{round(chance * 100)}% CERTAIN]{Style.RESET_ALL}'
    else:
        return f'{Style.DIM}[{assigned_str}]{Style.RESET_ALL}'
