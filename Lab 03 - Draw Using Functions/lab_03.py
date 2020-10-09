
import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
# 8 is my pixel/box multiplier size...
BOX = 8
HLF = BOX / 2
QTR = HLF / 2

def draw_invader_0(x, y, color):
    """ Draw an invader 0 """
    # arcade.draw_rectangle_filled(center_x, center_y, width, height, color)

    # width =  8 * 11
    # height = 8 * 8
    # arcade.draw_rectangle_outline(x, y, width, height, arcade.color.RED, 1)

    # Body / face
    arcade.draw_rectangle_filled(x, y - 4, 7 * BOX, 5 * BOX, color)
    # Eyes
    arcade.draw_rectangle_filled(x - 2 * BOX, y + 4, BOX, BOX, arcade.color.BLACK)
    arcade.draw_rectangle_filled(x + 2 * BOX, y + 4, BOX, BOX, arcade.color.BLACK)
    # Mouth / cut ???
    arcade.draw_rectangle_filled(x, y - 20, 4 * BOX, BOX, arcade.color.BLACK)
    # Antena
    arcade.draw_rectangle_filled(x - 2 * BOX, y + 2 * BOX + 4, BOX, BOX, color)
    arcade.draw_rectangle_filled(x - 3 * BOX, y + 3 * BOX + 4, BOX, BOX, color)

    arcade.draw_rectangle_filled(x + 2 * BOX, y + 2 * BOX + 4, BOX, BOX, color)
    arcade.draw_rectangle_filled(x + 3 * BOX, y + 3 * BOX + 4, BOX, BOX, color)
    # Legs
    arcade.draw_rectangle_filled(x - BOX - 4, y - 3 * BOX - 4, 2 * BOX, BOX, color)
    arcade.draw_rectangle_filled(x + BOX + 4, y - 3 * BOX - 4, 2 * BOX, BOX, color)
    # Arms
    arcade.draw_rectangle_filled(x - 4 * BOX, y, BOX, 2 * BOX, color)
    arcade.draw_rectangle_filled(x - 5 * BOX, y - BOX - 4, BOX, 3 * BOX, color)

    arcade.draw_rectangle_filled(x + 4 * BOX, y, BOX, 2 * BOX, color)
    arcade.draw_rectangle_filled(x + 5 * BOX, y - BOX - 4, BOX, 3 * BOX, color)

def draw_invader_1(x, y, color):
    """ Draw an invader 1 """
    # arcade.draw_rectangle_filled(center_x, center_y, width, height, color)

    # width =  8 * 11
    # height = 8 * 8
    # arcade.draw_rectangle_outline(x, y, width, height, arcade.color.RED, 1)

    # Body
    arcade.draw_rectangle_filled(x, y + BOX + 4, 9 * BOX, 5 * BOX, color)
    # Head shape / cut
    arcade.draw_rectangle_filled(x - 3 * BOX, y + 3 * BOX + 4, 3 * BOX, BOX, arcade.color.BLACK)
    arcade.draw_rectangle_filled(x - 4 * BOX, y + 2 * BOX + 4, BOX, BOX, arcade.color.BLACK)

    arcade.draw_rectangle_filled(x + 3 * BOX, y + 3 * BOX + 4, 3 * BOX, BOX, arcade.color.BLACK)
    arcade.draw_rectangle_filled(x + 4 * BOX, y + 2 * BOX + 4, BOX, BOX, arcade.color.BLACK)
    # Eyes
    arcade.draw_rectangle_filled(x - BOX - 4, y + 4, BOX + 4, BOX, arcade.color.BLACK)
    arcade.draw_rectangle_filled(x + BOX + 4, y + 4, BOX + 4, BOX, arcade.color.BLACK)
    # Legs
    arcade.draw_rectangle_filled(x - BOX - 4, y - BOX - 4, BOX + 4, BOX, color)
    arcade.draw_rectangle_filled(x - 2 * BOX, y - 2 * BOX - 4, BOX + 4, BOX, color)
    arcade.draw_rectangle_filled(x - 3 * BOX - 4, y - 3 * BOX - 4, BOX + 4, BOX, color)

    arcade.draw_rectangle_filled(x + BOX + 4, y - BOX - 4, BOX + 4, BOX, color)
    arcade.draw_rectangle_filled(x + 2 * BOX, y - 2 * BOX - 4, BOX + 4, BOX, color)
    arcade.draw_rectangle_filled(x + 3 * BOX + 4, y - 3 * BOX - 4, BOX + 4, BOX, color)
    # Nose / cut
    arcade.draw_rectangle_filled(x, y - 2 * BOX - 4, BOX + 4, BOX, color)

def draw_battle_ship(x, y):
    """ Draw the battle ship """
    # arcade.draw_rectangle_filled(center_x, center_y, width, height, color)
    #width =  8 * 11
    #height = 8 * 8
    #arcade.draw_rectangle_outline(x, y, width, height, arcade.color.RED, 1)

    # Body
    arcade.draw_rectangle_filled(x, y - 2 * BOX - 4, 11 * BOX, 3 * BOX, arcade.color.RED)
    arcade.draw_rectangle_filled(x, y - 4, 8 * BOX, BOX, arcade.color.RED)
    arcade.draw_rectangle_filled(x, y + 4, 2 * BOX, BOX, arcade.color.RED)
    arcade.draw_rectangle_filled(x, y + BOX + 4, BOX, BOX, arcade.color.RED)

def on_draw(delta_time):
    """ Draw everything """
    arcade.start_render()
    draw_invader_0(100, 500, arcade.color.YELLOW)
    draw_invader_1(200, 500, arcade.color.BLUE)
    draw_invader_0(300, 500, arcade.color.GREEN)
    draw_invader_1(400, 500, arcade.color.RED)
    draw_invader_0(500, 500, arcade.color.PURPLE)
    draw_invader_1(600, 500, arcade.color.MAGENTA)
    draw_invader_0(700, 500, arcade.color.BROWN)

    draw_invader_1(100, 400, arcade.color.DARK_OLIVE_GREEN)
    draw_invader_0(200, 400, arcade.color.DARK_RED)
    draw_invader_1(300, 400, arcade.color.DARK_GREEN)
    draw_invader_0(400, 400, arcade.color.DARK_TAN)
    draw_invader_1(500, 400, arcade.color.DARK_PASTEL_PURPLE)
    draw_invader_0(600, 400, arcade.color.DARK_TANGERINE)
    draw_invader_1(700, 400, arcade.color.TAUPE_GRAY)

    draw_battle_ship(on_draw.battle_ship_x, 32)

    # add some movement...
    on_draw.battle_ship_x += on_draw.x
    if on_draw.battle_ship_x <= 44 or on_draw.battle_ship_x >= SCREEN_WIDTH - 44:
        on_draw.x *= -1

on_draw.x = 4
on_draw.battle_ship_x = 44

def main():
    """ Description """
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
    arcade.set_background_color(arcade.color.BLACK)

    # Call on_draw every 60th of a second.
    arcade.schedule(on_draw, 1/60)
    # arcade.finish_render()
    arcade.run()

# Call the main function to get the program started.
main()
