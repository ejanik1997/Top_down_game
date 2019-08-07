import arcade

WIDTH = 1280
HEIGHT = 720
MOVEMENT_SPEED = 2
PLAYER_SCALE = 0.75


class untitled(arcade.Window):

    def __init__(self, width, height):
        super().__init__(width, height)
        arcade.set_background_color(arcade.color.BABY_BLUE)
        self.player_list = None
        self.enemy_list = None
        #self.player_sprite = None
        self.enemy = None
        #self.physics_engine = None
        self.walls = None
        self.player = None

    def setup(self): #my game
        self.player_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()
        #self.walls = arcade.SpriteList()
        self.player = arcade.AnimatedWalkingSprite()
        self.enemy = arcade.AnimatedWalkingSprite()

        self.enemy.stand_left_textures = []
        self.enemy.stand_right_textures = []
        self.enemy.walk_left_textures = []
        self.enemy.walk_right_textures = []
        self.enemy.walk_down_textures = []
        self.enemy.walk_up_textures = []

        self.player.stand_left_textures = []
        self.player.stand_right_textures = []
        self.player.walk_left_textures = []
        self.player.walk_right_textures = []
        self.player.walk_down_textures = []
        self.player.walk_up_textures = []

        self.player.stand_left_textures.append(arcade.load_texture("images/player/tile009.png"))
        self.player.stand_right_textures.append(arcade.load_texture("images/player/tile027.png"))

        self.enemy.stand_left_textures.append(arcade.load_texture("images/enemy/tile009.png"))
        self.enemy.stand_right_textures.append(arcade.load_texture("images/enemy/tile027.png"))

        self.player.walk_left_textures.append(arcade.load_texture("images/player/tile010.png"))
        self.player.walk_left_textures.append(arcade.load_texture("images/player/tile011.png"))
        self.player.walk_left_textures.append(arcade.load_texture("images/player/tile012.png"))
        self.player.walk_left_textures.append(arcade.load_texture("images/player/tile013.png"))
        self.player.walk_left_textures.append(arcade.load_texture("images/player/tile014.png"))
        self.player.walk_left_textures.append(arcade.load_texture("images/player/tile015.png"))
        self.player.walk_left_textures.append(arcade.load_texture("images/player/tile016.png"))
        self.player.walk_left_textures.append(arcade.load_texture("images/player/tile017.png"))
        self.enemy.walk_left_textures.append(arcade.load_texture("images/enemy/tile010.png"))
        self.enemy.walk_left_textures.append(arcade.load_texture("images/enemy/tile011.png"))
        self.enemy.walk_left_textures.append(arcade.load_texture("images/enemy/tile012.png"))
        self.enemy.walk_left_textures.append(arcade.load_texture("images/enemy/tile013.png"))
        self.enemy.walk_left_textures.append(arcade.load_texture("images/enemy/tile014.png"))
        self.enemy.walk_left_textures.append(arcade.load_texture("images/enemy/tile015.png"))
        self.enemy.walk_left_textures.append(arcade.load_texture("images/enemy/tile016.png"))
        self.enemy.walk_left_textures.append(arcade.load_texture("images/enemy/tile017.png"))

        self.player.walk_right_textures.append(arcade.load_texture("images/player/tile028.png"))
        self.player.walk_right_textures.append(arcade.load_texture("images/player/tile029.png"))
        self.player.walk_right_textures.append(arcade.load_texture("images/player/tile030.png"))
        self.player.walk_right_textures.append(arcade.load_texture("images/player/tile031.png"))
        self.player.walk_right_textures.append(arcade.load_texture("images/player/tile032.png"))
        self.player.walk_right_textures.append(arcade.load_texture("images/player/tile033.png"))
        self.player.walk_right_textures.append(arcade.load_texture("images/player/tile034.png"))
        self.player.walk_right_textures.append(arcade.load_texture("images/player/tile035.png"))
        self.enemy.walk_right_textures.append(arcade.load_texture("images/enemy/tile028.png"))
        self.enemy.walk_right_textures.append(arcade.load_texture("images/enemy/tile029.png"))
        self.enemy.walk_right_textures.append(arcade.load_texture("images/enemy/tile030.png"))
        self.enemy.walk_right_textures.append(arcade.load_texture("images/enemy/tile031.png"))
        self.enemy.walk_right_textures.append(arcade.load_texture("images/enemy/tile032.png"))
        self.enemy.walk_right_textures.append(arcade.load_texture("images/enemy/tile033.png"))
        self.enemy.walk_right_textures.append(arcade.load_texture("images/enemy/tile034.png"))
        self.enemy.walk_right_textures.append(arcade.load_texture("images/enemy/tile035.png"))

        self.player.walk_down_textures.append(arcade.load_texture("images/player/tile018.png"))
        self.player.walk_down_textures.append(arcade.load_texture("images/player/tile019.png"))
        self.player.walk_down_textures.append(arcade.load_texture("images/player/tile020.png"))
        self.player.walk_down_textures.append(arcade.load_texture("images/player/tile021.png"))
        self.player.walk_down_textures.append(arcade.load_texture("images/player/tile022.png"))
        self.player.walk_down_textures.append(arcade.load_texture("images/player/tile023.png"))
        self.player.walk_down_textures.append(arcade.load_texture("images/player/tile024.png"))
        self.player.walk_down_textures.append(arcade.load_texture("images/player/tile025.png"))
        self.player.walk_down_textures.append(arcade.load_texture("images/player/tile026.png"))
        self.enemy.walk_down_textures.append(arcade.load_texture("images/enemy/tile018.png"))
        self.enemy.walk_down_textures.append(arcade.load_texture("images/enemy/tile019.png"))
        self.enemy.walk_down_textures.append(arcade.load_texture("images/enemy/tile020.png"))
        self.enemy.walk_down_textures.append(arcade.load_texture("images/enemy/tile021.png"))
        self.enemy.walk_down_textures.append(arcade.load_texture("images/enemy/tile022.png"))
        self.enemy.walk_down_textures.append(arcade.load_texture("images/enemy/tile023.png"))
        self.enemy.walk_down_textures.append(arcade.load_texture("images/enemy/tile024.png"))
        self.enemy.walk_down_textures.append(arcade.load_texture("images/enemy/tile025.png"))
        self.enemy.walk_down_textures.append(arcade.load_texture("images/enemy/tile026.png"))

        self.player.walk_up_textures.append(arcade.load_texture("images/player/tile000.png"))
        self.player.walk_up_textures.append(arcade.load_texture("images/player/tile001.png"))
        self.player.walk_up_textures.append(arcade.load_texture("images/player/tile001.png"))
        self.player.walk_up_textures.append(arcade.load_texture("images/player/tile003.png"))
        self.player.walk_up_textures.append(arcade.load_texture("images/player/tile004.png"))
        self.player.walk_up_textures.append(arcade.load_texture("images/player/tile005.png"))
        self.player.walk_up_textures.append(arcade.load_texture("images/player/tile006.png"))
        self.player.walk_up_textures.append(arcade.load_texture("images/player/tile007.png"))
        self.player.walk_up_textures.append(arcade.load_texture("images/player/tile008.png"))
        self.enemy.walk_up_textures.append(arcade.load_texture("images/enemy/tile000.png"))
        self.enemy.walk_up_textures.append(arcade.load_texture("images/enemy/tile001.png"))
        self.enemy.walk_up_textures.append(arcade.load_texture("images/enemy/tile001.png"))
        self.enemy.walk_up_textures.append(arcade.load_texture("images/enemy/tile003.png"))
        self.enemy.walk_up_textures.append(arcade.load_texture("images/enemy/tile004.png"))
        self.enemy.walk_up_textures.append(arcade.load_texture("images/enemy/tile005.png"))
        self.enemy.walk_up_textures.append(arcade.load_texture("images/enemy/tile006.png"))
        self.enemy.walk_up_textures.append(arcade.load_texture("images/enemy/tile007.png"))
        self.enemy.walk_up_textures.append(arcade.load_texture("images/enemy/tile008.png"))

        self.player.texture_change_distance = 20
        self.enemy.texture_change_distance = 20

        self.player.center_x = WIDTH // 2
        self.player.center_y = HEIGHT // 2
        self.player.scale = 0.8

        self.enemy.center_x = WIDTH // 3
        self.enemy.center_y = HEIGHT // 3
        self.enemy.scale = 0.8

        self.player_list.append(self.player)
        self.enemy_list.append(self.enemy)

        #self.player_sprite = arcade.Sprite("images/player.jpg", 0.1)
        #self.player_sprite.center_x = 100
        #self.player_sprite.center_y = 100
        #self.player_list.append(self.player_sprite)

        #self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.walls)

    def on_draw(self):
        arcade.start_render()
        self.player_list.draw()
        self.enemy_list.draw()

    def update(self, delta_time: float):
        #self.physics_engine.update()
        self.player_list.update()
        self.player_list.update_animation()
        self.enemy_list.update()
        self.enemy_list.update_animation()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            self.player.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player.change_x = 0


def main():
    game = untitled(WIDTH, HEIGHT)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()


