def hard_opponent_coordinates(self, figure):
        """
        Computer chooses best coordinates for "From X Y" and "To X Y".
        """
        possible = [1, 2, 3, 4, 5]
        correct_xy = True
        flag = True
        quit = True
        counter_from = 0
        while correct_xy and flag:
            from_xy = choices(possible, k=2)
            if self.check_choosen_figure_on_the_board(figure, from_xy[0], from_xy[1]):
                if figure == Figure.NEUTRON:
                    if len(self.get_pawn_moves(from_xy[0], from_xy[1])) == 0:
                        # If neutron cannot move - game over
                        correct_xy = False
                        flag = True
                        quit = False
                        break
                    else:
                        flag = False
                    if flag is False:
                        for j in range(1, 6):
                            # If neutron can choose position on black row,
                            # choose it
                            vic = [j, 1]    # Victory position
                            if self.get_pawn_moves(from_xy[0], from_xy[1]).count(vic) == 1:
                                to_xy = vic
                                correct_xy = True
                                flag = False
                                break
                        else:
                            correct_xy = False
                            flag = True
                            quit = True
                            break
                else:
                    counter_from += 1
                    correct_xy = False
                    flag = True
                    quit = True
                    break
                    # if len(self.get_pawn_moves(from_xy[0], from_xy[1])) == 0:
                    #     correct_xy = True
                    #     flag = True
                    #     continue
                    # elif len(self.get_pawn_moves(from_xy[0], from_xy[1])) == 1:
                    #     flag = False
                    #     correct_xy = True
                    #     to_xy = self.get_pawn_moves(from_xy[0], from_xy[1])[0]
                    #     break
                    # else:
                    #     correct_xy = False
                    #     quit = True
                    #     flag = False
                    #     break
                    # flag = False

                    # if flag is False:
                    #     # for k in range(100):
                    #     if
                    #         # if black pawn can stand on the white row - move there
                    #         # to prevent empty places on white row (opponent)
                    #         if self.get_pawn_moves(from_xy[0], from_xy[1]).count(white_row) == 1:
                    #             to_xy = white_row
                    #             correct_xy = True
                    #             flag = False
                    #             break
                    #         elif (
                    #             self.get_pawn_moves(from_xy[0], from_xy[1]).count(white_row) != 1
                    #             and k != 99
                    #         ):
                    #             correct_xy = True
                    #             flag = True
                    #             continue
                    #         else:
                    #             correct_xy = False
                    #             flag = True
                    #             break
        counter_to = 0
        while correct_xy is False and quit is True:
            # If figure is Black Pawn

            to_xy = choices(possible, k=2)

            if self.get_pawn_moves(from_xy[0], from_xy[1]).count(to_xy) == 1:
                flag = False
                correct_xy = True
                counter_to += 1
                if figure == Figure.NEUTRON:
                    # Check looser position
                    # If Neutron has variants: choose looser position
                    # or another one, It should choose last one
                    if to_xy[1] == 5:
                        correct_xy = False
                        quit = True
                        continue
                    else:
                        break
                elif figure == Figure.BLACK:
                    if to_xy[1] == 5:
                        break
                    elif to_xy[1] != 5 and counter_to < 100:
                        correct_xy = False
                        quit = True
                        continue
                    elif to_xy[1] != 5 and counter_to == 100 and counter_from < 20:
                        correct_xy = True
                        flag = True
                        break
                    elif to_xy[1] != 5 and counter_to == 100 and counter_from == 20:
                        flag = False
                        correct_xy = True
                        break

        if flag is False and correct_xy is True and quit is True:
            print(from_xy)
            print(to_xy)
            print(self.get_pawn_moves(from_xy[0], from_xy[1]))
            self.move_pawns(from_xy, to_xy)
        if correct_xy is False and quit is False and flag is True:
            return False

def hard_opponent_coordinates_toXY_neutron(self, figure, fromXY, possible_moves):
        quit = True
        # possible = possible_moves
        new_possible = possible_moves.copy()
        possible = possible_moves.copy()
        while quit:
            for j in range(1, 6):
                vic = [j, 1]    # victory position
                if possible.count(vic) == 1:
                    toXY = vic
                    quit = False
                    break
            else:
                break
        # if quit is False:
        while quit:
            if len(new_possible) != 0:
                toXY = self.random_toXY(figure, fromXY, 1, new_possible)
                used = toXY
                if toXY[1] != 5 and len(new_possible) != 1:
                    new_possible.remove(used)
                    continue
                elif (toXY[1] == 5) and (len(possible) != 1):
                    new_possible.remove(used)
                    possible.remove(used)
                    correct_xy = False
                    quit = True
                    continue
                else:
                    break
            else:
                toXY = self.random_toXY(figure, fromXY, 1, possible)
                break