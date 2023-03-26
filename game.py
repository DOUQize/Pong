import arcade
from random import randint
import time


ROCET_SPEED = 3
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 500


class Pong(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Pong")
        self.background_color = [20, 20, 20]
        self.scene = None

    def setup(self):
        self.scene = arcade.Scene()

        self.ball = Ball()
        self.rocet = Rocet()
        self.rocetAI = RocetAI()
        self.scene.add_sprite("Ball", self.ball)
        self.scene.add_sprite("Rocet", self.rocet)
        self.scene.add_sprite("RocetAI", self.rocetAI)

        self.cost0 = Cost(0)
        self.cost0.position = [50, SCREEN_HEIGHT-50]
        self.cost1 = Cost(1)
        self.cost1.position = [-100, SCREEN_HEIGHT-50]
        self.cost2 = Cost(2)
        self.cost2.position = [-100, SCREEN_HEIGHT-50]
        self.cost3 = Cost(3)
        self.cost3.position = [-100, SCREEN_HEIGHT-50]
        self.cost4 = Cost(4)
        self.cost4.position = [-100, SCREEN_HEIGHT-50]
        self.scene.add_sprite("Cost0", self.cost0)
        self.scene.add_sprite("Cost1", self.cost1)
        self.scene.add_sprite("Cost2", self.cost2)
        self.scene.add_sprite("Cost3", self.cost3)
        self.scene.add_sprite("Cost4", self.cost4)

        self.cost0AI = Cost(0)
        self.cost0AI.position = [SCREEN_WIDTH-50, SCREEN_HEIGHT-50]
        self.cost1AI = Cost(1)
        self.cost1AI.position = [-100, SCREEN_HEIGHT-50]
        self.cost2AI = Cost(2)
        self.cost2AI.position = [-100, SCREEN_HEIGHT-50]
        self.cost3AI = Cost(3)
        self.cost3AI.position = [-100, SCREEN_HEIGHT-50]
        self.cost4AI = Cost(4)
        self.cost4AI.position = [-100, SCREEN_HEIGHT-50]
        self.scene.add_sprite("Cost0AI", self.cost0AI)
        self.scene.add_sprite("Cost1AI", self.cost1AI)
        self.scene.add_sprite("Cost2AI", self.cost2AI)
        self.scene.add_sprite("Cost3AI", self.cost3AI)
        self.scene.add_sprite("Cost4AI", self.cost4AI)


    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.A:
            self.rocet.change_y = ROCET_SPEED
        if symbol == arcade.key.D:
            self.rocet.change_y = -ROCET_SPEED

    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == arcade.key.A:
            self.rocet.change_y = 0
        if symbol == arcade.key.D:
            self.rocet.change_y = 0

    def on_draw(self):
        self.clear()
        self.scene.draw()

    def update(self, delta_time: float):
        self.ball.update()
        self.rocet.update()
        self.rocetAI.update()

        if self.rocetAI.center_y < self.ball.center_y:
            self.rocetAI.change_y = ROCET_SPEED
        if self.rocetAI.center_y > self.ball.center_y:
            self.rocetAI.change_y = -ROCET_SPEED

        if arcade.check_for_collision(self.ball, self.rocet):
            self.ball.change_x = -self.ball.change_x
            self.ball.change_y = randint(-5, 5)
        if arcade.check_for_collision(self.ball, self.rocetAI):
            self.ball.change_x = -self.ball.change_x
            self.ball.change_y = randint(-5, 5)

        if self.ball.player_score == 1:
            self.cost1.center_x = 50
            self.cost0.center_x = -100
        if self.ball.player_score == 2:
            self.cost2.center_x = 50
            self.cost1.center_x = -100
        if self.ball.player_score == 3:
            self.cost3.center_x = 50
            self.cost2.center_x = -100
        if self.ball.player_score == 4:
            self.cost4.center_x = 50
            self.cost3.center_x = -100

        if self.ball.bot_score == 1:
            self.cost1AI.center_x = SCREEN_WIDTH-50
            self.cost0AI.center_x = -100
        if self.ball.bot_score == 2:
            self.cost2AI.center_x = SCREEN_WIDTH-50
            self.cost1AI.center_x = -100
        if self.ball.bot_score == 3:
            self.cost3AI.center_x = SCREEN_WIDTH-50
            self.cost2AI.center_x = -100
        if self.ball.bot_score == 4:
            self.cost4AI.center_x = SCREEN_WIDTH-50
            self.cost3AI.center_x = -100


        if self.ball.player_score == 5:
            arcade.close_window()
            print("You win!")
        if self.ball.bot_score == 5:
            arcade.close_window()
            print("You lost!")


class Ball(arcade.Sprite):
    def __init__(self):
        super().__init__("ball.png", 0.8)
        self.center_y = SCREEN_HEIGHT/2
        self.center_x = SCREEN_WIDTH/2
        self.change_y = randint(-5, 5)
        self.change_x = 5
        self.player_score = 0
        self.bot_score = 0

    def update(self):
        self.center_y += self.change_y
        self.center_x += self.change_x
        if self.center_y - 15 < 0:
            self.change_y -= self.change_y * 2
        if self.center_y + 15 > SCREEN_HEIGHT:
            self.change_y -= self.change_y * 2
        if self.center_x - 13 < 0:
            self.center_y = SCREEN_HEIGHT/2
            self.center_x = SCREEN_WIDTH/2
            self.change_y = randint(-5, 5)
            self.change_x = 5
            time.sleep(1)
            self.bot_score += 1
        if self.center_x + 13 > SCREEN_WIDTH:
            self.center_y = SCREEN_HEIGHT/2
            self.center_x = SCREEN_WIDTH/2
            self.change_y = randint(-5, 5)
            self.change_x = 5
            time.sleep(1)
            self.player_score += 1


class Rocet(arcade.Sprite):
    def __init__(self):
        super().__init__("rocet.png", 1)
        self.center_y = SCREEN_HEIGHT/2
        self.center_x = 100
        self.change_y = 0

    def update(self):
        self.center_y += self.change_y
        if self.center_y <= 33:
            self.center_y = 33
        if self.center_y >= SCREEN_HEIGHT - 33:
            self.center_y = SCREEN_HEIGHT - 33


class RocetAI(arcade.Sprite):
    def __init__(self):
        super().__init__("rocet.png", 1)
        self.center_y = SCREEN_HEIGHT/2
        self.center_x = SCREEN_WIDTH - 100
        self.change_y = 0

    def update(self):
        self.center_y += self.change_y
        if self.center_y <= 33:
            self.center_y = 33
        if self.center_y >= SCREEN_HEIGHT - 33:
            self.center_y = SCREEN_HEIGHT - 33


class Cost(arcade.Sprite):
    def __init__(self, num):
        super().__init__(f"numders/{num}.png")

    def update(self):
        self.center_x = self.center_x




if __name__ == "__main__":
    game = Pong()
    game.setup()
    arcade.run()