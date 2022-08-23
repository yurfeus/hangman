
def ugadai_slovo():

    letters_list = ("a", "b", 'c', 'd',
                    'e', 'f', 'g', 'h',
                    'i', 'j', 'k', 'l',
                    'm', 'n', 'o', 'p',
                    'q', 'r', 's', 't',
                    'u', 'v', 'w', 'x', 'y', 'z')

    #proverka, vse li bukvy v zagadannom slove
    #cond = True
    while True:
        guess_word = input("Vvedite slovo, kotoroe nado otgadat': ")
        for letter in guess_word:
            if letter.lower() in letters_list:
                cond = False
            else:
                print("Please, enter only letters!")
                cond = True
                break
        if cond == False:
            break

    wrong = 0
    stages = ['',
              "      ______/\_    _",
              "     /      \  \__/__\  ",
              "    |        |    \__ ",
              "   (  T N T   )      \ ",
              "    |        |        \__\|/_ ",
              "_____\______/____________/|\  ",
              "",
             ]

    game_over_msg = """ 
        *************
        ****BOOM!****
        ***BOOOM!!***
        **BOOOOM!!!**
        *************
        """
    r_letters = list(guess_word)
    board = ["_"] * len(guess_word)
    win = False
    print("Let's start the game!")
    print(f"ugadaite slovo iz {len(board)} bukv: ")
    print(" "*(18-len(board)), "".join(board))


    while wrong < len(stages) -1:
        #proverka vvoda 1 bukvy
        while True:
            print("\n")
            msg = "Vvedite bukvu: "
            char = input(msg)
            if len(set(char)) == 1:
                char = str(set(char))[2]
                break
            print("Pozhaluista, vnimatelnee!!!"
                  f"\nVy vveli '{char}'"
                  "\nKakuju imenno bukvu vvodit?")

        if char in r_letters:
            cind = r_letters.index(char)
            board[cind] = char
            r_letters[cind] = '$'
        else:
            wrong +=1
        print(("".join(board)))
        print("\n".join(stages[0:wrong+1]))

        if "_" not in board:
            print("\nYOU WIN! The word was: ",
                  "\n","".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong]),
              "\nYou Loose! The word was: '{}'.".format(guess_word),
              game_over_msg)

ugadai_slovo()






#for i in stages:
#    print(i)
#print (game_over_msg)