"""
Use sprites to scroll around a large screen.

Simple program to show basic sprite usage.

Artwork from http://kenney.nl

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.sprite_move_scrolling
"""

import random
import arcade
import os

SPRITE_SCALING = 0.5

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Sprite Move with Scrolling Screen Example"

# How many pixels to keep as a minimum margin between the character
# and the edge of the screen.
VIEWPORT_MARGIN = 40

MOVEMENT_SPEED = 5


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
        """
        Initializer
        """
        super().__init__(width, height, title)

        # Set the working directory (where we expect to find files) to the same
        # directory this .py file is in. You can leave this out of your own
        # code, but it is needed to easily run the examples using "python -m"
        # as mentioned at the top of this program.
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        # Sprite lists
        self.player_list = None

        # Set up the player
        self.player_sprite = None

        self.coin_list = None
        self.wall_list = None

        self.physics_engine = None

        # Used in scrolling
        self.view_bottom = 0
        self.view_left = 0

        self.coin_count = 0
        self.score = 0

        self.done = False

    def setup(self):
        """ Set up the game and initialize the variables. """
        self.done = False
        self.coin_count = 0
        self.score = 0

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()

        # Set up the player
        self.player_sprite = arcade.Sprite(":resources:images/animated_characters/female_person/femalePerson_idle.png", 0.4)
        self.player_sprite.center_x = 64
        self.player_sprite.center_y = 270
        self.player_list.append(self.player_sprite)

        # -- Set up several columns of walls
        """
        for x in range(200, 1650, 210):
            for y in range(0, 1000, 64):
                # Randomly skip a box so the player can find a way through
                if random.randrange(5) > 0:
                    wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", SPRITE_SCALING)
                    wall.center_x = x
                    wall.center_y = y
                    self.wall_list.append(wall)
        """


        # Adding some coins
        for i in range(128, 1920, 128):
            for j in range(128, 1920, 128):
                r = random.randrange(3)
                # Create the coin instance
                # Coin image from kenney.nl
                if r == 1 and j + 64 < 1920 - 128:
                    coin = arcade.Sprite(":resources:images/items/coinGold.png", SPRITE_SCALING)
                    # Position the coin
                    coin.center_x = i
                    coin.center_y = j + 64
                    # Add the coin to the lists
                    self.coin_count += 1
                    self.coin_list.append(coin)

        # Drawing arbitrary blocks
        for i in range(0, 1920, 448):
            for j in range(0, 1920, 256):
                collide = False
                for coin in self.coin_list:
                    if coin.collides_with_point([i + 64, j + 64]):
                        collide = True
                        break
                if not collide:
                    wall = arcade.Sprite(":resources:images/tiles/lockRed.png", SPRITE_SCALING)
                    wall.center_x = i + 64
                    wall.center_y = j + 64
                    self.wall_list.append(wall)

        # Drawing an square
        for i in range(0, 1920, 64):
            # Randomly skip a box so the player can find a way through
            wall = arcade.Sprite(":resources:images/tiles/brickGrey.png", SPRITE_SCALING)
            wall.center_x = i
            wall.center_y = 0
            self.wall_list.append(wall)

            wall = arcade.Sprite(":resources:images/tiles/brickGrey.png", SPRITE_SCALING)
            wall.center_x = i
            wall.center_y = 1920
            self.wall_list.append(wall)

            wall = arcade.Sprite(":resources:images/tiles/brickGrey.png", SPRITE_SCALING)
            wall.center_x = 0
            wall.center_y = i
            self.wall_list.append(wall)

            wall = arcade.Sprite(":resources:images/tiles/brickGrey.png", SPRITE_SCALING)
            wall.center_x = 1920
            wall.center_y = i
            self.wall_list.append(wall)

        # Drawing the maze...
        for i in range(128, 1920, 128):
                r = random.randrange(4)
                if r == 0:
                    # Line
                    for j in range(128, 1920, 128):
                        if j == 896:
                            continue
                        wall = arcade.Sprite(":resources:images/tiles/brickBrown.png", SPRITE_SCALING)
                        wall.center_x = j
                        wall.center_y = i
                        self.wall_list.append(wall)
                        if j + 64 < 1920 - 128:
                            wall = arcade.Sprite(":resources:images/tiles/brickBrown.png", SPRITE_SCALING)
                            wall.center_x = j + 64
                            wall.center_y = i
                            self.wall_list.append(wall)
                elif r == 1:
                    # Dots
                    for j in range(128, 1920, 128):
                        wall = arcade.Sprite(":resources:images/tiles/brickBrown.png", SPRITE_SCALING)
                        wall.center_x = j
                        wall.center_y = i
                        self.wall_list.append(wall)
                elif r == 2:
                    # Dash
                    for j in range(128, 1920, 256):
                        wall = arcade.Sprite(":resources:images/tiles/brickBrown.png", SPRITE_SCALING)
                        wall.center_x = j
                        wall.center_y = i
                        self.wall_list.append(wall)

                        wall = arcade.Sprite(":resources:images/tiles/brickBrown.png", SPRITE_SCALING)
                        wall.center_x = j + 64
                        wall.center_y = i
                        self.wall_list.append(wall)

                        wall = arcade.Sprite(":resources:images/tiles/brickBrown.png", SPRITE_SCALING)
                        wall.center_x = j + 128
                        wall.center_y = i
                        self.wall_list.append(wall)

                elif r == 3:
                    # Random
                    for j in range(128, 1920, 128):
                        wall = arcade.Sprite(":resources:images/tiles/brickBrown.png", SPRITE_SCALING)
                        wall.center_x = j
                        wall.center_y = i
                        self.wall_list.append(wall)
                        r = random.randrange(2)
                        if r == 1 and j + 64 < 1920 - 128:
                            wall = arcade.Sprite(":resources:images/tiles/brickBrown.png", SPRITE_SCALING)
                            wall.center_x = j + 64
                            wall.center_y = i
                            self.wall_list.append(wall)

        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)

        # Set the background color
        arcade.set_background_color(arcade.color.AMAZON)

        # Set the viewport boundaries
        # These numbers set where we have 'scrolled' to.
        self.view_left = 0
        self.view_bottom = 0

    def on_draw(self):
        """
        Render the screen.
        """
        # This command has to happen before we start drawing
        arcade.start_render()

        # Draw all the sprites.
        self.wall_list.draw()
        self.player_list.draw()
        self.coin_list.draw()

        output = f"Score: {self.score}"
        arcade.draw_text(output, self.view_left + 10, self.view_bottom + 20, arcade.color.WHITE, 14)

        output = f"Coins left: {self.coin_list.__len__()}"
        arcade.draw_text(output, self.view_left + 150, self.view_bottom + 20, arcade.color.WHITE, 14)

        if self.done:
            arcade.draw_text("Game Over", self.view_left + 350, self.view_bottom + 300, arcade.color.WHITE, 14)
            return

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """
        if self.done:
            return
        if key == arcade.key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

    def on_update(self, delta_time):
        """ Movement and game logic """
        if self.done:
            return
        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.physics_engine.update()

        self.coin_list.update()
        # --- Manage Scrolling ---

        coins_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)

        # Loop through each colliding sprite, remove it, and add to the score.
        for coin in coins_hit_list:
            coin.remove_from_sprite_lists()
            self.score += 1

        if self.coin_list.__len__() <= 0:
            self.done = True

        # Keep track of if we changed the boundary. We don't want to call the
        # set_viewport command if we didn't change the view port.
        changed = False

        # Scroll left
        left_boundary = self.view_left + VIEWPORT_MARGIN
        if self.player_sprite.left < left_boundary:
            self.view_left -= left_boundary - self.player_sprite.left
            changed = True

        # Scroll right
        right_boundary = self.view_left + SCREEN_WIDTH - VIEWPORT_MARGIN
        if self.player_sprite.right > right_boundary:
            self.view_left += self.player_sprite.right - right_boundary
            changed = True

        # Scroll up
        top_boundary = self.view_bottom + SCREEN_HEIGHT - VIEWPORT_MARGIN
        if self.player_sprite.top > top_boundary:
            self.view_bottom += self.player_sprite.top - top_boundary
            changed = True

        # Scroll down
        bottom_boundary = self.view_bottom + VIEWPORT_MARGIN
        if self.player_sprite.bottom < bottom_boundary:
            self.view_bottom -= bottom_boundary - self.player_sprite.bottom
            changed = True

        # Make sure our boundaries are integer values. While the view port does
        # support floating point numbers, for this application we want every pixel
        # in the view port to map directly onto a pixel on the screen. We don't want
        # any rounding errors.
        self.view_left = int(self.view_left)
        self.view_bottom = int(self.view_bottom)

        # If we changed the boundary values, update the view port to match
        if changed:
            arcade.set_viewport(self.view_left,
                                SCREEN_WIDTH + self.view_left,
                                self.view_bottom,
                                SCREEN_HEIGHT + self.view_bottom)


def main():
    """ Main method """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
