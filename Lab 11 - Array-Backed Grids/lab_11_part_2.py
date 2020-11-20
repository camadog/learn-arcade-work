import arcade

WIDTH  = 20
HEIGHT = 20
MARGIN = 5

ROW_COUNT    = 10
COLUMN_COUNT = 10

SCREEN_WIDTH  = (COLUMN_COUNT * WIDTH) + ((COLUMN_COUNT + 1) * MARGIN)
SCREEN_HEIGHT = (ROW_COUNT * HEIGHT) + ((ROW_COUNT + 1) * MARGIN)

class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.BLACK)

        self.selected = 0

        # Create an empty list
        self.grid = []
        # Loop for each row
        for row in range(ROW_COUNT):
            # For each row, create a list that will
            # represent an entire row
            self.grid.append([])
            # Loop for each column
            for column in range(COLUMN_COUNT):
                # Add a the number zero to the current row
                self.grid[row].append(0)

        # self.grid[1][5] = 1


    def on_draw(self):
        """
        Render the screen.
        """
        arcade.start_render()

        color = None

        for column in range(COLUMN_COUNT):
            x = MARGIN + column * (MARGIN + WIDTH) + WIDTH / 2
            for row in range(ROW_COUNT):
                color = arcade.color.WHITE
                if self.grid[row][column]:
                    color = arcade.color.GREEN

                y = MARGIN + row * (MARGIN + HEIGHT) + HEIGHT / 2
                arcade.draw_rectangle_filled(x, y, WIDTH, HEIGHT, color)


    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        if button == arcade.MOUSE_BUTTON_LEFT:
            column = x // (WIDTH + MARGIN)
            row = y // (HEIGHT + MARGIN)

            if self.grid[row][column] == 0:
                self.grid[row][column] = 1
                self.selected += 1
            else:
                self.grid[row][column] = 0
                self.selected -= 1

            str = "Total of {} cells are selected."
            print(str.format(self.selected))

            for row in range(ROW_COUNT):
                count = 0
                for column in range(COLUMN_COUNT):
                    if self.grid[row][column] == 1:
                        count += 1
                str = "Row {} has {} cells selected."
                print(str.format(row, count))

            for column in range(COLUMN_COUNT):
                count = 0
                for row in range(ROW_COUNT):
                    if self.grid[row][column] == 1:
                        count += 1
                str = "Column {} has {} cells selected."
                print(str.format(column, count))


def main():

    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()


if __name__ == "__main__":
    main()
