#!/usr/bin/env python3

import sys
import os
import random
import time
import subprocess
import platform


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def check_internet():
    try:
        param = '-n' if platform.system().lower() == 'windows' else '-c'
        subprocess.check_call(['ping', param, '1', 'www.google.com'], 
                            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
    except subprocess.CalledProcessError:
        return False


COLORS = {
    'Bl': '\033[30m',
    'Re': '\033[1;31m',
    'Gr': '\033[1;32m',
    'Ye': '\033[1;33m',
    'Blu': '\033[1;34m',
    'Mage': '\033[1;35m',
    'Cy': '\033[1;36m',
    'Wh': '\033[1;37m',
    'reset': '\033[0m'
}


def c(text, color):
    return f"{COLORS.get(color, '')}{text}{COLORS['reset']}"


def loading_animation(message, duration=0.2, cycles=10):
    faces = ['🙂', '😎', '🙂']
    for i in range(cycles):
        sys.stdout.write(f'\r{c(message, "Wh")} {c(faces[i % len(faces)], "Gr")}')
        time.sleep(duration)
    clear_screen()


def banner():
    banner_text = """\
    __________                     .__                    __      __                .___
    \\______   \\__ _________________|  |   ____           /  \\    /  \\___________  __| _/
    |     ___/  |  \\___   /\\___   /  | _/ __ \\   ______ \\   \\/\\/   /  _ \\_  __ \\/ __ | 
    |    |   |  |  //    /  /    /|  |_\\  ___/  /_____/  \\        (  <_> )  | \\/ /_/ | 
    |____|   |____//_____ \\/_____ \\____/\\___  >           \\__/\\  / \\____/|__|  \\____ | 
                        \\/      \\/         \\/                 \\/                   \\/ 
    <<  WORD  PUZZLE  GAME   <<============================>>    AUTHOR  BY  HUNBYTS >>

                  -----------------------------------------------
                    |             .:: MENU GAME ::.             |
                    |                                           |
                    |   [1] NOOB                                |
                    |   [2] MEDIUM                              |
                    |   [3] HIGH                 [COMING SOON] |
                    |   [4] LEGEND               [COMING SOON] |
                    |   [5] GLORY                [COMING SOON] |
                    |                                           |
                   -----------------------------------------------\
"""
    for line in banner_text.split('\n'):
        print(c(line, 'Ye'))


def get_questions(level):
    soal_noob = [
        {"soal": "A - C - R", "jawaban": "CAR"},
        {"soal": "D - L - R - O - W", "jawaban": "WORLD"},
        {"soal": "O - L - E - V", "jawaban": "LOVE"},
        {"soal": "X - I - U - N - L", "jawaban": "LINUX"},
        {"soal": "M - H - T - L", "jawaban": "HTML"},
        {"soal": "C - S - S", "jawaban": "CSS"},
        {"soal": "D - R - E", "jawaban": "RED"},
        {"soal": "S - B - H - A", "jawaban": "BASH"},
        {"soal": "Y - B - E - T", "jawaban": "BYTE"},
        {"soal": "E - L - B - U", "jawaban": "BLUE"},
        {"soal": "L - I - S - T", "jawaban": "LIST"},
        {"soal": "T - C - A", "jawaban": "CAT"},
        {"soal": "T - U - E - R", "jawaban": "TRUE"},
        {"soal": "L - F - E - S - A", "jawaban": "FALSE"},
        {"soal": "O - O - M - N", "jawaban": "MOON"},
        {"soal": "T - S - R - A - H", "jawaban": "TRASH"},
        {"soal": "G - O - O - D", "jawaban": "GOOD"},
        {"soal": "Y - D - A", "jawaban": "DAY"},
        {"soal": "E - L - P - A - P", "jawaban": "APPLE"},
        {"soal": "T - M - I - S - E", "jawaban": "TIMES"}
    ]

    soal_medium = [
        {"soal": "T - N - O - U - M - N - I", "jawaban": "MOUNTAIN"},
        {"soal": "N - D - C - A - E - B - R - A - L - A", "jawaban": "CANDELABRA"},
        {"soal": "S - T - U - R - A - U", "jawaban": "TAURUS"},
        {"soal": "W - O - L - O - L - F", "jawaban": "FOLLOW"},
        {"soal": "T - Q - B - U - O - E - U", "jawaban": "BOUQUET"},
        {"soal": "F - A - C - T - I - R - F - R", "jawaban": "AIRCRAFT"},
        {"soal": "E - A - K - L", "jawaban": "LAKE"},
        {"soal": "E - M - A - I - N", "jawaban": "ANIME"},
        {"soal": "M - G - I - I - N - E", "jawaban": "GEMINI"},
        {"soal": "Z - N - E - R - E - B - U - L - I", "jawaban": "NEBULIZER"},
        {"soal": "D - L - N - O - I - M - A - N", "jawaban": "MANDOLIN"},
        {"soal": "O - M - O - N - K - I", "jawaban": "KIMONO"},
        {"soal": "H - T - E - L - P - E - N - A", "jawaban": "ELEPHANT"},
        {"soal": "R - I - D - A - O - N - D", "jawaban": "ANDROID"},
        {"soal": "S - D - O - W - I - N - W", "jawaban": "WINDOWS"},
        {"soal": "K - W - T - E - N - O - R", "jawaban": "NETWORK"},
        {"soal": "G - A - L - A - U - E - N - G", "jawaban": "LANGUAGE"},
        {"soal": "G - P - A - R - A - O - N", "jawaban": "PARAGON"},
        {"soal": "T - P - U - R - O - M - C - E", "jawaban": "COMPUTER"},
        {"soal": "N - O - M - H - P - M - N - E - E - O - N", "jawaban": "PHENOMENON"}
    ]

    return soal_noob if level == '1' else soal_medium


def play_game(name, level):
    questions = get_questions(level)
    random.shuffle(questions)
    
    level_name = "NOOB" if level == '1' else "MEDIUM"
    score = 0
    
    loading_animation("LOADING YOUR LEVEL")
    
    for i, q in enumerate(questions):
        print(f"""
    {c('LEVEL', 'Wh')} {c(str(i+1), 'Ye')} {c('|', 'Wh')} {c(level_name, 'Gr')}
        
        {c('QUESTION:', 'Ye')}             
        {c(q['soal'], 'Gr')}           
            
    """)
        answer = input(f"{c('[+]', 'Wh')} {c(name, 'Ye')} {c('-', 'Wh')} {c('Answer', 'Gr')} {c(':', 'Ye')} ")
        
        if answer.upper() == q['jawaban']:
            print(c("Good Job!", "Wh"))
            time.sleep(1)
            clear_screen()
            score += 5
        else:
            print(c("Defeat!", "Re"))
            time.sleep(1)
            clear_screen()
    
    print(f"{c(name, 'Ye')}{c(', Your score: ', 'Wh')}{c(f'{score}/{len(questions)}', 'Gr')}\n")
    
    while True:
        play_again = input(f"{c('[+]', 'Wh')} {c('NEXT GAME', 'Gr')} {c('Y/N', 'Ye')} {c(':', 'Wh')} ").lower()
        if play_again == 'y':
            banner()
            main(name)
            return
        elif play_again == 'n':
            print(f"\n{c('[+]', 'Wh')} {c('CLOSE GAME...', 'Ye')}")
            time.sleep(1)
            sys.exit()
        else:
            print(c("Option not found!", "Re"))


def login():
    clear_screen()
    print(c(f"\n[+] LOGIN YOUR GAME", "Gr"))
    name = input(c(f"\nInput Full Name :", "Gr"))
    
    while True:
        try:
            age = int(input(c(f"Age            :", "Gr")))
            if age >= 100:
                print(c("You're too old!", "Re"))
                sys.exit()
            break
        except ValueError:
            print(c("Please enter a valid number!", "Re"))
    
    clear_screen()
    return name


def main(name=None):
    if name is None:
        name = login()
    
    loading_animation("LOADING YOUR GAME")
    banner()
    
    while True:
        user_choice = input(c(f"\n   [+] Choose option game :", "Gr"))
        
        if user_choice in ['1', '2']:
            play_game(name, user_choice)
        elif user_choice in ['3', '4', '5']:
            print(c("Coming soon!", "Ye"))
        else:
            print(c("Invalid option!", "Re"))


if __name__ == "__main__":
    if not check_internet():
        print(c("No internet connection! Please check your network.", "Re"))
        sys.exit()
    
    print(c("Internet connection OK!", "Gr"))
    clear_screen()
    main()
