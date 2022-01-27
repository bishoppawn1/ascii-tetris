import time

tetris_board_chars_map = {
    0: "██",
    1: "▓▓",
    2: "▒▒",
    3: "░░",
    30: " .",
    31: "<!",
    32: "==",
    33: "\/",
    34: "  ",
    35: "!>"
}
classic_tetris_board = \
    [[31, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 35],
     [31, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 35],
     [31, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 35],
     [31, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 35],
     [31, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 35],
     [31, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 35],
     [31, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 35],
     [31, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 35],
     [31, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 35],
     [31, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 35],
     [31, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 35],
     [31, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 35],
     [31, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 35],
     [31, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 35],
     [31, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 35],
     [31, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 35],
     [34, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 34]]


# converts one integer to ascii character
def int_to_ascii(i):
    return tetris_board_chars_map[i]


# convert int array to ascii characters

def int_array_to_ascii_characters(int_array):
    g = ""
    for index in range(len(int_array)):
        g += int_to_ascii(int_array[index])
    return g


def draw_int_array(int_array):
    print(int_array_to_ascii_characters(int_array))


def int_2d_array_to_ascii_characters(int_2d_array):
    g = ""
    for index in range(len(int_2d_array)):
        g = g + int_array_to_ascii_characters(int_2d_array[index]) + "\n"
    return g

def draw_int_2d_array(int_2d_array):
    print(int_2d_array_to_ascii_characters(int_2d_array))

draw_int_2d_array(classic_tetris_board)

