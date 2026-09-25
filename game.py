"""Main game loop and entry logic."""

import time
from pathlib import Path

import readchar
from colorama import Fore, Style

from combat import format_prediction, monte_carlo_predict, run_mission
from constants import (
    COURSE_BASE_COST,
    COURSE_COST_INCREASE,
    COURSE_STATS,
    MAX_MISSION_FAILS,
    MAX_STUDENTS,
    POWER_COLORS,
    SAVE_FILE_NAME,
    SHOW_BATTLE_PROGRESS,
    START_YEAR,
    END_YEAR,
    STUDENT_BASE_COST,
    TOTAL_TURNS,
)
from models import Student
from storage import load_state, save_state
from utils import (
    accept_candidate,
    clear_screen,
    display_candidate,
    display_missions,
    display_student,
    display_students,
    generate_candidate,
    generate_course_names,
    generate_missions,
    get_course_name,
    get_int_input,
    print_student_stats,
    rand,
    recruit_cost,
    take_course,
)

def main():
    clear_screen()

    # Credit for ASCII art text generation: https://patorjk.com/software/taag
    print(r'''  _________                         .__                         
 /   _____/__ ________   ___________|  |__   ___________  ____  
 \_____  \|  |  \____ \_/ __ \_  __ \  |  \_/ __ \_  __ \/  _ \ 
 /        \  |  /  |_> >  ___/|  | \/   Y  \  ___/|  | \(  <_> )
/_______  /____/|   __/ \___  >__|  |___|  /\___  >__|   \____/ 
        \/      |__|        \/           \/     \/              
 ____ ___      .__                          .__  __             
|    |   \____ |__|__  __ ___________  _____|__|/  |_ ___.__.   
|    |   /    \|  \  \/ // __ \_  __ \/  ___/  \   __<   |  |   
|    |  /   |  \  |\   /\  ___/|  | \/\___ \|  ||  |  \___  |   
|______/|___|  /__| \_/  \___  >__|  /____  >__||__|  / ____|   
             \/              \/           \/          \/''')
    
    print('\nPress [ENTER] to continue: ')
    input()

    print(f'''You are the President of the International Superhero University. Supervillain activity is surging! Train your students and assign them to missions to save the world. The game starts in {START_YEAR}. Reach the year {END_YEAR} to win!

[ MONTHLY CYCLE ]
Each turn is ONE MONTH. Use your budget to prepare:
 - RECRUIT (,): Every turn 3 student candidates are generated. Review their stats and superpowers and enroll the ones you like (from $85, +$5 per faculty). The dormitory holds at most {MAX_STUDENTS} students; you can graduate a student to free up space.
 - TRAIN (.): Buy courses to boost stats (each buy costs $10, +$10 each time). Six stat courses: (+HP), (+MP), (+DMG), (+PWR), (+DEF), (+AGL). Course names change every turn!

[ SUPERPOWERS ]
Powers belong to three classes:
 - Attack: super-attack deals PWR damage to the weakest enemy.
 - Heal:   super-attack heals a teammate by PWR.
 - Splash: super-attack deals PWR damage to ALL enemies.
Powers also carry team-wide or enemy-wide side effects (buffs / debuffs).

[ MISSIONS & COMBAT ]
Always 3 missions per month. Assign students to stop supervillains. Combat is automatic:
 1. HEROES ACT FIRST: they choose when to spend MP efficiently.
 2. VILLAINS RETALIATE: melee damage is reduced by the hero's DEF; ranged attacks may miss depending on AGL.
Powers fail if the villain is IMMUNE to that superpower.

[ OUTCOMES ]
 - VICTORY: Earn prize money. Survivors' HP/MP are restored.
 - DEFEAT: Dead students are gone FOREVER. The mission fails.

[ GAME OVER ]
You lose if {MAX_MISSION_FAILS} missions fail, or if you have 0 students and no 
money to recruit new ones. Villains grow stronger every month!

================================================================
       Press [ENTER] to begin your presidency! Good luck!
================================================================''')
    input('')

    if Path(SAVE_FILE_NAME).is_file():
        default_state = input('Saved game detected. Continue saved game? (Y/n) ').lower() == 'n'
    else:
        default_state = True

    month, money, total_failed_missions, students, missions, n_of_dead_students = load_state(rand, default=default_state)
    candidates = [generate_candidate(rand) for _ in range(3)]
    course_names = generate_course_names(rand)

    # month loop
    while True:
        if month >= TOTAL_TURNS:
            print(f"\n=== MONTH {month} ===")
            print(f"Congratulations! You have guided the university to the year {END_YEAR}!")
            print("You WIN!")
            break

        def display_status_bar():
            months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
            date_string = f'{months[month % 12]} {START_YEAR + month // 12}'
            print(f"\n{'='*20} {date_string} {'='*(20 + 14 - len(date_string))}")
            print(f"Money: ${money} | Students: {len(students)}/{MAX_STUDENTS} | Failed Missions: {total_failed_missions}/{MAX_MISSION_FAILS}")

        current_action = 'idle'
        current_student = None
        last_managed_student = None
        assignments = {}
        predictions = [0.0 for _ in range(len(missions))]
        resigned = False

        # action loop
        while True:
            clear_screen()

            display_status_bar()
            display_students(students, assignments)
            display_missions(missions, assignments, predictions)

            print()
            if current_action == 'idle':
                print('Type the two letters of a student (for example, ID) to buy courses or assign to missions.')
                print('Press \' (single-quote) to select the next unassigned student.')
                print('Press ; (semicolon) to select the last managed student.')
                print('Press . (dot) to buy a course for all the students.')
                print('Press , (comma) to review new student candidates.')
                print('After all students have been assigned, press Enter to proceed.')
                print()
                print('Your command: ', end='')
                uni_id = ''
                if isinstance(current_student, str) and len(current_student) == 1:
                    print(current_student, end='')
                    uni_id = current_student

                try:
                    cmd = readchar.readkey().upper()
                except KeyboardInterrupt:
                    resigned = True
                    if input('\nSave game? (Y/n) ').lower() != 'n':
                        save_state(month, money, total_failed_missions, n_of_dead_students, students, missions)
                    else:
                        print("Game Over! You have resigned.")
                    break

                if cmd == ',':
                    current_action = 'accept'
                elif cmd == '.':
                    current_action = 'manage'
                    current_student = 'all'
                elif cmd == readchar.key.BACKSPACE:
                    current_student = None
                elif cmd == readchar.key.ENTER:
                    if len(assignments) == len(students):
                        current_action = 'proceed'
                    else:
                        if input(f'\n{Style.BRIGHT}{Fore.RED}Not all students have been assigned. Are you sure you want to proceed? (y/N) ').strip().lower() == 'y':
                            current_action = 'proceed'
                elif cmd == ";":
                    if not isinstance(last_managed_student, Student):
                        if len(students) > 0:
                            current_action = 'manage'
                            current_student = students[0]
                    else:
                        current_action = 'manage'
                        current_student = last_managed_student
                elif cmd == "'":
                    unassigned_students = [s for s in students if s.uni_id not in assignments]
                    if len(unassigned_students) > 0:
                        current_action = 'manage'
                        current_student = unassigned_students[0]
                    else:
                        print(f'\n{Style.BRIGHT}{Fore.RED}No unassigned students{uni_id}{Style.RESET_ALL}')
                        time.sleep(1)
                elif cmd.isalpha():
                    if uni_id == '':
                        current_student = cmd
                    else:
                        uni_id += cmd

                        for s in students:
                            if s.uni_id == uni_id:
                                current_action = 'manage'
                                current_student = s
                                break
                        else:
                            print(f'{cmd}\n{Style.BRIGHT}{Fore.RED}Invalid student ID: {uni_id}{Style.RESET_ALL}')
                            current_student = None
                            time.sleep(1)
            elif current_action == 'accept':
                print("Recruitment office - new candidates arrived this month:")
                print()
                if not candidates:
                    print("No candidates are available right now.")
                    input('Press [ENTER] to continue: ')
                    current_action = 'idle'
                else:
                    cost = recruit_cost(students, n_of_dead_students)
                    for i, cand in enumerate(candidates):
                        display_candidate(cand, i + 1, cost)
                        print(f"   Enroll cost: ${cost}")
                        print()
                    print(f"You have {len(students)}/{MAX_STUDENTS} students.")
                    if len(students) >= MAX_STUDENTS:
                        print(f'{Style.BRIGHT}{Fore.RED}The dormitory is full! Graduate a student to free up space.{Style.RESET_ALL}')
                    print("Press 1/2/3 to recruit that candidate (again, if you wish), or space to leave: ", end='')
                    key = readchar.readkey().upper()
                    if key in '123':
                        idx = int(key) - 1
                        if idx >= len(candidates):
                            print(f'\n{Style.BRIGHT}{Fore.RED}No such candidate.{Style.RESET_ALL}')
                            time.sleep(1)
                        elif len(students) >= MAX_STUDENTS:
                            print(f'\n{Style.BRIGHT}{Fore.RED}The dormitory is full!{Style.RESET_ALL}')
                            time.sleep(1)
                        elif money < cost:
                            print(f'\n{Style.BRIGHT}{Fore.RED}Not enough money!${Style.RESET_ALL}')
                            time.sleep(1)
                        else:
                            candidate = candidates.pop(idx)
                            accept_candidate(rand, candidate, students)
                            money -= cost
                            print(f'\n{Style.BRIGHT}{candidate.superhero_name}{Style.RESET_ALL} has been enrolled as [{candidate.uni_id}]!')
                            input('Press [ENTER] to continue: ')
                    elif key == ' ':
                        current_action = 'idle'
            elif current_action == 'manage':
                s = current_student
                last_managed_student = current_student
                if s == 'all':
                    print(f'You are now managing all students.')
                else:
                    print(f'You are now managing [{s.uni_id}] {Style.BRIGHT}{s.superhero_name}{Style.RESET_ALL}.')
                    print_student_stats(s)
                print(f' Remaining money: ${money}')

                course_letters = ['1', '2', '3', '4', '5', '6']
                course_costs = []
                print("Courses:")
                for i, stat in enumerate(COURSE_STATS):
                    if s == 'all':
                        name = f'{stat} course'
                        cost = sum([COURSE_BASE_COST + COURSE_COST_INCREASE * s1.courses_taken[stat] for s1 in students])
                    else:
                        name = get_course_name(course_names, stat, s.power)
                        cost = COURSE_BASE_COST + COURSE_COST_INCREASE * s.courses_taken[stat]
                    print(f"[{course_letters[i]}] {name} (+{stat}): ${cost}")
                    course_costs.append(cost)

                if s == 'all':
                    print('Press the corresponding key to buy a course for all students.')
                else:
                    print(f'Press the corresponding key to buy a course for {Style.BRIGHT}{s.superhero_name}{Style.RESET_ALL}.')
                    print(f'Press > to assign {Style.BRIGHT}{s.superhero_name}{Style.RESET_ALL} to a mission.')
                    print(f'Press G to graduate {Style.BRIGHT}{s.superhero_name}{Style.RESET_ALL}.')
                print('Press spacebar to cancel.\nYour command: ', end='')
                cmd = readchar.readkey().upper()
                if cmd in course_letters:
                    stat = COURSE_STATS[course_letters.index(cmd)]
                    cost = course_costs[course_letters.index(cmd)]

                    if money < cost:
                        print(f"{cmd}\n{Style.BRIGHT}{Fore.RED}Not enough money!{Style.RESET_ALL}")
                        time.sleep(1)
                    else:
                        if s == 'all':
                            for s1 in students:
                                take_course(s1, stat)
                        else:
                            take_course(s, stat)

                        money -= cost
                elif cmd == ' ':
                    current_action = 'idle'
                elif cmd == '>' and s != 'all':
                    current_action = 'assign'
                elif cmd == 'G' and s != 'all':
                    if input(f'\nGraduate {Style.BRIGHT}{s.superhero_name}{Style.RESET_ALL} [{s.uni_id}]? This removes the student. (y/N) ').strip().lower() == 'y':
                        students.remove(s)
                        if s.uni_id in assignments:
                            del assignments[s.uni_id]
                        current_action = 'idle'
                        current_student = None
                        n_of_dead_students += 1
                        print(f'{Style.BRIGHT}{s.superhero_name}{Style.RESET_ALL} has graduated!')
                        input('Press [ENTER] to continue: ')
            elif current_action == 'assign':
                s = current_student
                display_student(s)
                print(f'Assign {Style.BRIGHT}{s.superhero_name}{Style.RESET_ALL} to a mission.\n')
                print('Missions:')
                for j, m in enumerate(missions):
                    print(f'{j+1}. {m.city} ({Style.BRIGHT}{m.villain.name}{Style.RESET_ALL})', end='')
                    n_assigned = sum([1 for s_uni_id in assignments if assignments[s_uni_id] == m])
                    if n_assigned > 0:
                        print(f' ' + format_prediction(predictions[j], n_assigned), end='')
                    if s.power in m.villain.immunities:
                        print(f' {Fore.RED}WARNING! {m.villain.name} is immune to {s.power}{Style.RESET_ALL}', end='')
                    print()

                m_idx = get_int_input("Type the number of the mission (or 0 to cancel): ", 0, len(missions)) - 1
                if m_idx == -1:
                    current_action = 'manage'
                else:
                    m = missions[m_idx]
                    assignments[s.uni_id] = m
                    predictions[m_idx] = monte_carlo_predict(m, [s for s in students if assignments.get(s.uni_id) == m], rand)
                    current_action = 'idle'
            elif current_action == 'proceed':
                # everyone is assigned, resolving missions
                print('Resolving mission results...\n')

                total_prize = 0
                failed_missions = 0
                dead_students = []
                mission_results = []

                clear_screen()
                display_status_bar()
                print()
                for i, m in enumerate(missions):
                    heroes = [s for s in students if assignments.get(s.uni_id) == m]
                    success, dead = run_mission(m, heroes, rand, verbose=SHOW_BATTLE_PROGRESS)
                    dead_students.extend(dead)
                    if success:
                        total_prize += m.prize
                        mission_results.append(True)
                    else:
                        failed_missions += 1
                        mission_results.append(False)

                for i, m in enumerate(missions):
                    if mission_results[i]:
                        print(f"{i+1}. Mission in {m.city} SUCCESS! Prize: ${m.prize}")
                    else:
                        print(f"{i+1}. Mission in {m.city} FAILED!")

                money += total_prize

                for s in dead_students:
                    n_of_dead_students += 1
                    if s in students:
                        students.remove(s)
                    print(f"{Style.BRIGHT}{s.superhero_name}{Style.RESET_ALL} {Style.BRIGHT}{Style.DIM}{Fore.RED}is dead!{Style.RESET_ALL}")

                total_failed_missions += failed_missions
                print()
                input('Press [ENTER] to continue: ')
                break

            # recalculate predictions
            for i, m in enumerate(missions):
                predictions[i] = monte_carlo_predict(m, [s for s in students if assignments.get(s.uni_id) == m], rand)

        if total_failed_missions >= MAX_MISSION_FAILS:
            print(f"\nGame Over! You failed {MAX_MISSION_FAILS} missions.")
            break

        if not students and money < STUDENT_BASE_COST:
            print("\nGame Over! All students are dead and you have no money to accept new ones.")
            break

        if resigned:
            break

        month += 1
        missions = generate_missions(month, rand)
        candidates = [generate_candidate(rand) for _ in range(3)]
        course_names = generate_course_names(rand)
        assignments = {}
        predictions = [0.0 for _ in range(len(missions))]


if __name__ == "__main__":
    main()
