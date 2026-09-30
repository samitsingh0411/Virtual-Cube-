from termcolor import colored

test_list = ["B1", "Y3", "O4"]
test_string = "abc"
color_test_string = colored(test_string, "black", on_color="on_green")


def assign_color(arg_input):
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
            output_string = colored(f'"{arg_input}"', "black", (193, 68, 0))
            return output_string


def print_list(arg_list):
    output_string = "["

    for i in range(0, len(arg_list) - 1):
        output_string = output_string + str(assign_color(arg_list[i])) + ", "

    output_string = output_string + str(assign_color(arg_list[-1]))
    output_string = output_string + "] "
    return output_string


print(color_test_string.center(50, "*"))
