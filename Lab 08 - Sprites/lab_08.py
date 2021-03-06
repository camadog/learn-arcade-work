import random
import arcade

# --- Constants ---
SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_COIN = 0.2
COIN_COUNT = 50

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class Snake(arcade.Sprite):

    def reset_pos(self):
        # Reset the coin to a random spot above the screen
        self.center_y = random.randrange(SCREEN_HEIGHT)
        self.center_x = random.randrange(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100)

    def update(self):
        self.center_x -= 1
        # See if we went off-screen
        # if self.center_y < -20:
            # self.center_y = SCREEN_HEIGHT + 20
        if self.right < 0:
            # self.bottom = SCREEN_HEIGHT
            # Reset the coin to a random spot above the screen
            self.reset_pos()

class Coin(arcade.Sprite):

    def reset_pos(self):
        # Reset the coin to a random spot above the screen
        self.center_y = random.randrange(SCREEN_HEIGHT + 20,
                                         SCREEN_HEIGHT + 100)
        self.center_x = random.randrange(SCREEN_WIDTH)

    def update(self):
        self.center_y -= 1
        # See if we went off-screen
        # if self.center_y < -20:
            # self.center_y = SCREEN_HEIGHT + 20
        if self.top < 0:
            # self.bottom = SCREEN_HEIGHT
            # Reset the coin to a random spot above the screen
            self.reset_pos()

class MyGame(arcade.Window):
    """ Our custom Window Class"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprite Example")

        self.done = False

        # Variables that will hold sprite lists
        self.player_list = None
        self.snake_list = None
        self.coin_list = None

        # Set up the player info
        self.player_sprite = None
        self.score = 0

        #self.good_sound = arcade.load_sound("good.ogg")
        #self.bad_sound  = arcade.load_sound("bad.ogg")

        # Don't show the mouse cursor
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.snake_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()

        # Score
        self.score = 0

        # Set up the player
        # Character image from kenney.nl
        self.player_sprite = arcade.Sprite("rabbit.png", 0.1)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        # Create the coins
        for i in range(COIN_COUNT):

            # Create the coin instance
            # Coin image from kenney.nl
            coin = Coin(":resources:images/items/coinGold.png", SPRITE_SCALING_COIN)

            # Position the coin
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT)

            # Add the coin to the lists
            self.coin_list.append(coin)

        # Create the snakes
        for i in range(30):

            # snake image from kenney.nl
            snake = Snake("snake.png", 0.1)

            # Position the coin
            snake.center_x = random.randrange(SCREEN_WIDTH)
            snake.center_y = random.randrange(SCREEN_HEIGHT)

            # Add the coin to the lists
            self.snake_list.append(snake)

    def on_draw(self):
        """ Draw everything """
        arcade.start_render()
        self.snake_list.draw()
        self.coin_list.draw()
        self.player_list.draw()

        # Put the text on the screen.
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

        if self.done:
            arcade.draw_text("Game Over", 350, 300, arcade.color.WHITE, 18)

    def on_mouse_motion(self, x, y, dx, dy):
        """ Handle Mouse Motion """
        if self.done:
            return

        # Move the center of the player sprite to match the mouse x, y
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y

    def update(self, delta_time):
        """ Movement and game logic """
        if self.done:
            return
        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.coin_list.update()
        self.snake_list.update()

        # Generate a list of all sprites that collided with the player.
        coin_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                        self.coin_list)

        # Loop through each colliding sprite, remove it, and add to the score.
        for coin in coin_hit_list:

            self.score += 1
            # arcade.play_sound(self.good_sound)
            # Reset the coin to a random spot above the screen
            # coin.reset_pos()
            coin.remove_from_sprite_lists()

        snake_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                        self.snake_list)

        # Loop through each colliding sprite, remove it, and add to the score.
        for snake in snake_hit_list:

            self.score -= 1
            # arcade.play_sound(self.bad_sound)
            # Reset the coin to a random spot above the screen
            snake.reset_pos()

        if self.coin_list.__len__() <= 0:
            self.done = True



def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
