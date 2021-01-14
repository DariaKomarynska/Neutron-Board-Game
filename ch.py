    def hard_opponent_coordinates(self, figure):
        """
        Computer chooses best coordinates for "From X Y" and "To X Y".
        """
        correct_xy = True
        flag = True
        quit = True
        counter_from = 0
        while correct_xy and flag:
            from_xy = choices(possible, k=2)
            if self.check_choosen_figure_on_the_board(figure, from_xy[0], from_xy[1]):
                            flag = True
                            quit = True
                            break
                elif figure == Figure.BLACK:
                    if len(self.get_pawn_moves(from_xy[0], from_xy[1])) == 0:
                        correct_xy = True
                        flag = True
                        continue
                    elif len(self.get_pawn_moves(from_xy[0], from_xy[1])) == 1:
                        flag = False
                        correct_xy = True
                        to_xy = self.get_pawn_moves(from_xy[0], from_xy[1])[0]
                        break
                    else:
                        correct_xy = False
                        quit = True
                        flag = False
                        break

                    if flag is False:
                        for k in range(100):
                            for i in range(1, 6):
                                white_row = [i, 5]
                                # if black pawn can stand on the white row - move there
                                # to prevent empty places on white row (opponent)
                                if self.get_pawn_moves(from_xy[0], from_xy[1]).count(white_row) == 1:
                                    to_xy = white_row
                                    correct_xy = True
                                    flag = False
                                    break
                                elif (
                                    self.get_pawn_moves(from_xy[0], from_xy[1]).count(white_row) != 1
                                    and k != 99
                                ):
                                    correct_xy = True
                                    flag = True
                                    continue
                                else:
                                    correct_xy = False
                                    flag = True
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
                        continue
                    else:
                        break
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


        # toXY = self.random_toXY(figure, fromXY, 1, possible)
        # return toXY


        #     if toXY[1] == 5 and len(possible) != 1:
        #         used = toXY
        #         possible.remove(used)
        #         new.remove(used)
        #         continue
        #     elif :
        #         continue

        #     else:
        #         quit = False
        #         break
        # return toXY

        # # if quit is False:
        # while quit:
        #     if len(new_possible) != 0:
        #         toXY = self.random_toXY(figure, fromXY, 1, new_possible)
        #         used = toXY
        #         if toXY[1] != 5 and len(new_possible) != 1:
        #             new_possible.remove(used)
        #             continue
        #         elif (toXY[1] == 5) and (len(possible) != 1):
        #             new_possible.remove(used)
        #             possible.remove(used)
        #             correct_xy = False
        #             quit = True
        #             continue
        #         else:
        #             break
        #     else:
        #         toXY = self.random_toXY(figure, fromXY, 1, possible)
        #         break
        #     # if toXY[1] != 5:
        #     #     toXY = self.random_toXY(figure, fromXY, 1, possible_moves)

        # return toXY


            # else:
            #     temp_to_XY_moves = self.check_neutron_try_without_white_moves(figure, from_XY, possible_moves)

            #     if len(temp_to_XY_moves) == 1:
            #         to_XY = temp_to_XY_moves[0]
            #         self.move_pawns(from_XY, to_XY, 0)
            #     else:
            #         new_possible = temp_to_XY_moves.copy()
            #         while quit is True:
            #             to_XY = self.random_toXY(figure, from_XY, 1, new_possible)
            #             # coor = self.move_pawns(from_XY, to_XY, 1)
            #             if self.move_pawns(from_XY, to_XY, 1) is False and len(new_possible) != 1:
            #                 used = to_XY
            #                 new_possible.remove(used)
            #                 continue
            #             else:
            #                 quit = False
            #                 break

            #     used = temp_to_XY
            #     if self.move_pawns(from_XY, temp_to_XY, 1) is False:
            #         if len(possible_moves) != 1:
  # while quit:
            #     temp_to_XY = self.hard_opponent_coordinates_toXY_neutron(figure, from_XY, possible_moves)
            #     used = temp_to_XY
            #     # print(from_XY)
            #     # print(to_XY)
            #     if self.move_pawns(from_XY, temp_to_XY, 1) is False:
            #         if len(possible_moves) != 1:

            #             possible_moves.remove(used)
            #             quit = True
            #             continue
            #         else:
            #             quit = False
            #             break
            #     else:
            #         quit = False
            #         break