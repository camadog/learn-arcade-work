import arcade


def draw_section_outlines():
    # Draw squares on bottom
    arcade.draw_rectangle_outline(150, 150, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(450, 150, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(750, 150, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(1050, 150, 300, 300, arcade.color.BLACK)

    # Draw squares on top
    arcade.draw_rectangle_outline(150, 450, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(450, 450, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(750, 450, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(1050, 450, 300, 300, arcade.color.BLACK)


def draw_section_1():
    for row in range(30):
        for column in range(30):
            x = 5 + (10 * column)  # Instead of zero, calculate the proper x location using 'column'
            y = 5 + (10 * row) # Instead of zero, calculate the proper y location using 'row'
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)

def draw_section_2():
    color = arcade.color.BLACK
    for row in range(30):
        for column in range(30):
            x = 305 + (10 * column)
            y = 5 + (10 * row)
            if column % 2 == 0:
                color = arcade.color.WHITE
            else:
                color = arcade.color.BLACK
            arcade.draw_rectangle_filled(x, y, 5, 5, color)

def draw_section_3():
    color = arcade.color.BLACK
    for row in range(30):
        if color == arcade.color.WHITE:
            color = arcade.color.BLACK
        elif color == arcade.color.BLACK:
            color = arcade.color.WHITE
        for column in range(30):
            x = 605 + (10 * column)
            y = 5 + (10 * row)
            arcade.draw_rectangle_filled(x, y, 5, 5, color)

def draw_section_4():
    color = arcade.color.BLACK
    for row in range(30):
        for column in range(30):
            if column % 2 == 1:
                    color = arcade.color.BLACK
            elif row % 2 == 0:
                color = arcade.color.WHITE
            x = 905 + (10 * column)
            y = 5 + (10 * row)
            arcade.draw_rectangle_filled(x, y, 5, 5, color)

def draw_section_5():
    color = arcade.color.WHITE
    for row in range(30, 0, -1):
        for column in range(row, 30, 1):
            x = 5 + (10 * column)
            y = 295 + (10 * row)
            arcade.draw_rectangle_filled(x, y, 5, 5, color)

def draw_section_6():
    color = arcade.color.WHITE
    for row in range(31, 0, -1):
        for column in range(31 - row, 0, -1):
            x = 295 + (10 * column)
            y = 295 + (10 * row)
            arcade.draw_rectangle_filled(x, y, 5, 5, color)

def draw_section_7():
    color = arcade.color.WHITE
    for row in range(30, 0, -1):
        for column in range(0, row, 1):
            x = 605 + (10 * column)
            y = 295 + (10 * row)
            arcade.draw_rectangle_filled(x, y, 5, 5, color)

def draw_section_8():
    color = arcade.color.WHITE
    for row in range(30, 0, -1):
        for column in range(0, row, 1):
            x = 1195 - (10 * column)
            y = 295 + (10 * row)
            arcade.draw_rectangle_filled(x, y, 5, 5, color)


def main():
    # Create a window
    arcade.open_window(1200, 600, "Lab 05 - Loopy Lab")
    arcade.set_background_color(arcade.color.AIR_FORCE_BLUE)

    arcade.start_render()

    # Draw the outlines for the sections
    draw_section_outlines()

    # Draw the sections
    draw_section_1()
    draw_section_2()
    draw_section_3()
    draw_section_4()
    draw_section_5()
    draw_section_6()
    draw_section_7()
    draw_section_8()

    arcade.finish_render()

    arcade.run()


main()
