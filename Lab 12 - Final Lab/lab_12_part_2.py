#   Images:
#   All images used in this project were obtained from Kenney at https://kenney.nl/

import arcade

# --- Constants ---
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 480

TILE_SCALING = 0.5

MOVEMENT_SPEED = 5

LEFT = 0
RIGHT = 1

PLAYER_START_X = 200
PLAYER_START_Y = 40

class Frog(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.lives = 5
        self.score = 0
        self.scale = 0.5
        self.center_x = PLAYER_START_X
        self.center_y = PLAYER_START_Y
        self.change_x = 0
        self.change_y = 0
        self.texture = arcade.load_texture("sprites/frog.png")
        self.set_hit_box([(-8,-8),(-8,8),(8,8),(8,-8)])

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y
        

class Vehicle(arcade.Sprite):
    def __init__(self, x, y, image, speed, direction):
        super().__init__()
        
        self.scale = 2
        
        self.over = False
        self.speed = speed
        self.direction = direction
        
        self.center_x = x
        self.center_y = y
        
        if direction == LEFT:
            self.texture = arcade.load_texture(image, flipped_horizontally=True)
        else: 
            self.texture = arcade.load_texture(image)

    def update(self):
        """ Comment """
        if self.direction == RIGHT:
            self.center_x += self.speed
            if self.left > SCREEN_WIDTH:
                self.right = 0
        else:
            self.center_x -= self.speed
            if self.right < 0:
                self.left = SCREEN_WIDTH

class Platform(Vehicle):
    def __init__(self, x, y, image, speed, direction, frog):
        super().__init__(x, y, image, speed, direction)
        self.scale = 0.5
        self.frog = frog
        
        self.dive = False
        self.image = image
        
    def update(self):
        super().update()
        if self.over and self.direction == RIGHT:
            self.frog.center_x += self.speed
            self.over = False
        elif self.over and self.direction == LEFT:
            self.frog.center_x -= self.speed
            self.over = False
            
        if self.dive:
            self.fcount +=1
            if self.fcount == 120:
                self.fcount = 0
                self.diving = not self.diving
                if not self.diving: 
                    if self.direction == LEFT:
                        self.texture = arcade.load_texture(self.image, flipped_horizontally=True)
                    else: 
                        self.texture = arcade.load_texture(self.image)
                else:
                    self.texture = arcade.load_texture("sprites/platformPack_tile017.png")

    def set_dive(self):
        self.dive = True
        self.diving = False
        self.fcount = 0
        
        
class MyGame(arcade.Window):
    """ Our custom Window Class"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Final Lab - Frogger Game")
        arcade.set_background_color(arcade.color.LIGHT_BLUE)
        self.set_mouse_visible(False)

        self.player = None
        
        self.player_list = None
        self.car_list = None
        self.platform_list = None
        
        self.wall_list = None
        self.background_list = None
        self.foreground_list = None
        self.water_list = None
        self.finish_list = None
        self.win_list = None
        
        self.physics_engine = None

        self.done = False
        self.complete = False
        
        self.gameover = arcade.load_sound("gameover4.wav")

    def setup(self):
        """ Set up the game and initialize the variables. """
        self.player = Frog()
        self.player_list = arcade.SpriteList()
        self.player_list.append(self.player);
        
        self.car_list = arcade.SpriteList()
        self.platform_list = arcade.SpriteList()
        
        sprt1 = [
            "sprites/sedan.png", 
            "sprites/sedan_blue.png",
            "sprites/sedan.png", 
            "sprites/sedan_blue.png",
        ]
        
        st1 = [0, 140, 280, 420]
        st2 = [0, 175, 350]
        
        #Street 1
        speed = 1
        i = 0
        for x in st1:
            car = Vehicle(x, 80, sprt1[i], speed, RIGHT)
            self.car_list.append(car)
            i+=1
        #Street 2
        speed+=1
        for x in st2:
            car = Vehicle(x, 134, "sprites/ambulance.png", speed, LEFT)
            self.car_list.append(car)
        #Street 3
        speed+=1
        i = 0
        for x in st1:
            car = Vehicle(x, 200, sprt1[i], speed, RIGHT)
            self.car_list.append(car)
            i+=1
        #Turtles 1
        speed = 1
        for x in st2:
            platform = Platform(x, 272, "sprites/platformPack_tile041.png", speed, LEFT, self.player)
            if x == 175:
                platform.set_dive()
            self.platform_list.append(platform)
            platform = Platform(x + 32, 272, "sprites/platformPack_tile041.png", speed, LEFT, self.player)
            if x == 175:
                platform.set_dive()
            self.platform_list.append(platform)
        #Platforms 1
        for x in st1:
            pla = Platform(x, 304, "sprites/platformPack_tile004.png", speed, RIGHT, self.player)
            self.platform_list.append(pla)
            pla = Platform(x + 32, 304, "sprites/platformPack_tile004.png", speed, RIGHT, self.player)
            self.platform_list.append(pla)
        #Big Log
        speed += 1
        for x in range(0, 128, 32):
            pla = Platform(x, 336, "sprites/platformPack_tile004.png", speed, RIGHT, self.player)
            self.platform_list.append(pla)
        #Turtles 2
        for x in st2:
            platform = Platform(x, 368, "sprites/platformPack_tile041.png", speed, LEFT, self.player)
            self.platform_list.append(platform)
            if x == 175:
                platform.set_dive()
            platform = Platform(x + 32, 368, "sprites/platformPack_tile041.png", speed, LEFT, self.player)
            self.platform_list.append(platform)
            if x == 175:
                platform.set_dive()
        
        str1 = [
            [10, 400], [185, 400], [360, 400]
        ]
        
        for coords in str1:
            pla = Platform(coords[0], coords[1], "sprites/platformPack_tile004.png", speed, RIGHT, self.player)
            self.platform_list.append(pla)
            pla = Platform(coords[0] + 32, coords[1], "sprites/platformPack_tile004.png", speed, RIGHT, self.player)
            self.platform_list.append(pla)
            pla = Platform(coords[0] + 64, coords[1], "sprites/platformPack_tile004.png", speed, RIGHT, self.player)
            self.platform_list.append(pla)
        
        
        self.wall_list = arcade.SpriteList()
        self.background_list = arcade.SpriteList()
        self.foreground_list = arcade.SpriteList()
        self.water_list = arcade.SpriteList()
        self.finish_list = arcade.SpriteList()
        self.win_list = arcade.SpriteList()
        
        map = arcade.tilemap.read_tmx("frogger.tmx")
        
        self.wall_list = arcade.tilemap.process_layer(map_object=map,
                                                      layer_name="Walls",
                                                      scaling=TILE_SCALING,
                                                      use_spatial_hash=True)
        self.background_list = arcade.tilemap.process_layer(map_object=map,
                                                      layer_name="Background",
                                                      scaling=TILE_SCALING,
                                                      use_spatial_hash=True)
        self.foreground_list = arcade.tilemap.process_layer(map_object=map,
                                                      layer_name="Foreground",
                                                      scaling=TILE_SCALING,
                                                      use_spatial_hash=True)
        self.water_list = arcade.tilemap.process_layer(map_object=map,
                                                      layer_name="Water",
                                                      scaling=TILE_SCALING,
                                                      use_spatial_hash=True)
        self.finish_list = arcade.tilemap.process_layer(map_object=map,
                                                      layer_name="Finish",
                                                      scaling=TILE_SCALING,
                                                      use_spatial_hash=True)
        
        self.physics_engine = arcade.PhysicsEngineSimple(self.player, self.wall_list)
            
            

    def on_draw(self):
        """ Draw everything """
        arcade.start_render()
        
        self.background_list.draw()
        self.foreground_list.draw()
        self.water_list.draw()
        self.finish_list.draw()
        self.win_list.draw()

        self.platform_list.draw()
        
        self.player_list.draw()
        #self.player_list.draw_hit_boxes(arcade.color.RED)
        
        self.car_list.draw()
        
        """ I have problems with Pillow :( """
        #arcade.draw_text(f"Lives: {self.player.lives}", 20, 5, arcade.color.BLACK, 16)
        #arcade.draw_text(f"Score: {self.player.score}", 100, 5, arcade.color.BLACK, 16)
        
        if self.complete:
            arcade.draw_text("You Win", 180, 220, arcade.color.BLACK, 26)
        elif self.done:
            arcade.draw_text("Game Over", 180, 220, arcade.color.BLACK, 26)

    def update(self, delta_time):
        """ Movement and game logic """
        self.physics_engine.update()
        self.platform_list.update()
        self.car_list.update()
        
        die = False
        win = False
        
        #Collision
        carhit = arcade.check_for_collision_with_list(self.player, self.car_list)
        if carhit:
            die = True
            arcade.play_sound(self.gameover)
            
        over = arcade.check_for_collision_with_list(self.player, self.platform_list)
        finish = arcade.check_for_collision_with_list(self.player, self.finish_list)
        if finish:
            win = arcade.Sprite("sprites/platformPack_tile011.png", 0.5)
            win.center_x = finish[0].center_x
            win.center_y = finish[0].center_y
            self.win_list.append(win)
            finish[0].remove_from_sprite_lists()
            if not len(self.finish_list):
                self.complete = True
                self.done = True
        elif over:
            over[0].over = True
            if over[0].dive and over[0].diving:
                die = True
        else:
            drown = arcade.check_for_collision_with_list(self.player, self.water_list)
            if drown:
                die = True
                
        if win:
            self.player.center_x = PLAYER_START_X
            self.player.center_y = PLAYER_START_Y
            self.player.score += 100
        
        if die:
            self.player.center_x = PLAYER_START_X
            self.player.center_y = PLAYER_START_Y
            self.player.lives -= 1
        
        if self.player.lives <= 0:
            self.done = True

        
    def on_key_press(self, key, modifiers):
        """ Called whenever the user presses a key. """
        if self.done:
            return
        if key == arcade.key.LEFT:
            self.player.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player.change_x = MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.player.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player.change_y = -MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """ Called whenever a user releases a key. """
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.player.change_y = 0


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()
