import time
import random
import os

hangman_words = [
    "soap", "farm", "pull", "worm", "walk", "pipe", "force", "experience", "red", "war",
    "different", "time", "ribbon", "army", "bulb", "degree", "hill", "shop", "limit", "frame",
    "storm", "flag", "guide", "wood", "grey", "answer", "skin", "snake", "tin", "sugar",
    "boat", "jump", "regret", "chance", "winter", "deep", "sister", "garden", "smile", "basin",
    "note", "soldier", "look", "writing", "together", "condition", "silk", "middle", "colour",
    "when", "grass", "sick", "risk", "key", "old", "need", "knee", "brother", "joy", "drive",
    "month", "nation", "spoon", "fruit", "wheel", "ice", "kind", "picture", "love", "bank",
    "uncle", "verse", "cup", "lamp", "hammer", "arm", "burst", "moon", "father", "white",
    "sheet", "bag", "table", "building", "bowl", "muscle", "theatre", "knife", "dog", "thunder",
    "cold", "ant", "glass", "hair"
]

hangman_art = ['''
                   
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

table_words = hangman_words
the_man_hanged_drawed = hangman_art

class App:
    def calculator():
        os.system("clear")
        print("""

            CALCULATOR
            Enter a calculation
            and get it answered.

        """)
        running = True
        try:
            while running:
                calculation = input(">>> ")
                if calculation == "quit" or calculation == "exit":
                    break
                
                print(eval(calculation))
        except:
            time_rea = 5

            
            while True:
                os.system("clear")
                print("We are sorry about the unexpected message!")
                print(f"""

                    But the last command you wrote in the calculator
                    caused the app to crash.

                    Now the app will exit safely in {time_rea}

                """)

                time_rea -= 1
                time.sleep(1)

                if time_rea == -1:
                    break
                    
    def password_generator():
        os.system("clear")
        def create_password(lenght):

            # dont worry bout that
        
            alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
            end_password = ""
            
            for i in range(lenght):
                choose = random.randint(0, 1)
                if choose == 0:
                    end_password += f"{random.randint(0, 100)}"
                elif choose == 1:
                    choose_letter = random.randint(0, 52)
                    end_password += f"{alphabet[choose_letter]}"

            return end_password
        
        print("""
              
              HOW LONG DO YOU WANT YOUR PASSWORD TO BE?
              MAX CHARACTERS: 56
              ANYMORE WILL CAUSE YOUR COMPUTER TO CRASH.
              
              """)
        lengh = int(input("> "))

        try:

            print(create_password(lengh))
            time.sleep(3)

        except:
            print("YOU CAUSED THE APPLICATION TO CRASH")
            while True:
                os.system("clear")
                print("We are sorry about the unexpected message!")
                print(f"""

                    But the last command you wrote.
                    caused the app to crash.

                    Now the app will exit safely in {time_rea}

                """)

                time_rea -= 1
                time.sleep(1)

                if time_rea == -1:
                    break

    def countdown():
        os.system("clear")
        time_to_countdown = 0

        print("""

            WELCOME TO COUNTDOWN
            INSERT TIME AND THE APP
            WILL COUNTDOWN
              
            CANNOT USE OTHER APPS
            WHILE COUNTDOWN
              
            PLEASE ONLY TYPE IN SECONDS

        """)

        try:
            time_to_countdown = int(input("> "))

            while True:
                os.system("clear")
                print(f"""

                    TIME REMAINING:
                    {time_to_countdown}
                  
                    """)
                
                time.sleep(1)
            
                time_to_countdown -= 1
            
                if time_to_countdown == -1:
                    print("COUNTDOWN ENDED")
                    time.sleep(1)
                    break

        except:
            print("PLEASE ONLY INPUT A NUMBER!")
            time.sleep(3)

    def dollars_to_pesos():
        os.system("clear")
        print("""

        WELCOME TO MONEY CONVERTOR:
        DOLLARS TO PESOS EDITION
              
        INPUT DOLLAR VALUE AND
        RECEIVE THE EQUIVALENT IN
        PESOS
              
        
        CONVERTION WILL BE RETURNED IN      
        PESOS: ${amount}
              
        PLEASE INPUT DOLLAR VALUE IN
              
        > {amount}$

        """)

        while True:
            try:
                dollar_input = input("> ")

                if dollar_input:
                    if dollar_input == "EXIT":
                        print("THANKS FOR USING")
                        time.sleep(1)

                        break

                    dollar_input_out_dollar = dollar_input.replace("$", "")

                    dollar_int = int(dollar_input_out_dollar)

                    dollar_value = 18.20

                    returned_pesos = dollar_int * dollar_value

                    print(f"{dollar_input} ARE WORTH ${returned_pesos}")

            except:
                print("ONLY INPUT NUMBERS, NOT LETTERS.")
            
    def hangman():
        wins = 0
        loses = 0
        print("""

            WELCOME TO HANGMAN.SH
            PLEASE INPUT 'START'
            TO CREATE A NEW GAME.
                  
            INPUT 'EXIT' TO LEAVE
                  
            INPUT 'STATS' TO SEE
            YOUR SESION STATS.

            """)
        while True:

            start_game = input(">>> ")

            if start_game == "START":
                fails = 0
                word = table_words[random.randint(0, len(table_words))]
                word_list = [*word]


                player_correct_guesses = ["_" for word in word_list]

                while True:
                    os.system("clear")
                    print(f"""

                        {the_man_hanged_drawed[fails]}

                        {player_correct_guesses}

                    """)

                    if player_correct_guesses == word_list:
                        print("YOU WIN!")
                        time.sleep(1)
                        wins += 1
                        break

                    if fails == 6:
                        print("YOU LOST!")
                        print(f"THE WORD WAS {word}")
                        time.sleep(1)
                        loses += 1
                        break

                    print("Guess a letter:")
                    letter_guess = input("> ")

                    if letter_guess in word_list:
                        for i, letter in enumerate(word_list):
                            if letter == letter_guess:
                                player_correct_guesses[i] = letter_guess

                    else:
                        fails += 1


            elif start_game == "EXIT":
                break

            elif start_game == "STATS":
                print(f"""

                    WINS: {wins}
                    LOSES: {loses}

                """)

            elif start_game == "WORDS":
                print(hangman_words)

            else:
                print("Enter valid command.")
    
    def rock_paper_scissors():
        wins = 0
        loses = 0
        ties = 0
        availible_moves = ["ROCK", "PAPER", "SCISSORS"]

        def choose_move_ai(moves):
            move = random.randint(0, 2)

            ai_move = moves[move]

            return ai_move
        
        while True:
            print("""

            WELCOME TO
            ROCK PAPER SCISSORS
            
            INPUT 'START' FOR A 
            NEW GAME.
              
            INPUT 'HELP' FOR INSTRUCTIONS
              
            INPUT 'STATS' FOR ALL OF YOUR
            SESSION STATS
            
            INPUT 'EXIT' FOR LEAVING THE
            GAME.

            """)
            
            player_choose_input = input("> ")

            if player_choose_input == "START":
                os.system("clear")

                print("""

                    PLEASE ENTER A MOVE
                    ROCK, PAPER, SCISSORS.

                """)

                move_player = input("> ")

                print("PROCESSING AI MOVE...")

                time.sleep(3)

                ai_move = choose_move_ai(availible_moves)

                if move_player == "ROCK":
                    if ai_move == "PAPER":
                        print("YOU LOST!")
                        print(f"THE AI CHOSE {ai_move}")
                        time.sleep(3)
                        loses += 1
                        os.system("clear")
                        
                    elif ai_move == "SCISSORS":
                        print("YOU WIN!")
                        print(f"THE AI CHOSE {ai_move}")
                        time.sleep(3)
                        wins += 1
                        os.system("clear")
                        
                    elif ai_move == move_player:
                        print("ITS A TIE!")
                        print(f"THE AI CHOSE {ai_move}")
                        time.sleep(3)
                        ties += 1
                        os.system("clear")
                        
                
                elif move_player == "PAPER":
                    if ai_move == "SCISSORS":
                        print("YOU LOST!")
                        print(f"THE AI CHOSE {ai_move}")
                        time.sleep(3)
                        loses += 1
                        os.system("clear")
                        
                    elif ai_move == "ROCK":
                        print("YOU WIN!")
                        print(f"THE AI CHOSE {ai_move}")
                        time.sleep(3)
                        wins += 1
                        os.system("clear")
                        
                    elif ai_move == "PAPER":
                        print("ITS A TIE!")
                        print(f"THE AI CHOSE {ai_move}")
                        time.sleep(3)
                        ties += 1
                        os.system("clear")
                        

                elif move_player == "SCISSORS":
                    if ai_move == "ROCK":
                        print("YOU LOST!")
                        print(f"THE AI CHOSE {ai_move}")
                        time.sleep(3)
                        loses += 1
                        os.system("clear")
                        
                    elif ai_move == "PAPER":
                        print("YOU WIN")
                        print(f"THE AI CHOSE {ai_move}")
                        time.sleep(3)
                        wins += 1
                        os.system("clear")
                        
                    elif ai_move == "SCISSORS":
                        print("ITS A TIE!")
                        print(f"THE AI CHOSE {ai_move}")
                        time.sleep(3)
                        ties += 1
                        os.system("clear")
                    
                else:
                    print("NOT A VALID MOVE!")
                    time.sleep(3)
                    os.system("clear")
                        

            elif player_choose_input == "HELP":
                print("""

                YOU WILL FIRST BE ASKED TO INPUT
                MOVES BETWEEN ROCK, PAPER, SCISSORS.
                      
                AFTER YOU INPUT, THE COMPUTER WILL
                CHOOSE A RANDOM MOVEMENT.
                      
                IF YOU CHOOSE ROCK:
                      AND AI CHOOSE PAPER, YOU LOSE
                      AND AI CHOOSE SCISSORS, YOU WIN
                      AND AI CHOOSE ROCK, TIE

                IF YOU CHOOSE PAPER:
                      AND AI CHOOSE ROCK, YOU WIN
                      AND AI CHOOSE SCISSORS, YOU LOSE
                      AND AI CHOOSE PAPER, TIE

                IF YOU CHOOSE SCISSORS:
                      AND AI CHOOSE PAPER, YOU WIN
                      AND AI CHOOSE ROCK, YOU LOSE
                      AND AI CHOOSE SCISSORS, TIE

                """)

            elif player_choose_input == "EXIT":
                break

            elif player_choose_input == "STATS":
                print(f"""

                    WINS: {wins}
                    LOSTS: {loses}
                    TIES: {ties}

                    """)

            else:
                print(f"""

                    INVALID COMMAND:
                    {player_choose_input}

                    """)