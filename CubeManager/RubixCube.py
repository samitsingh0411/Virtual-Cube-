import json
import os
import random

from termcolor import colored

from CubeManager.alg_name import test_dict
from CubeManager.ErrorForCube import (
    InvalidInput,
    InvalidMove,
    PathNotFound,
    UnrecoganizedName,
)
from CubeManager.FaceClass import Face


# Utility Functions
def _rotate_list(_list, dir_flag=None):
    """
    Rotate with Normal Flag "n":
    Rotates a list in this way [a, b, c, d] ---> [d, a, b, c] (default)
    z
    Rotate with Opposite Flag "o"
    Rotates a list in this way [a, b, c, d] ---> [b, c, d, a]
    """

    if dir_flag is None or dir_flag == "n":
        last_element = _list[len(_list) - 1]
        for i in range(len(_list) - 1, 0, -1):
            _list[i] = _list[i - 1]
        _list[0] = last_element
        return _list
    elif dir_flag == "o":
        first_element = _list[0]
        for i in range(0, len(_list) - 1):
            _list[i] = _list[i + 1]
        _list[len(_list) - 1] = first_element
        return _list
    else:
        return _list


def _assign_color(arg_input):
    match arg_input[0]:
        case "W":
            output_string = colored(f'"{arg_input}"', "black", on_color="on_white")
            return output_string
        case "Y":
            output_string = colored(f'"{arg_input}"', "black", on_color="on_yellow")
            return output_string
        case "B":
            output_string = colored(f'"{arg_input}"', "black", on_color="on_blue")
            return output_string
        case "G":
            output_string = colored(f'"{arg_input}"', "black", on_color="on_green")
            return output_string
        case "R":
            output_string = colored(f'"{arg_input}"', "black", on_color="on_red")
            return output_string
        case "O":
            output_string = colored(f'"{arg_input}"', "black", on_color="on_cyan")
            return output_string


def _print_list(arg_list):
    output_string = "["

    for i in range(0, len(arg_list) - 1):
        output_string = output_string + str(_assign_color(arg_list[i])) + ", "

    output_string = output_string + str(_assign_color(arg_list[-1]))
    output_string = output_string + "] "
    return output_string


class Cube:
    def __init__(self, name, dimension):
        self.name = name
        self.dimension = dimension


class ThreeByThree(Cube):
    def __init__(self, name=None, load_path=None):

        if load_path is not None:
            if name is None:
                self.load(load_path, name)
            else:
                raise InvalidInput(
                    "Too many args, either enter name or enter path to load cube"
                )

        super().__init__(name, "3x3")

        self.Top = Face(
            "W", "top", [["W1", "W2", "W3"], ["W4", "W ", "W6"], ["W7", "W8", "W9"]]
        )

        self.Bottom = Face(
            "Y", "bottom", [["Y1", "Y2", "Y3"], ["Y4", "Y ", "Y6"], ["Y7", "Y8", "Y9"]]
        )

        self.Front = Face(
            "O", "front", [["O1", "O2", "O3"], ["O4", "O ", "O6"], ["O7", "O8", "O9"]]
        )

        self.Back = Face(
            "R", "back", [["R1", "R2", "R3"], ["R4", "R ", "R6"], ["R7", "R8", "R9"]]
        )

        self.Right = Face(
            "G", "right", [["G1", "G2", "G3"], ["G4", "G ", "G6"], ["G7", "G8", "G9"]]
        )

        self.Left = Face(
            "B", "left", [["B1", "B2", "B3"], ["B4", "B ", "B6"], ["B7", "B8", "B9"]]
        )

    def save(self, path_to_save=None):
        json_save_dict = {
            "Top": {
                "color": self.Top.color,
                "face_list": self.Top.face_list,
                "orient": "top",
            },
            "Bottom": {
                "color": self.Bottom.color,
                "face_list": self.Bottom.face_list,
                "orient": "bottom",
            },
            "Left": {
                "color": self.Left.color,
                "face_list": self.Left.face_list,
                "orient": "left",
            },
            "Right": {
                "color": self.Right.color,
                "face_list": self.Right.face_list,
                "orient": "right",
            },
            "Front": {
                "color": self.Front.color,
                "face_list": self.Front.face_list,
                "orient": "front",
            },
            "Back": {
                "color": self.Back.color,
                "face_list": self.Back.face_list,
                "orient": "back",
            },
        }

        if path_to_save is None:
            file_name = self.name + ".json"

        else:
            if os.path.exists(path_to_save):
                file_name = path_to_save

            else:
                raise PathNotFound("Path path provided for the file is wrong")

        with open(file_name, "w") as f:
            json.dump(json_save_dict, f, indent=4)
            print(self.name, "saved")

    def load(self, path_to_load, cube_name=None):
        try:
            with open(path_to_load, "r") as file:
                cube_dict = json.loads(file.read())
                if cube_name is not None:
                    self.name = cube_name
                else:
                    print("You have to provide a cube name")
                    return

                self.Top = Face(
                    color=cube_dict["Top"]["color"],
                    orient=cube_dict["Top"]["orient"],
                    face_list=cube_dict["Top"]["face_list"],
                )
                self.Bottom = Face(
                    color=cube_dict["Bottom"]["color"],
                    orient=cube_dict["Bottom"]["orient"],
                    face_list=cube_dict["Bottom"]["face_list"],
                )
                self.Left = Face(
                    color=cube_dict["Left"]["color"],
                    orient=cube_dict["Left"]["orient"],
                    face_list=cube_dict["Left"]["face_list"],
                )
                self.Right = Face(
                    color=cube_dict["Right"]["color"],
                    orient=cube_dict["Right"]["orient"],
                    face_list=cube_dict["Right"]["face_list"],
                )
                self.Front = Face(
                    color=cube_dict["Front"]["color"],
                    orient=cube_dict["Front"]["orient"],
                    face_list=cube_dict["Front"]["face_list"],
                )
                self.Back = Face(
                    color=cube_dict["Back"]["color"],
                    orient=cube_dict["Back"]["orient"],
                    face_list=cube_dict["Back"]["face_list"],
                )

        except FileNotFoundError:
            raise PathNotFound("The path you gave doesn't seem valid.")
        except PermissionError:
            print("Error: Permission denied. Unable to access the file.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    # Move Implementation

    def _R(self):
        # Moving Front Side
        temp = self.Bottom.get_left_row()
        self.Bottom.set_left_row(list(reversed(self.Back.get_right_row())))
        self.Back.set_right_row(self.Top.get_right_row())
        self.Top.set_right_row(self.Front.get_right_row())
        self.Front.set_right_row(list(reversed(temp)))

        # Rotataing adjacent face
        # Rotating Corners
        self.Right.set_corners(_rotate_list(self.Right.get_corners()))
        # Rotating Edges
        self.Right.set_edges(_rotate_list(self.Right.get_edges()))

    def _R_prime(self):
        for i in range(3):
            self._R()

    def _L(self):
        self.rotate("h", 2)
        self._R()
        self.rotate("h", 2)

    def _L_prime(self):
        self.rotate("h", 2)
        self._R_prime()
        self.rotate("h", 2)

    def _U(self):

        # Rotating sides
        temp_right_left = self.Right.get_left_row()

        self.Right.set_left_row(self.Back.get_bottom_row())
        self.Back.set_bottom_row(list(reversed(self.Left.get_right_row())))
        self.Left.set_right_row(self.Front.get_top_row())
        self.Front.set_top_row(list(reversed(temp_right_left)))

        # Rotating top face
        self.Top.set_corners(_rotate_list(self.Top.get_corners()))
        self.Top.set_edges(_rotate_list(self.Top.get_edges()))

        # self.rotate("h", 1)
        # self.rotate("v", 1)
        # self.rotate("h", 3)
        # self._R()
        # self.rotate("h", 1)
        # self.rotate("v", 3)
        # self.rotate("h", 3)
        pass

    def _U_prime(self):
        for i in range(3):
            self._U()

    def _F(self):
        self.rotate("v")
        self._U()
        self.rotate_prime("v")

    def _F_prime(self):
        self.rotate("v")
        self._U_prime()
        self.rotate_prime("v")

    def _B(self):
        self.rotate("h", 2)
        self._F()
        self.rotate("h", 2)

    def _B_prime(self):
        self.rotate("h", 2)
        self._F_prime()
        self.rotate("h", 2)

    def _D(self):
        self.rotate("v", 2)
        self._U()
        self.rotate("v", 2)

    def _D_prime(self):
        self.rotate("v", 2)
        self._U_prime()
        self.rotate("v", 2)

    def _M_prime(self):
        self.rotate("v")
        self._R()
        self._L_prime()

    def _M(self):
        self.rotate("v", dir="o")
        self._R()
        self._L_prime()

    def _E(self):
        self.rotate("h")
        self._D()
        self._U_prime()

    def _E_prime(self):
        self.rotate("h", dir="o")
        self._D_prime()
        self._U()

    def _r(self):
        self.rotate("v")
        self.do("L")

    def _r_prime(self):
        for i in range(3):
            self.rotate("v")
            self.do("L")

    def _l(self):
        self.rotate("v", dir="o")
        self.do("R")

    def _l_prime(self):
        for i in range(3):
            self.rotate("v", dir="o")
            self.do("R")

    def _u(self):
        self.rotate("h", dir="o")
        self.do("D")

    def _u_prime(self):
        for i in range(3):
            self.rotate("h", dir="o")
            self.do("D")

    def _d(self):
        self.rotate("h")
        self.do("U")

    def _d_prime(self):
        for i in range(3):
            self.rotate("h")
            self.do("U")

    def _b(self):
        self.do("z'")
        self.do("F")

    def _b_prime(self):
        for i in range(3):
            self.do("z'")
            self.do("F")

    def _f(self):
        self.do("z")
        self.do("B")

    def _f_prime(self):
        for i in range(3):
            self.do("z")
            self.do("B")

    def _r_horizontal(self):

        # Rotate Top
        self.Top.set_corners(_rotate_list(self.Top.get_corners()))
        self.Top.set_edges(_rotate_list(self.Top.get_edges()))

        # temp = self.Front
        temp_front_top_row = self.Front.get_top_row()
        temp_front_middle_row = self.Front.get_middle_row_h()
        temp_front_bottom_row = self.Front.get_bottom_row()

        # Right --> Front
        self.Front.set_top_row(list(reversed(self.Right.get_left_row())))
        self.Front.set_middle_row_h(list(reversed(self.Right.get_middle_row_v())))
        self.Front.set_bottom_row(list(reversed(self.Right.get_right_row())))

        # Back --> Right
        self.Right.set_right_row(self.Back.get_top_row())
        self.Right.set_middle_row_v(self.Back.get_middle_row_h())
        self.Right.set_left_row(self.Back.get_bottom_row())

        # Left --> Back
        self.Back.set_top_row(list(reversed(self.Left.get_left_row())))
        self.Back.set_middle_row_h(list(reversed(self.Left.get_middle_row_v())))
        self.Back.set_bottom_row(list(reversed(self.Left.get_right_row())))

        # Left --> Front
        self.Left.set_right_row(temp_front_top_row)
        self.Left.set_middle_row_v(temp_front_middle_row)
        self.Left.set_left_row(temp_front_bottom_row)

        # Rotate Bottom
        self.Bottom.set_corners(_rotate_list(self.Bottom.get_corners(), "o"))
        self.Bottom.set_edges(_rotate_list(self.Bottom.get_edges(), "o"))

    def _r_veritcal(self):
        # Rotating vertical fases

        temp_top_top_row = self.Top.get_top_row()
        temp_top_middle_row = self.Top.get_middle_row_h()
        temp_top_bottom_row = self.Top.get_bottom_row()

        # Back --> Top
        self.Top.set_top_row(self.Back.get_top_row())
        self.Top.set_middle_row_h(self.Back.get_middle_row_h())
        self.Top.set_bottom_row(self.Back.get_bottom_row())

        # Bottom --> Back
        self.Back.set_top_row(list(reversed(self.Bottom.get_bottom_row())))
        self.Back.set_middle_row_h(list(reversed(self.Bottom.get_middle_row_h())))
        self.Back.set_bottom_row(list(reversed(self.Bottom.get_top_row())))

        # Front --> Bottom
        self.Bottom.set_top_row(list(reversed(self.Front.get_bottom_row())))
        self.Bottom.set_middle_row_h(list(reversed(self.Front.get_middle_row_h())))
        self.Bottom.set_bottom_row(list(reversed(self.Front.get_top_row())))

        # Top --> Front
        self.Front.set_top_row(temp_top_top_row)
        self.Front.set_middle_row_h(temp_top_middle_row)
        self.Front.set_bottom_row(temp_top_bottom_row)

        # Rotating adjacent faces
        # Left
        self.Left.set_corners(_rotate_list(self.Left.get_corners()))
        self.Left.set_edges(_rotate_list(self.Left.get_edges()))

        # Right (counter-clockwise rotation here)
        self.Right.set_corners(_rotate_list(self.Right.get_corners(), "o"))
        self.Right.set_edges(_rotate_list(self.Right.get_edges(), "o"))

    def rotate_prime(self, axis, times=1):
        if axis == "h":
            for i in range(times):
                self._r_horizontal()
            return
        if axis == "v":
            for i in range(times):
                self._r_veritcal()
            return

    def rotate(self, axis, times=1, dir=None):
        """
        Rotates the cube some number of times in a give direction vertically or horizontally clockwise or anti-clockwise
        n (normal) => LEFT to RIGHT or DOWN to UP
        o (opposite) => RIGHT to LEFT or Down to UP
        """

        if dir == "n" or dir is None:
            if axis == "h":
                for i in range(times * 3):
                    self._r_horizontal()
                return
            if axis == "v":
                for i in range(times * 3):
                    self._r_veritcal()
                return
        elif dir == "o":
            if axis == "h":
                for i in range(times):
                    self._r_horizontal()
                return
            if axis == "v":
                for i in range(times):
                    self._r_veritcal()
                return

    def _do_using_list(self, move_list):
        for i in move_list:
            match i[-1]:
                case "2":
                    times = 2
                    move = i[:-1]
                    print(move)
                case "3":
                    times = 3
                    move = i[:-1]
                    ## string string to remove the last element from it and make move = new_string
                case _:
                    times = 1
                    move = i

            match move:
                case "R":
                    for i in range(times):
                        self._R()
                case "R'":
                    for i in range(times):
                        self._R_prime()
                case "L":
                    for i in range(times):
                        self._L()
                case "L'":
                    for i in range(times):
                        self._L_prime()
                case "U":
                    for i in range(times):
                        self._U()
                case "U'":
                    for i in range(times):
                        self._U_prime()
                case "F":
                    for i in range(times):
                        self._F()
                case "F'":
                    for i in range(times):
                        self._F_prime()
                case "B":
                    for i in range(times):
                        self._B()
                case "B'":
                    for i in range(times):
                        self._B_prime()
                case "D":
                    for i in range(times):
                        self._D()
                case "D'":
                    for i in range(times):
                        self._D_prime()
                case "M":
                    for i in range(times):
                        self._M()
                case "M'":
                    for i in range(times):
                        self._M_prime()
                case "E":
                    for i in range(times):
                        self._E()
                case "E'":
                    for i in range(times):
                        self._E_prime()
                case "x":
                    for i in range(times):
                        self.rotate("v")
                case "x'":
                    for i in range(times):
                        self.rotate("v", dir="o")
                case "y":
                    for i in range(times):
                        self.rotate("h", dir="o")
                case "y'":
                    for i in range(times):
                        self.rotate("h")
                case "z":
                    for i in range(times):
                        self.rotate("h")
                        self.rotate("v")
                        self.rotate("h", dir="o")
                case "z'":
                    for i in range(times):
                        self.rotate("h", dir="o")
                        self.rotate("v")
                        self.rotate("h")
                case "r":
                    for i in range(times):
                        self._r()
                case "r'":
                    for i in range(times):
                        self._r_prime()
                case "l":
                    for i in range(times):
                        self._l()
                case "l'":
                    for i in range(times):
                        self._l_prime()
                case "u":
                    for i in range(times):
                        self._u()
                case "u'":
                    for i in range(times):
                        self._u_prime()
                case "d":
                    for i in range(times):
                        self._d()
                case "d'":
                    for i in range(times):
                        self._d_prime()
                case "f":
                    for i in range(times):
                        self._f()
                case "f'":
                    for i in range(times):
                        self._f_prime()
                case "b":
                    for i in range(times):
                        self._b()
                case "b'":
                    for i in range(times):
                        self._b_prime()
                case _:
                    raise InvalidMove(
                        f" {i} is not a valid cube move. \n Pick from these [\"R, R', L, L', U, U', F, F' or B, B']"
                    )
        return

    def do(self, move_arg=None, move_list=None, alg_name=None, times_arg=1):
        """
        Does the following moves on the cube: R, R', L, L', U, U', F, F', B, B', D, D'.
        You can enter them individually or pass a list of them.
        """
        if type(times_arg) is not int:
            raise InvalidInput('The "times" value must be an int')

        # Doing move using list
        if move_list is not None:
            if move_arg is None and alg_name is None:
                self._do_using_list(move_list)
                return self
            else:
                raise InvalidInput(
                    "You can only enter either single moves or a list of them, enter a list like so [\"R, R', L, L', U, U', F, F' or B, B']: 1"
                )

        # Doing moves using notations
        elif move_arg is not None:
            if move_list is not None and alg_name is not None:
                raise InvalidInput(
                    "You can only enter either single moves or a list of them, enter a list like so [\"R, R', L, L', U, U', F, F' or B, B']: 2"
                )

            else:
                match move_arg[-1]:
                    case "2":
                        times = 2
                        move = move_arg[:-1]
                        print(move)
                    case "3":
                        times = 3
                        move = move_arg[:-1]
                        ## new string, removes the last element from it and make move = new_string
                    case _:
                        times = times_arg
                        move = move_arg

                match move:
                    case "R":
                        for i in range(times):
                            self._R()
                    case "R'":
                        for i in range(times):
                            self._R_prime()
                    case "L":
                        for i in range(times):
                            self._L()
                    case "l'":
                        for i in range(times):
                            self._L_prime()
                    case "U":
                        for i in range(times):
                            self._U()
                    case "U'":
                        for i in range(times):
                            self._U_prime()
                    case "F":
                        for i in range(times):
                            self._F()
                    case "F'":
                        for i in range(times):
                            self._F_prime()
                    case "B":
                        for i in range(times):
                            self._B()
                    case "B'":
                        for i in range(times):
                            self._B_prime()
                    case "D":
                        for i in range(times):
                            self._D()
                    case "D'":
                        for i in range(times):
                            self._D_prime()
                    case "M":
                        for i in range(times):
                            self._M()
                    case "M'":
                        for i in range(times):
                            self._M_prime()
                    case "E":
                        for i in range(times):
                            self._E()
                    case "E'":
                        for i in range(times):
                            self._E_prime()
                    case "x":
                        for i in range(times):
                            self.rotate("v")
                    case "x'":
                        for i in range(times):
                            self.rotate("v", dir="o")
                    case "y":
                        for i in range(times):
                            self.rotate("h", dir="o")
                    case "y'":
                        for i in range(times):
                            self.rotate("h")
                    case "z":
                        for i in range(times):
                            self.rotate("h")
                            self.rotate("v")
                            self.rotate("h", dir="o")
                    case "z'":
                        for i in range(times):
                            self.rotate("h", dir="o")
                            self.rotate("v")
                            self.rotate("h")

                    case "r":
                        for i in range(times):
                            self._r()

                    case "r'":
                        for i in range(times):
                            self._r_prime()

                    case "l":
                        for i in range(times):
                            self._l()

                    case "l'":
                        for i in range(times):
                            self._l_prime()

                    case "u":
                        for i in range(times):
                            self._u()

                    case "u'":
                        for i in range(times):
                            self._u_prime()

                    case "d":
                        for i in range(times):
                            self._d()

                    case "d'":
                        for i in range(times):
                            self._d_prime()

                    case "f":
                        for i in range(times):
                            self._f()

                    case "f'":
                        for i in range(times):
                            self._f_prime()

                    case "b":
                        for i in range(times):
                            self._b()

                    case "b'":
                        for i in range(times):
                            self._b_prime()

                    case _:
                        raise InvalidMove(
                            f" {move} is not a valid cube move. \n Pick from these [\"R, R', L, L', U, U', F, F', D, D', B, B']"
                        )

        # Doing moves using alg name
        elif alg_name is not None:
            if alg_name not in test_dict:
                raise UnrecoganizedName(
                    "The alg name you entered is not recoganized. \n Use <CubeObject>.list_alg() to get full list of supported algs names"
                )
            else:
                self._do_using_list(test_dict[alg_name])
                return self

        return self

    def shuffle(self, shuffle_length=15):
        """
        Shuffles the cube and returns the shuffle sequence in the form of a list.
        """
        moves_list = ["R", "R'", "L", "L'", "U", "U'", "F", "F'", "D", "D'", "B", "B'"]
        rand_move_list = []
        for i in range(shuffle_length):
            rand_move_list.append(random.choice(moves_list))

        self.do(move_list=rand_move_list)
        return rand_move_list

    def solve(self):
        self.Top = Face(
            "W", "top", [["W1", "W2", "W3"], ["W4", "W ", "W6"], ["W7", "W8", "W9"]]
        )

        self.Bottom = Face(
            "Y", "bottom", [["Y1", "Y2", "Y3"], ["Y4", "Y ", "Y6"], ["Y7", "Y8", "Y9"]]
        )

        self.Front = Face(
            "O", "front", [["O1", "O2", "O3"], ["O4", "O ", "O6"], ["O7", "O8", "O9"]]
        )

        self.Back = Face(
            "R", "back", [["R1", "R2", "R3"], ["R4", "R ", "R6"], ["R7", "R8", "R9"]]
        )

        self.Right = Face(
            "G", "right", [["G1", "G2", "G3"], ["G4", "G ", "G6"], ["G7", "G8", "G9"]]
        )

        self.Left = Face(
            "B", "left", [["B1", "B2", "B3"], ["B4", "B ", "B6"], ["B7", "B8", "B9"]]
        )

        return self

    def __str__(self):

        # print the back face
        spacing_1 = 102
        for i in self.Back.face_list:
            print(_print_list(i).center(spacing_1))  # center(47)
        print()
        # print the middle line including right, top, left, bottom
        print(
            _print_list(self.Left.face_list[0]),
            _print_list(self.Top.face_list[0]),
            _print_list(self.Right.face_list[0]),
            _print_list(self.Bottom.face_list[0]),
        )
        print(
            _print_list(self.Left.face_list[1]),
            _print_list(self.Top.face_list[1]),
            _print_list(self.Right.face_list[1]),
            _print_list(self.Bottom.face_list[1]),
        )
        print(
            _print_list(self.Left.face_list[2]),
            _print_list(self.Top.face_list[2]),
            _print_list(self.Right.face_list[2]),
            _print_list(self.Bottom.face_list[2]),
        )
        print()

        # print the front face
        for i in self.Front.face_list:
            print(_print_list(i).center(spacing_1))
        return f"{self.name}".center(100, ".")
