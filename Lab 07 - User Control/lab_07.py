""" Lab 7 - User Control """

import arcade

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

MOVEMENT_SPEED = 5
DEAD_ZONE = 0.02

# 8 is my pixel/box multiplier size...
BOX = 8
HLF = BOX / 2
QTR = HLF / 2

class BattleShip:
    def __init__(self, position_x, position_y, change_x, change_y, radius, color):

        # Take the parameters of the init function above, and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.radius = radius
        self.color = color

    def on_draw(self):
        """ Draw the battle ship """
        # arcade.draw_rectangle_filled(center_x, center_y, width, height, color)
        #width =  8 * 11
        #height = 8 * 8
        #arcade.draw_rectangle_outline(x, y, width, height, arcade.color.RED, 1)
        # Body
        arcade.draw_rectangle_filled(self.position_x, self.position_y - 2 * BOX - 4, 11 * BOX, 3 * BOX, self.color)
        arcade.draw_rectangle_filled(self.position_x, self.position_y - 4, 8 * BOX, BOX, self.color)
        arcade.draw_rectangle_filled(self.position_x, self.position_y + 4, 2 * BOX, BOX, self.color)
        arcade.draw_rectangle_filled(self.position_x, self.position_y + BOX + 4, BOX, BOX, self.color)


    def update(self, sound):
        # Move the ball
        self.position_y += self.change_y
        self.position_x += self.change_x
        # See if the ball hit the edge of the screen. If so, change direction
        if self.position_x < self.radius:
            self.position_x = self.radius
            arcade.play_sound(sound)

        if self.position_x > SCREEN_WIDTH - self.radius:
            self.position_x = SCREEN_WIDTH - self.radius
            arcade.play_sound(sound)

        if self.position_y < self.radius:
            self.position_y = self.radius
            arcade.play_sound(sound)

        if self.position_y > SCREEN_HEIGHT - self.radius:
            self.position_y = SCREEN_HEIGHT - self.radius
            arcade.play_sound(sound)

class RealInvader:
    def __init__(self, position_x, position_y, change_x, change_y, radius, color):

        # Take the parameters of the init function above, and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.radius = radius
        self.color = color

    def on_draw(self):
        """ Draw an invader 0 """
        # arcade.draw_rectangle_filled(center_x, center_y, width, height, color)

        # Body / face
        arcade.draw_rectangle_filled(self.position_x, self.position_y - 4, 7 * BOX, 5 * BOX, self.color)
        # Eyes
        arcade.draw_rectangle_filled(self.position_x - 2 * BOX, self.position_y + 4, BOX, BOX, arcade.color.BLACK)
        arcade.draw_rectangle_filled(self.position_x + 2 * BOX, self.position_y + 4, BOX, BOX, arcade.color.BLACK)
        # Mouth / cut ???
        arcade.draw_rectangle_filled(self.position_x, self.position_y - 20, 4 * BOX, BOX, arcade.color.BLACK)
        # Antena
        arcade.draw_rectangle_filled(self.position_x - 2 * BOX, self.position_y + 2 * BOX + 4, BOX, BOX, self.color)
        arcade.draw_rectangle_filled(self.position_x - 3 * BOX, self.position_y + 3 * BOX + 4, BOX, BOX, self.color)

        arcade.draw_rectangle_filled(self.position_x + 2 * BOX, self.position_y + 2 * BOX + 4, BOX, BOX, self.color)
        arcade.draw_rectangle_filled(self.position_x + 3 * BOX, self.position_y + 3 * BOX + 4, BOX, BOX, self.color)
        # Legs
        arcade.draw_rectangle_filled(self.position_x - BOX - 4, self.position_y - 3 * BOX - 4, 2 * BOX, BOX, self.color)
        arcade.draw_rectangle_filled(self.position_x + BOX + 4, self.position_y - 3 * BOX - 4, 2 * BOX, BOX, self.color)
        # Arms
        arcade.draw_rectangle_filled(self.position_x - 4 * BOX, self.position_y, BOX, 2 * BOX, self.color)
        arcade.draw_rectangle_filled(self.position_x - 5 * BOX, self.position_y - BOX - 4, BOX, 3 * BOX, self.color)

        arcade.draw_rectangle_filled(self.position_x + 4 * BOX, self.position_y, BOX, 2 * BOX, self.color)
        arcade.draw_rectangle_filled(self.position_x + 5 * BOX, self.position_y - BOX - 4, BOX, 3 * BOX, self.color)


    def update(self, sound):
        # Move the ball
        self.position_y += self.change_y
        self.position_x += self.change_x
        # See if the ball hit the edge of the screen. If so, change direction
        if self.position_x < self.radius:
            self.position_x = self.radius
            arcade.play_sound(sound)

        if self.position_x > SCREEN_WIDTH - self.radius:
            self.position_x = SCREEN_WIDTH - self.radius
            arcade.play_sound(sound)

        if self.position_y < self.radius:
            self.position_y = self.radius
            arcade.play_sound(sound)

        if self.position_y > SCREEN_HEIGHT - self.radius:
            self.position_y = SCREEN_HEIGHT - self.radius
            arcade.play_sound(sound)


def draw_invader_0(x, y, color):
    """ Draw an invader 0 """
    # arcade.draw_rectangle_filled(center_x, center_y, width, height, color)

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


class MyGame(arcade.Window):
    """ Our Custom Window Class"""

    def __init__(self):
        """ Initializer """

        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 7 - User Control")
        self.set_mouse_visible(False)

        self.ship = BattleShip(88, 32, 0, 0, 88, arcade.color.AUBURN)
        self.invader = RealInvader(88, 200, 0, 0, 88,arcade.color.AUBURN)

        self.laser_sound = arcade.load_sound("laser.ogg")
        self.sound = arcade.load_sound("another.ogg")

        joysticks = arcade.get_joysticks()
        if joysticks:
            self.joystick = joysticks[0]
            self.joystick.open()
        else:
            print("There are no joysticks.")
            self.joystick = None

    def on_draw(self):
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

        self.ship.on_draw()

        self.invader.on_draw()
        # draw_battle_ship(100, 32)

    def on_key_press(self, key, modifiers):
        """ Called whenever the user presses a key. """
        if key == arcade.key.LEFT:
            self.invader.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.invader.change_x = MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.invader.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.invader.change_y = -MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """ Called whenever a user releases a key. """
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.invader.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.invader.change_y = 0

    def on_mouse_press(self, x, y, button, modifiers):
        """ Called when the user presses a mouse button. """
        if button == arcade.MOUSE_BUTTON_LEFT:
            arcade.play_sound(self.laser_sound)

    def update(self, delta_time):
        # Update the position according to the game controller
        if self.joystick:
            # Set a "dead zone" to prevent drive from a centered joystick
            if abs(self.joystick.x) < DEAD_ZONE:
                self.ship.change_x = 0
            else:
                self.ship.change_x = self.joystick.x * MOVEMENT_SPEED

            # Set a "dead zone" to prevent drive from a centered joystick
            if abs(self.joystick.y) < DEAD_ZONE:
                self.ship.change_y = 0
            else:
                self.ship.change_y = -self.joystick.y * MOVEMENT_SPEED

        self.ship.update(self.sound)
        self.invader.update(self.sound)


def main():
    window = MyGame()
    arcade.run()


main()
