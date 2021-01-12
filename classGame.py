from classFigure import Figure
from classBoard import Board


class Game:
    # def __init__(self):
    #     b = Board()

    def game_two_people_light_2_3(self, version, white, black, neutron, black_won, white_won):
        counter = 23
        b = Board()
        print("Player-1 - 🟡 | Player-2 - 🟣")
        print(b)
        while True:
            print()
            print("Player-1 🟡, move a piece:")
            b.enter_coordinates(white)
            self.print_b(b)
            print()
            print("Player-2 🟣, move Neutron 🐹: ")
            if version == 2:
                if b.enter_coordinates(neutron) is False:
                    self.print_b(b)
                    print(white_won)
                    break
            else:
                input("Computer's move - Press enter  ")
                if b.random_opponent_coordinates(neutron) is False:
                    self.print_b(b)
                    print(white_won)
                    break
            self.print_b(b)
            print()
            # After moving neutron
            if b.game_over(counter) is True:
                break
            print("Player-2 🟣, move a piece: ")
            if version == 2:
                b.enter_coordinates(black)
            else:
                input("Computer's move - press enter  ")
                b.random_opponent_coordinates(black)
            self.print_b(b)
            print()
            print("Player-1 🟡, move Neutron 🐹: ")
            if b.enter_coordinates(neutron) is False:
                self.print_b(b)
                print(black_won)
                break
            self.print_b(b)
            # After moving neutron
            if b.game_over(counter) is True:
                break
        print()

    def game_with_hard_computer_4_5(self, version, white, black, neutron, black_won, white_won):
        counter = 45
        b = Board()
        print("Player-1 - 🟣 | Player-2 - 🟡")
        self.print_b(b)
        while True:
            print()
            print("Player-1 🟣, move a piece:")
            input("Computer's move - Press enter  ")
            b.hard_opponent_coordinates(black)
            self.print_b(b)
            print()
            print("Player-2 🟡, move Neutron 🐹: ")
            if version == 4:
                if b.enter_coordinates(neutron) is False:
                    self.print_b(b)
                    print(black_won_hard)
                    break
            else:
                input("Computer's move - Press enter  ")
                if b.random_opponent_coordinates(neutron) is False:
                    self.print_b(b)
                    print(black_won_hard)
                    break
            self.print_b(b)
            # After moving neutron
            if b.game_over(counter) is True:
                break
            print("Player-2 🟡, move a piece: ")
            if version == 4:
                b.enter_coordinates(white)
            else:
                input("Computer's move - press enter  ")
                b.random_opponent_coordinates(white)
            self.print_b(b)
            print()
            print("Player-1 🟣, move Neutron 🐹: ")
            input("Computer's move - Press enter  ")
            if b.hard_opponent_coordinates(neutron) is False:
                self.print_b(b)
                print(white_won_hard)
                break
            self.print_b(b)
            # After moving neutron
            if b.game_over(counter) is True:
                break

    def print_b(self, b):
        print()
        print(b)

    def play_all_versions(self, version):
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
        b = Board()
        white = Figure.WHITE
        black = Figure.BLACK
        neutron = Figure.NEUTRON
        print()
        print("Write X and Y of pawn: two numbers from 1 to 5 with", "space")
        print()
        if version == 2 or version == 3:
            self.game_two_people_light_2_3(version, white, black, neutron, black_won, white_won)
        else:
            self.game_with_hard_computer_4_5(version, white, black, neutron, black_won_hard, white_won_hard)

    def start_choice_print(self, board, place):
        # Start game from rules or play now
        if place == 1:
            print("The Game of Neutron\nStart new game!")
            self.print_b(board)
        print()
        if place == 1:
            print("If you want to read short rules, enter '1'")
        print(
            "To start game between 2 people, enter '2'\
            \nTo start light game with computer, enter '3'\
            \nTo start hard game with computer, enter '4'\
            \nTo start game between hard and light computers, enter '5'"
        )
        if place == 0:
            print("If you don't want to play, enter '0'")

    def rules_print(self):
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

    def choose_correctly(self, place):
        quit = True
        while quit:
            # Check: is input number correct?
            start = input("Your choice: ")
            print()
            if (
                len(start) == 1
                and start.isdigit()
            ):
                # Check number of input elements
                # Check: is input element digit?
                start = int(start)
                if ((start not in range(1, 6) and place == 1)
                    or ((start not in range(2, 6) and start != 0) and place == 0)):
                    print("Try again")

                else:
                    quit = False
                    break
            else:
                print("Try again")
        return start

    def start_rules_game(self):
        b = Board()
        self.start_choice_print(b, 1)
        start = self.choose_correctly(1)
        if start == 1:
            self.rules_print()
            self.start_choice_print(b, 0)
            start = self.choose_correctly(0)
        if start == 2 or start == 3 or start == 4 or start == 5:
            # 2 if start the game between two people
            # 3 if start the game between human and light computer
            # 4 if start the game between human and hard computer
            # 5 if start the game between hard and light computers
            self.play_all_versions(start)
        elif start == 0:
            print("END")






