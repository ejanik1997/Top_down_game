import arcade
from math import sqrt
import random

WIDTH = 1920
HEIGHT = 1080
MOVEMENT_SPEED = 2
ENEMY_SPEED_MODIFIER = 0.75
PLAYER_SPEED_MODIFIER = 1.25
PLAYER_SCALE = 0.75
GAME_NAME = "SWORDS AND SANDALS 9999"
ENEMY_COUNT = 3


class untitled(arcade.Window):
    def __init__(self):
        super().__init__(WIDTH, HEIGHT, GAME_NAME, fullscreen=True)
        arcade.set_background_color(arcade.color.AMAZON)
        self.player_list = None
        self.enemy_list = None
        self.enemy = None
        self.player = None
        self.set_mouse_visible(False)

    def setup(self):
        self.player_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()
        self.player = arcade.AnimatedWalkingSprite()

        self.player.stand_left_textures = []
        self.player.stand_right_textures = []
        self.player.walk_left_textures = []
        self.player.walk_right_textures = []
        self.player.walk_down_textures = []
        self.player.walk_up_textures = []

        self.load_9x4_sprite("player")
        self.player_list.append(self.player)

        for i in range(ENEMY_COUNT):
            self.enemy = arcade.AnimatedWalkingSprite()
            self.enemy.stand_left_textures = []
            self.enemy.stand_right_textures = []
            self.enemy.walk_left_textures = []
            self.enemy.walk_right_textures = []
            self.enemy.walk_down_textures = []
            self.enemy.walk_up_textures = []
            self.load_9x4_sprite("enemy")
            self.enemy.center_x = random.randrange(50, 1870)
            self.enemy.center_y = random.randrange(50, 1020)
            self.enemy_list.append(self.enemy)

    def load_9x4_sprite(self, arg):
        if arg == "player":
            self.player.stand_left_textures.append(arcade.load_texture("images/player/tile009.png"))
            self.player.stand_right_textures.append(arcade.load_texture("images/player/tile027.png"))
            self.player.scale = 0.8
            self.player.texture_change_distance = 20
            self.player.center_x = WIDTH // 2
            self.player.center_y = HEIGHT // 2
            for i in range(9):
                self.player.walk_up_textures.append(arcade.load_texture("images/player/tile00" + str(i) + ".png"))
            for i in range(10, 18):
                self.player.walk_left_textures.append(arcade.load_texture("images/player/tile0" + str(i) + ".png"))
            for i in range(18, 27):
                self.player.walk_down_textures.append(arcade.load_texture("images/player/tile0" + str(i) + ".png"))
            for i in range(28, 36):
                self.player.walk_right_textures.append(arcade.load_texture("images/player/tile0" + str(i) + ".png"))
        if arg == "enemy":
            self.enemy.stand_left_textures.append(arcade.load_texture("images/enemy/tile009.png"))
            self.enemy.stand_right_textures.append(arcade.load_texture("images/enemy/tile027.png"))
            self.enemy.texture_change_distance = 20
            self.enemy.scale = 0.8
            for i in range(9):
                self.enemy.walk_up_textures.append(arcade.load_texture("images/enemy/tile00" + str(i) + ".png"))
            for i in range(10, 18):
                self.enemy.walk_left_textures.append(arcade.load_texture("images/enemy/tile0" + str(i) + ".png"))
            for i in range(18, 27):
                self.enemy.walk_down_textures.append(arcade.load_texture("images/enemy/tile0" + str(i) + ".png"))
            for i in range(28, 36):
                self.enemy.walk_right_textures.append(arcade.load_texture("images/enemy/tile0" + str(i) + ".png"))

    def get_vector(self, enemy):
        vector = []
        vector.append(0)
        vector.append(0)
        distance = [self.player.position[0] - enemy.position[0], self.player.position[1] - enemy.position[1]]
        sum = abs(abs(distance[0])+abs(distance[1]))
        if sum != 0:
            vector[0] = (abs(distance[0])/sum)
            vector[1] = (abs(distance[1])/sum)
        return vector

    def get_radius(self, p_pos, e_pos):
        distance = []
        distance.append(abs(p_pos[0]-e_pos[0]))
        distance.append(abs(p_pos[1]-e_pos[1]))
        radius = sqrt(distance[0]+distance[1])
        return radius

    def follow(self, enemy):
        vector = untitled.get_vector(self, enemy)
        if self.get_radius(self.player.position, enemy.position)<15 and self.get_radius(self.player.position, enemy.position)>5:
            if self.player.position[0] > enemy.position[0] and self.player.position[1] > enemy.position[1]: #going upright
                enemy.change_y = MOVEMENT_SPEED*vector[1]*ENEMY_SPEED_MODIFIER
                enemy.change_x = MOVEMENT_SPEED*vector[0]*ENEMY_SPEED_MODIFIER
                if vector[0] > vector[1]:
                    enemy.state = 1
                else:
                    enemy.state = 3
            elif self.player.position[0] < enemy.position[0] and self.player.position[1] > enemy.position[1]: #going upleft
                enemy.change_y = MOVEMENT_SPEED*vector[1]*ENEMY_SPEED_MODIFIER
                enemy.change_x = -MOVEMENT_SPEED*vector[0]*ENEMY_SPEED_MODIFIER
                if vector[0] > vector[1]:
                    enemy.state = 2
                else:
                    enemy.state = 3
            elif self.player.position[0] > enemy.position[0] and self.player.position[1] < enemy.position[1]: #going downright
                enemy.change_y = -MOVEMENT_SPEED*vector[1]*ENEMY_SPEED_MODIFIER
                enemy.change_x = MOVEMENT_SPEED*vector[0]*ENEMY_SPEED_MODIFIER
                if vector[0] > vector[1]:
                    enemy.state = 1
                else:
                    enemy.state = 4
            elif self.player.position[0] < enemy.position[0] and self.player.position[1] < enemy.position[1]: #going downleft
                enemy.change_y = -MOVEMENT_SPEED*vector[1]*ENEMY_SPEED_MODIFIER
                enemy.change_x = -MOVEMENT_SPEED*vector[0]*ENEMY_SPEED_MODIFIER
                if vector[0] > vector[1]:
                    enemy.state = 2
                else:
                    enemy.state = 4
            else:
                enemy.change_y = 0
                enemy.change_x = 0
        else:
            enemy.change_y = 0
            enemy.change_x = 0

    def on_draw(self):
        arcade.start_render()
        if self.player.position[1] > self.enemy.position[1]:
            self.player_list.draw()
            self.enemy_list.draw()
        else:
            self.enemy_list.draw()
            self.player_list.draw()
        #distance = self.get_radius(self.player.position, self.enemy.position)
        #distance_display = f"Distance: {distance}"
        #arcade.draw_text(distance_display, 10, 60, arcade.color.WHITE, 14)
        for i in range(ENEMY_COUNT):
            untitled.follow(self, self.enemy_list[i])

    def update(self, delta_time: float):
        self.player_list.update()
        self.player_list.update_animation()
        self.enemy_list.update()
        self.enemy_list.update_animation()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            self.player.change_y = MOVEMENT_SPEED*PLAYER_SPEED_MODIFIER
        elif key == arcade.key.DOWN:
            self.player.change_y = -MOVEMENT_SPEED*PLAYER_SPEED_MODIFIER
        elif key == arcade.key.LEFT:
            self.player.change_x = -MOVEMENT_SPEED*PLAYER_SPEED_MODIFIER
        elif key == arcade.key.RIGHT:
            self.player.change_x = MOVEMENT_SPEED*PLAYER_SPEED_MODIFIER
        if key == arcade.key.Q:
            self.enemy.change_x = 100
            self.enemy.change_y = 100

    def on_key_release(self, key, modifiers):
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player.change_x = 0
        if key == arcade.key.W or key == arcade.key.S:
            self.enemy.change_y = 0
        elif key == arcade.key.A or key == arcade.key.D:
            self.enemy.change_x = 0
        if key == arcade.key.ESCAPE:
            arcade.close_window()


def main():
    game = untitled()
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()


