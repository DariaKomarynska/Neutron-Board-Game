from classFigure import Figure
from classBoard import Board


class Game:
    # def __init__(self):
    #     b = Board()

    def start_rules_game(self):
        b = Board()
        print("The Game of Neutron\nStart new game!")
        print()
        print(b)
        quit = True
        # Start game from rules or play now
        print(
            "If you want to read short rules, enter '1'\
            \nTo start game between 2 people, enter '2'\
            \nTo start light game with computer, enter '3'\
            \nTo start hard game with computer, enter '4'\
            \nTo start game between hard and light computers, enter '5'"
        )
        while quit:
            # Check: is input number correct?
            start = input("Your choice: ")
            print()
            if len(start) != 1:
                print("Enter 1, 2, 3, 4 or 5 without space.")
                quit = True
            else:
                quit = False

            if quit is False:
                # Check: is input element digit?
                if not start.isdigit():
                    print("Please, write correctly.")
                    quit = True
                elif start.isdigit():
                    n_start = int(start)
                    quit = False

            if quit is False:
                # Check: is input element 1-5?
                if n_start not in range(1, 6):
                    print("Please, choose 1, 2, 3, 4 or 5")
                    quit = True

            flag = True

        while quit is False:
            # 1 if player want to rules
            if n_start == 1 and flag is True:
                print(
                    "RULES\
                \nWinning the game is simple.\
                \nJust maneuver the neutron onto your own back row."
                )
                print()
                print(
                    "Every",
                    "piece, even the neutron, moves in excactly the",
                    "same way:\nalong a straight line horizontally,",
                    "vertically, or diagonally.\nA piece stops moving",
                    "just before it runs into another piece or the side",
                    "wall.\nThere is no jumping or capturing. But there",
                    "is one unusual feature.\nWhen a piece moves, it must",
                    " go as far as possible in the direction chosen.",
                )
                print()
                flag = False
            if n_start == 1 and flag is False:
                print()
                print(
                    "If you want to start game between two people, enter '2'",
                    "\nIf you want to start light game with computer,",
                    "enter '3'\
                    \nIf you want to start hard game with computer,",
                    "enter '4'",
                    "\nIf you want to start game between hard and light computers,",
                    "enter '5'",
                    "\nIf you don't want to play, enter '0'",
                )
                new_start = input("Your choice: ")

                # Check: is input element correct?
                if len(new_start) != 1:
                    print("Try again.")
                    quit = False
                    flag = False
                else:
                    quit = True

                if quit is True:

                    if not new_start.isdigit():
                        # Check: is input element digit?
                        print("Please, write correctly.")
                        quit = False
                        flag = False
                    elif new_start.isdigit():
                        new_start = int(new_start)
                        quit = True
                if quit is True:
                    if new_start == 0:
                        # 0 if player don't want to play
                        print("END")
                        break

                    elif new_start == 2 or new_start == 3 or new_start == 4 or new_start == 5:
                        # 2 if start the game between two people
                        # 3 if start the game between human and light computer
                        # 4 if start the game between human and hard computer
                        self.start_game(new_start)
                        break

                    else:
                        # if input number is not 2, 3, 4, 5 or 0
                        print("Enter only 2, 3, 4, 5 or 0.")
                        quit = False
                        flag = False

            elif n_start == 2 or n_start == 3 or n_start == 4 or n_start == 5:
                self.start_game(n_start)
                break

    def start_game5(self, version):
        b = Board()
        if version == 2 or version == 3:
            new = 23
            print("Player-1 - 🟡 | Player-2 - 🟣")
        if version == 4 or version == 5:
            new = 45
            print("Player-1 - 🟣 | Player-2 - 🟡")
        print()
        print(b)
        version = int(version)
        white = Figure.WHITE
        black = Figure.BLACK
        neutron = Figure.NEUTRON
        white_won = "Player-2 has fallen into a trap and cannot move Neutron\
                    \n🟣 Player-2 🟣 is Looser\
                    \n🟡 Player-1 🟡 is WINNER"
        black_won = "Player-1 has fallen into a trap and cannot move Neutron\
                    \n🟡 Player-1 🟡 is Looser\
                    \n🟣 Player-2 🟣 is WINNER"
        black_won_hard = "Player-2 has fallen into a trap and cannot move Neutron\
                    \n🟡 Player-2 🟡 is Looser\
                    \n🟣 Player-1 🟣 is WINNER"
        white_won_hard = "Player-1 has fallen into a trap and cannot move Neutron\
                    \n🟣 Player-1 🟣 is Looser\
                    \n🟡 Player-2 🟡 is WINNER"
        print("Write X and Y of pawn: two numbers from 1 to 5 with", "space")
        while True:
            print()
            if version == 2 or version == 3:
                print("Player-1 🟡, move a piece:")
                b.enter_coordinates(white)
            elif version == 4 or version == 5:
                print("Player-1 🟣, move a piece:")
                input("Computer's move - Press enter  ")
                b.hard_opponent_coordinates(black)
            print()
            print(b)
            print()
            if version == 2:
                print("Player-2 🟣, move Neutron 🐹: ")
                if b.enter_coordinates(neutron) is False:
                    print()
                    print(b)
                    print(white_won)
                    break
            elif version == 3:
                print("Player-2 🟣, move Neutron 🐹: ")
                input("Computer's move - Press enter  ")
                if b.random_opponent_coordinates(neutron) is False:
                    print()
                    print(b)
                    print(white_won)
                    break
            elif version == 4:
                print("Player-2 🟡, move Neutron 🐹: ")
                if b.enter_coordinates(neutron) is False:
                    print()
                    print(b)
                    print(black_won_hard)
                    break
            elif version == 5:
                print("Player-2 🟡, move Neutron 🐹: ")
                input("Computer's move - Press enter  ")
                if b.random_opponent_coordinates(neutron) is False:
                    print()
                    print(b)
                    print(black_won_hard)
                    break
            print()
            print(b)
            # After moving neutron
            if b.game_over(new) is True:
                break
            print()
            if version == 2:
                print("Player-2 🟣, move a piece: ")
                b.enter_coordinates(black)
            elif version == 3:
                print("Player-2 🟣, move a piece: ")
                input("Computer's move - press enter  ")
                b.random_opponent_coordinates(black)
            elif version == 4:
                print("Player-2 🟡, move a piece: ")
                b.enter_coordinates(white)
            elif version == 5:
                print("Player-2 🟡, move a piece: ")
                input("Computer's move - press enter  ")
                b.random_opponent_coordinates(white)
            print()
            print(b)
            print()
            if version == 2 or version == 3:
                print("Player-1 🟡, move Neutron 🐹: ")
                if b.enter_coordinates(neutron) is False:
                    print()
                    print(b)
                    print(black_won)
                    break
            elif version == 4 or version == 5:
                print("Player-1 🟣, move Neutron 🐹: ")
                input("Computer's move - Press enter  ")
                if b.hard_opponent_coordinates(neutron) is False:
                    print()
                    print(b)
                    print(white_won_hard)
                    break
            print()
            print(b)
            # After moving neutron
            if b.game_over(new) is True:
                break
        print()

    def start_game(self, version):
        b = Board()
        if version == 2 or version == 3:
            new = 23
            print("Player-1 - 🟡 | Player-2 - 🟣")
        if version == 4 or version == 5:
            new = 45
            print("Player-1 - 🟣 | Player-2 - 🟡")
        print()
        print(b)
        version = int(version)
        white = Figure.WHITE
        black = Figure.BLACK
        neutron = Figure.NEUTRON
        white_won = "Player-2 has fallen into a trap and cannot move Neutron\
                    \n🟣 Player-2 🟣 is Looser\
                    \n🟡 Player-1 🟡 is WINNER"
        black_won = "Player-1 has fallen into a trap and cannot move Neutron\
                    \n🟡 Player-1 🟡 is Looser\
                    \n🟣 Player-2 🟣 is WINNER"
        black_won_hard = "Player-2 has fallen into a trap and cannot move Neutron\
                    \n🟡 Player-2 🟡 is Looser\
                    \n🟣 Player-1 🟣 is WINNER"
        white_won_hard = "Player-1 has fallen into a trap and cannot move Neutron\
                    \n🟣 Player-1 🟣 is Looser\
                    \n🟡 Player-2 🟡 is WINNER"
        print("Write X and Y of pawn: two numbers from 1 to 5 with", "space")
        while True:
            print()
            if version == 5:
                print("Player-1 🟣, move a piece:")
                input("Computer's move - Press enter  ")
                b.hard_opponent_coordinates(black)
            print()
            print(b)
            print()
            # After moving neutron
            if b.game_over(new) is True:
                break
        print()