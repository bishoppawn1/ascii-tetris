tetris_board_chars_map = {
    0: "█",
    1: "▓",
    2: "▒",
    3: "░"
}


# converts one integer to ascii character
def int_to_ascii(i):

    return tetris_board_chars_map[i]

    # if (i == 0):
    #     return "█"
    # if (i == 1):
    #     return "▓"
    # if (i == 2):
    #     return "▒"
    # if (i == 3):
    #     return "░"
    # else:
    #     return


# convert int array to ascii characters

def int_array_to_ascii_characters(int_array):
    g = ""
    for index in range(len(int_array)):
        g += int_to_ascii(int_array[index])
    return g


def draw_int_array(int_array):
    print(int_array_to_ascii_characters(int_array))


draw_int_array([1, 0, 2, 1])