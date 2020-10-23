import arcade

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480


class MyGame(arcade.Window):

    def __init__(self, width, height, title):
        # Call the parent class's init function
        super().__init__(width, height, title)
        # Set the background color
        arcade.set_background_color(arcade.color.ASH_GREY)

        # Attributes to store where our ball is
        self.ball_x = 50
        self.ball_y = 50

    def on_draw(self):
        """Called whenever we need to draw the window."""
        arcade.start_render()
        arcade.draw_circle_filled(self.ball_x, self.ball_y, 15, arcade.color.AUBURN)

    # Animating by overriding the update method
    def update(self, delta_time):
        """ Called to update our objects. Happens aproximately 60 times per second. """
        self.ball_x += 1
        self.ball_y += 1

def main():
    # Using the Window Class
    # arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing Example")

    # Creating a Window with a Class
    # window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing Example")

    # Extending the Window Class
    window = MyGame(640, 480, "Drawing Example")

    arcade.run()


main()
