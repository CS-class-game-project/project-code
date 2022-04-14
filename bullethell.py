import random
import arcade
import math
import time

SCREEN_TITLE = "bullet hell"
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
SPRITE_SCALING = 0.5
MOVEMENT_SPEED = 5
class Player(arcade.Sprite):
    """ Player Class """

    def update(self):
        """ Move the player """
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.left < 0:
            self.left = 0
        elif self.right > SCREEN_WIDTH - 1:
            self.right = SCREEN_WIDTH - 1

        if self.bottom < 0:
            self.bottom = 0
        elif self.top > SCREEN_HEIGHT - 1:
            self.top = SCREEN_HEIGHT - 1

class MyGame(arcade.Window):

    def __init__(self, width, height, title):

        super().__init__(width, height, title)

        self.score = 0

        self.bullet_list1 = None
        self.bullet_list2 = None

        self.player_list = None
        self.player_sprite = None

        self.enemy_sprite = None
        self.background = None
        arcade.set_background_color(arcade.color.BLACK)
    def setup(self):
        #self.background = arcade.load_texture(r"")

        self.player_list = arcade.SpriteList()
        self.player_sprite = Player(r"C:\Users\emmet\Desktop\School_Code\bulletheck\darkknightsheet.png")

        self.player_sprite.center_x = SCREEN_WIDTH/2
        self.player_sprite.center_y = SCREEN_HEIGHT/2

        self.player_list.append(self.player_sprite)

    def on_draw(self):
        self.clear()
        self.player_list.draw()
    def on_update(self, delta_time: float):
        self.player_list.update()

    def on_key_press(self, key, modifiers):
        # If the player presses a key, update the speed
        if key == arcade.key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0
def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()
if __name__ == "__main__":
    main()